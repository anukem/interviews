
[Easy]
[[Interview Question]]

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

**Input:** nums = [1,3,5,6], target = 5
**Output:** 2

**Example 2:**

**Input:** nums = [1,3,5,6], target = 2
**Output:** 1

**Example 3:**

**Input:** nums = [1,3,5,6], target = 7
**Output:** 4

---
This is just binary search with a little extra on top. If you don't find the element, there are a couple cases you need to be mindful of. If mid is out of bounds, its because it belongs at the index right outside of the existing array. If the mid point it lands on is greater than the target, than we know it has to be at that index, because after shifting everything over to make room, it ends up in the same spot. And for every other case, its always one above where the mid is.


Final solution after 20 minutes:
```python
def searchInsert(self, nums: List[int], target: int) -> int:

      found = False
      left = 0
      right = len(nums) - 1
      mid = len(nums) // 2
      answer = None

      while not found and left < right:
        if nums[mid] == target:
          found = True
          answer = mid
        elif nums[mid] > target:
          right = mid - 1
          mid = (left + right) // 2
        else:
          left = mid + 1
          mid = ((left + right) // 2)

      if found:
        return answer
      else:
        if mid < 0:
          return 0
        if nums[mid] > target:
          return mid
        elif nums[mid] == target:
          return mid
        else:
          return mid + 1
```



