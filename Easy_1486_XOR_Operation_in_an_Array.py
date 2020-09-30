# 1486. XOR Operation in an Array

# 32 ms, Faster than 53.03 %, 14.2 MB, Less than 5.20%
#class Solution:
#    def xorOperation(self, n: int, start: int) -> int:
        
#        ans = 0
#        nums = []
        
#        for i in range(n):
#            nums.append(start + 2*i)
#            ans = ans ^ nums[i]
        
#        return ans
            
# 28 ms, Faster than 78.75 %, 14.1 MB, Less than 6.35%
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        ans = 0
        
        for i in range(n):
            nums = start + 2*i
            ans = ans ^ nums
        
        return ans
