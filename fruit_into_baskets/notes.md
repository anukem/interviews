[Medium]
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array `fruits` where `fruits[i]` is the **type** of fruit the `ith` tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

- You only have **two** baskets, and each basket can only hold a **single type** of fruit. There is no limit on the amount of fruit each basket can hold.
- Starting from any tree of your choice, you must pick **exactly one fruit** from **every** tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
- Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Given the integer array `fruits`, return _the **maximum** number of fruits you can pick_.

---

So my thought here is to use two pointers.
The first will start at the beginning and the end with start at the `start + 1`.
From there, I'll try to expand outward while I can, and if I hit a point where I can't,
i'll record the max length I've seen thus far, and reset the pointers to be `start = end`, and `end = start + 1` and redo the process.
Note: the algorithm i described above didn't take into account the fact that the fruit immediately preceding the start might also
contribute to the size of of the largest number of fruits picked.

After 34 min, I came up with the following solution

```
```python
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
      start, end = 0, 1

      if len(fruits) == 0:
        return 0
      elif len(fruits) == 1:
        return 1
      elif len(fruits) == 2:
        return 2
      
      maxLength = 2
      baskets = set([fruits[0], fruits[1]])
      while end < len(fruits):
        if fruits[end] in baskets:
          maxLength = max(maxLength, end - start + 1)
          end += 1
        elif len(baskets) == 2:
          start = end - 1
          while fruits[start] == fruits[end - 1]:
            start -= 1
          start += 1
          baskets = set([fruits[start], fruits[end]])
        else:
          baskets.add(fruits[end])
          maxLength = max(maxLength, end - start + 1)
        
      return maxLength
```

The trickiest part was figuring out how to handle the reset of the starting pointer. In the general case, you'll want to make sure that the starting pointer always goes as far back as it can. Initially, I was traversing from wherever it was, up until I couldn't go any further, but when I realized that the longest sequence before that value is always made up of the same fruit, I noticed I could iterate backwards and get to the same result.

