def trap_water(heights: list) -> int:
    if len(heights) == 0:
        return 0
    
    result = 0
    left, right = 0, len(heights) - 1
    left_max, right_max = heights[left], heights[right]
    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, heights[left])
            result += left_max - heights[left]
        else:
            right -= 1
            right_max = max(right_max, heights[right])
            result += right_max - heights[right]
    return result