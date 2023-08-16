#Solution 1: Using Hashmap
#Time Complexity: O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_element = {}
        for i in nums:
            if i not in majority_element:
                majority_element[i] = nums.count(i)
        max_value = max(zip(majority_element.values(), majority_element.keys()))[1]
        return max_value

#Solution 2: Using Boyer Moore Algorithm
#Time Complexity: O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res,count = 0,0
        for i in nums:
            if count == 0:
                res = i
            if i == res:
                count += 1
            elif i != res:
                count -= 1 
        return res