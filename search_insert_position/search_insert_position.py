from typing import List
def searchInsert( nums: List[int], target: int) -> int:

  found = False
  left = 0
  right = len(nums) - 1
  mid = len(nums) // 2
  answer = -1

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

assert searchInsert([1,2,3,4], 2) == 1
assert searchInsert([1,2,3,4], 4) == 3
assert searchInsert([1,2,3,4], 5) == 4
