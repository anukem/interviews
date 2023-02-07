import functools
from heapq import heappush, heappop


def getMaxArea(acc, currentValue):
    maxSeen, start, end, startValue, endValue = acc
    val, curIndex = currentValue
    if curIndex > start and curIndex < end:
        return maxSeen, start, end, startValue, endValue

    indexToCheck = (
        start
        if computeArea(startValue, val, abs(start - curIndex))
        > computeArea(endValue, val, abs(end - curIndex))
        else end
    )
    valueToCheck = startValue if indexToCheck == start else endValue

    newMax = computeArea(valueToCheck, val, abs(indexToCheck - curIndex))
    if newMax > maxSeen:
        if indexToCheck == start:
            return newMax, start, curIndex, startValue, val
        else:
            return newMax, curIndex, end, val, endValue
    else:
        return maxSeen, start, end, startValue, endValue


def computeArea(left, right, distance):
    return min(left, right) * distance


def getMax(acc, currentValue):
    heappush(acc, currentValue)
    if len(acc) > 2:
        heappop(acc)
    return acc


def maxArea(height) -> int:
    if len(height) == 0 or len(height) == 1:
        return 0

    if (len(height)) == 2:
        return computeArea(height[0], height[1], 1)

    enumHeight = [(y, x) for x, y in enumerate(height)]
    enumHeight.sort()
    enumHeight.reverse()
    right, left = enumHeight[0], enumHeight[1]

    answer = functools.reduce(
        getMaxArea,
        enumHeight[2:],
        (
            computeArea(left[0], right[0], abs(left[1] - right[1])),
            left[1],
            right[1],
            left[0],
            right[0],
        ),
    )

    return answer[0]
