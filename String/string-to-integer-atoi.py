class Solution:
    def myAtoi(self, s: str) -> int:
        left, right = 0, len(s)
        ans = 0
        positive, negative = False, False
        while left < right and s[left] == " ":
            left += 1

        if left < right and s[left] == "+":
            positive = True
            left += 1

        if left < right and s[left] == "-":
            negative = True
            left += 1

        while left < right and "0" <= s[left] <= "9":
            ans = ans * 10 + (ord(s[left]) - ord('0'))
            left += 1

        if negative:
            ans = -ans
        
        if positive and negative:
            return 0
    
        INT_MAX, INT_MIN = 2**31-1, -2**31

        if ans < INT_MIN:
            ans = INT_MIN
        
        if ans > INT_MAX:
            ans = INT_MAX

        return ans 


        

