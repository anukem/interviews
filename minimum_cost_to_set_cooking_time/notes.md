Minimum Cost to Set Cooking Time

Medium

A generic microwave supports cooking times for:

-   at least `1` second.
-   at most `99` minutes and `99` seconds.

To set the cooking time, you push **at most four digits**. The microwave normalizes what you push as four digits by **prepending zeroes**. It interprets the **first** two digits as the minutes and the **last** two digits as the seconds. It then **adds** them up as the cooking time. For example,

-   You push `9` `5` `4` (three digits). It is normalized as `0954` and interpreted as `9` minutes and `54` seconds.
-   You push `0` `0` `0` `8` (four digits). It is interpreted as `0` minutes and `8` seconds.
-   You push `8` `0` `9` `0`. It is interpreted as `80` minutes and `90` seconds.
-   You push `8` `1` `3` `0`. It is interpreted as `81` minutes and `30` seconds.

You are given integers `startAt`, `moveCost`, `pushCost`, and `targetSeconds`. **Initially**, your finger is on the digit `startAt`. Moving the finger above **any specific digit** costs `moveCost` units of fatigue. Pushing the digit below the finger **once** costs `pushCost` units of fatigue.

There can be multiple ways to set the microwave to cook for `targetSeconds` seconds but you are interested in the way with the minimum cost.

Return _the **minimum cost** to set_ `targetSeconds` _seconds of cooking time_.

Remember that one minute consists of `60` seconds.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/12/30/1.png)

**Input:** startAt = 1, moveCost = 2, pushCost = 1, targetSeconds = 600
**Output:** 6
**Explanation:** The following are the possible ways to set the cooking time.
- 1 0 0 0, interpreted as 10 minutes and 0 seconds.
  The finger is already on digit 1, pushes 1 (with cost 1), moves to 0 (with cost 2), pushes 0 (with cost 1), pushes 0 (with cost 1), and pushes 0 (with cost 1).
  The cost is: 1 + 2 + 1 + 1 + 1 = 6. This is the minimum cost.
- 0 9 6 0, interpreted as 9 minutes and 60 seconds. That is also 600 seconds.
  The finger moves to 0 (with cost 2), pushes 0 (with cost 1), moves to 9 (with cost 2), pushes 9 (with cost 1), moves to 6 (with cost 2), pushes 6 (with cost 1), moves to 0 (with cost 2), and pushes 0 (with cost 1).
  The cost is: 2 + 1 + 2 + 1 + 2 + 1 + 2 + 1 = 12.
- 9 6 0, normalized as 0960 and interpreted as 9 minutes and 60 seconds.
  The finger moves to 9 (with cost 2), pushes 9 (with cost 1), moves to 6 (with cost 2), pushes 6 (with cost 1), moves to 0 (with cost 2), and pushes 0 (with cost 1).
  The cost is: 2 + 1 + 2 + 1 + 2 + 1 = 9.

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/12/30/2.png)

**Input:** startAt = 0, moveCost = 1, pushCost = 2, targetSeconds = 76
**Output:** 6
**Explanation:** The optimal way is to push two digits: 7 6, interpreted as 76 seconds.
The finger moves to 7 (with cost 1), pushes 7 (with cost 2), moves to 6 (with cost 1), and pushes 6 (with cost 2). The total cost is: 1 + 2 + 1 + 2 = 6
Note other possible ways are 0076, 076, 0116, and 116, but none of them produces the minimum cost.

**Constraints:**

-   `0 <= startAt <= 9`
-   `1 <= moveCost, pushCost <= 105`
-   `1 <= targetSeconds <= 6039`

---

So this question feels like some combo of "how many combinations of coins can i use to make some value" and what's the minimum cost of some permutation.

For the first part, I could use a greedy algorithm that keeps trying to take the largest value at my current index, and if it can, it returns the result of taking that amount as well as what would happen if it didn't.

This ended up being close to what I actually did. I kept trying to generate different permutations of minutes and seconds that met the target and then checked to see if they were valid permutations before returning.

Spent way too long on this one, but my solution was the following:

```python
def get_possible_times(seconds):
        totalMinutes = seconds // 60
        remainingSeconds = seconds % 60
        possibilities = []
        while totalMinutes > 0:
          if totalMinutes <= 99 and remainingSeconds <= 99:
            possibilities.append((totalMinutes, remainingSeconds))

          totalMinutes -= 1
          remainingSeconds += 60

        if remainingSeconds <= 99:
          possibilities.append((0, remainingSeconds))

        return possibilities


      def convert_possible_times_to_path(time):
        minute, seconds = time

        seconds_with_zeroes = "0" + str(seconds) if seconds < 10 else str(seconds)
        paths = []
        if minute == 0:
          if seconds < 10:
            paths.append(str(seconds))

          paths.append(seconds_with_zeroes)
          paths.append("0" + str(minute) + seconds_with_zeroes)
          paths.append(str(minute) + seconds_with_zeroes)
        elif minute < 10:
          paths.append("0" + str(minute) + seconds_with_zeroes)
          paths.append(str(minute) + seconds_with_zeroes)
        else:
          paths.append(str(minute) + seconds_with_zeroes)


        return paths

      def reduce_cost(path, collectedCost, prevValue):
        if not path:
          return collectedCost

        if str(prevValue) == path[0]:
          collectedCost += pushCost
        else:
          collectedCost += moveCost
          collectedCost += pushCost

        return reduce_cost(path[1:],  collectedCost, path[0])

      def calculate_cost(paths):
        costs = []
        for path in paths:
          print(path)
          costs.append(reduce_cost([num for num in path], 0, startAt))

        print(costs)
        return min(costs)


      paths = [convert_possible_times_to_path(time) for time in get_possible_times(targetSeconds)]

      costs = [calculate_cost(path) for path in paths]

      return min(costs) if costs else -1
```


