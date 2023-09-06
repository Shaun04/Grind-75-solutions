class Solution:
    def trap(self, height: List[int]) -> int:
        left, right , max_height, ans= 0, len(height) - 1, 0, 0
        while left < right:
            min_height = min(height[left], height[right])
            max_height = max(min_height, max_height)
            ans += max_height - min_height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans