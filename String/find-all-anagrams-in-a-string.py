class Solution:
    def findAnagrams(self, s: str, p: str):
        s_counter = Counter(s[:len(p)])
        p_counter = Counter(p)
        index = []
        for i in range(len(p), len(s)):
            if s_counter == p_counter:
                index.append(i - len(p))
            s_counter[s[i]] += 1
            s_counter[s[i-len(p)]] -= 1

        if p_counter == s_counter:
            index.append(len(s) - len(p))
        
        return index
