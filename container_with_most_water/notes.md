You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return _the maximum amount of water a container can store_.

**Notice** that you may not slant the container.

---
I originally started out with a n^2 solution that simply checks all pairs of lines and computes their area and returns the solution. This works on 48 our of the 61 test cases, but fails beyond that. So that lets me know we need to be more clever with which pairs we check and probably need to get to the result in some linear fashion.

So my next idea was to start with the two largest lines and compute their area. From there, I would expand out checking the next highest line either to the left or the right until there were no more lines to check in either direction. After that I could return the result.

So in an array of [1,3,6,2,9,5], I would first compute (width *height) = (4 -2)* (min(6, 9)) = 12. From there, I would move to the next hightest number which is 5 and compare the max distance from either 9 to 5 or 6 to five and compute the area. That would yield 15 for 6 and 5 and then I know that between those two lines, nothing can be greater.

After about an hour and a half, here's the solution I came up with

```
import functools

from heapq import heappush, heappop

class Solution:

  
  

def maxArea(self, height: List[int]) -> int:

def computeArea(left, right, distance):

return min(left, right) * distance

  

if len(height) == 0 or len(height) == 1:

return 0

  

if (len(height)) == 2:

return computeArea(height[0], height[1], 1)

  
  

def getMax(acc, currentValue):

heappush(acc, currentValue)

if len(acc) > 2:

heappop(acc)

return acc

pq = []

max_val = max(height)

enumHeight = [(y, x )for x, y in enumerate(height)]

enumHeight.sort()

enumHeight.reverse()

right, left = enumHeight[0], enumHeight[1]

  

def getMaxArea(acc, currentValue):

maxSeen, start, end, startValue, endValue = acc

val, curIndex = currentValue

if curIndex > start and curIndex < end:

return maxSeen, start, end, startValue, endValue

indexToCheck = start if computeArea(startValue, val, abs(start - curIndex)) > computeArea(endValue, val, abs( end - curIndex)) else end

valueToCheck = startValue if indexToCheck == start else endValue

  

newMax = computeArea(valueToCheck, val, abs(indexToCheck - curIndex))

if newMax > maxSeen:

if indexToCheck == start:

return newMax, start, curIndex, startValue, val

else:

return newMax, curIndex, end, val, endValue

else:

return maxSeen, start, end, startValue, endValue

  

  
  
  
  

something = functools.reduce(getMaxArea, enumHeight[2:], (computeArea(left[0], right[0], abs(left[1] - right[1])), left[1], right[1], left[0], right[0]))

print(something)

 return something[0]
```

---
This solved 57/61 test cases.

The full solution requires using two pointers that start from the ends of the array. From there, you compute the area and increment/decrement the pointers based on which ever is smaller.

```
def container_with_most_water(heights):
        left, right = 0, len(heights) - 1
        max_area = 0
        while left < right:
            max_area = max(max_area, (right - left) * min(heights[left], heights[right]))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area
      
      return container_with_most_water(height)
```

