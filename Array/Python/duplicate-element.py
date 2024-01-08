# Approach 1: Using hashmap
# Time complexity is O(n)
class Solution:
    def containsDuplicate(self, nums) -> bool:
        hash_map = {}
        for i in nums:
            if i in hash_map:
                return True
            else:
                hash_map[i] = i
        return False

# Approach 2: Using Sets
# Time complexity is O(n)
class Solution:
    def containsDuplicate(self, nums) -> bool:
        if len(list(nums)) == len(set(nums)):
            return False
        else:
            return True
