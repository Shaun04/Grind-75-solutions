#Approach 1: Using Set
class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash_set = set()
        for i in s:
            if i in hash_set:
                hash_set.remove(i)
            else:
                hash_set.add(i)
        if len(hash_set) != 0:
            return len(s) - len(hash_set) + 1
        else:
            return len(s)

#Approach 2: Using Dictonary
class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd_count = 0
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
            if d[i] % 2 == 1:
                odd_count += 1
            else:
                odd_count -= 1
        if odd_count > 1:
            return len(s) - odd_count + 1
        return len(s)
        
        