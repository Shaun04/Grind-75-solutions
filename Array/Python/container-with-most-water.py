class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            area = (right - left) * min(height[left],height[right])
            max_area = max(area, max_area)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_area