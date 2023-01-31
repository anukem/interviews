_You are given an integer `n`.

Each number from `1` to `n` is grouped according to the sum of its digits.

Return _the number of groups that have the largest size_._

---
My thought process was to first iterate over all the numbers from 1 to n. At each step I would calculate what group n belonged to, and add it to the set of all numbers that match that value. From there, I could filter down the list of groups to be just those that are at least as large as the first element in the list. (Also need to sort from largest to smallest). After that I can return the length of the size of the those groups.

After 18 min, my solution was

```
def countLargestGroup(n):
        def calculate_size(n):
            str_of_n = str(n)
            total = 0
            for digit in str_of_n:
                total += int(digit)
            return total


        sizes = {}
        for i in range(1, n + 1):
            size = calculate_size(i)
            if size in sizes:
                sizes[size].append(i)
            else:
                sizes[size] = [i]

        groups = [y for x, y in sizes.items()]
        groups.sort()
        groups = list(filter(lambda x: len(x) == len(groups[0]), groups))

        return len(groups)

```

T.C(n) -> O(n) where n is the value of the input.
S.C(n) -> O(n) where n is the value of the input because we create and store an additional array for every number.


