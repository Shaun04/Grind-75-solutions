class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = set()
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                return result
            if nums[i] < 0 and nums[i] == nums[i-1]:
                continue
            first = nums[i]
            left,right = i + 1, len(nums) - 1
            while left < right:
                second, third = nums[left], nums[right]
                pot_ans = first + second + third
                if pot_ans < 0:
                    left += 1
                elif pot_ans > 0:
                    right -= 1
                else:
                    result.add((first, second, third))
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
                    
        return result