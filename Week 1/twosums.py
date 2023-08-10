class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in hash_map:
                return [hash_map[rem], i]
            else:
                hash_map[nums[i]] = i
