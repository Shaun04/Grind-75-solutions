class Solution:
    def closestToZero (self,arr, n):
        arr.sort()
        left, right = 0, n - 1
        min_sum = 0
        while right > left:
            sum = arr[left] + arr[right]
            if sum == 0:
                return sum
            elif min_sum == 0 or abs(min_sum) > abs(sum):
                min_sum = sum
            elif abs(min_sum) == abs(sum):
                if min_sum < sum:
                    min_sum = sum
                    
            if sum > 0:
                right -= 1
            else:
                left += 1
        return min_sum