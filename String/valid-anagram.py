# Method 1: Using Hashmap
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_map_s, hash_map_t = {}, {}
        for i in s:
            if i in hash_map_s:
                hash_map_s[i] += 1
            else:
                hash_map_s[i] = 1
        for i in t:
            if i in hash_map_t:
                hash_map_t[i] += 1
            else:
                hash_map_t[i] = 1
        for c in hash_map_s:
            if hash_map_s[c] != hash_map_t.get(c,0):
                return False
        return True

# Method 2: Using Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# Method 3: Using Sorting
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)