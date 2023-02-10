[Easy]
Write an algorithm to determine if a number `n` is happy.

A **happy number** is a number defined by the following process:

- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it **loops endlessly in a cycle** which does not include 1.
- Those numbers for which this process **ends in 1** are happy.

Return `true` _if_ `n` _is a happy number, and_ `false` _if not_.

---

The intuition here is that cycles that loop endlessly must visit the same number at least once. If we can design an algoritm that accounts for visiting a number at least once, we can return the right result.

In 10 minutes, here's what I came up with.

```
```python
def isHappy(self, n: int) -> bool:
      seen = {}
      val = str(n)
      seen[val] = 1
      while val != "1" and seen[val] != 2:
        digits = [x for x in val]
        val = str(sum([int(x)**2 for x in digits]))

        if val not in seen:
          seen[val] = 1
        else:
          seen[val] += 1
      


      return val == "1"
```

This solution O(n) where n is number of the largest possible cycle.

TODO: fun idea would be to think about how to design an algorithm or proof for what the size of the largest cycle is.
