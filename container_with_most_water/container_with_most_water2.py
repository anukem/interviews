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


print(container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49)
