# Using same array for prefix and postfix
# Time Complexity is O(n) and Space Complexity is O(1)
class Solution:
    def productExceptSelf(self, nums):
        answer = [1] * len(nums)
        left,right = nums[0], nums[-1]
        for i in range(len(nums) - 1):  
            answer[i+1] = left
            left = left * nums[i+1]
        for i in range(len(nums)-1,0,-1):
            answer[i-1] *= right
            right = right * nums[i-1]
        return answer

# Using different arrays for prefix and postfix
# Time Complexity is O(n) and Space Complexity is O(n)
class Solution:
    def productExceptSelf(self, nums):
        answer = []
        prefix,postfix = [1] * len(nums), [1] * len(nums)
        left,right = nums[0], nums[-1]
        for i in range(len(nums) - 1):  
            prefix[i+1] = left
            left = left * nums[i+1]
        for i in range(len(nums)-1,0,-1):
            postfix[i-1] = right
            right = right * nums[i-1]
        for i,j in zip(prefix,postfix):
            answer.append(i*j)
        return answer