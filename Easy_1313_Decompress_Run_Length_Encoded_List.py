# 1313. Decompress Run-Length Encoded List

# Brute Force O(n^2) 68 ms, Faster than 77.44%, 14.5 MB, Less than 5.12%
#class Solution:
#    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
#        ans = []
        
#        for i in range(len(nums)//2):
#            [freq, val] = [nums[2*i], nums[2*i + 1]]
#            for j in range(freq):
#                ans.append(val)
            
#        return ans


# Linear Scan 64 ms, Faster than 91.29%, 14.6 MB, Less than 5.12%
#class Solution:
#    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
#        ans = []
        
#        for i in range(0, len(nums), 2):
            
#            freq = nums[i]
#            val  = nums[i + 1]
            
#            ans.extend([val]*freq)
            
#        return ans

# No Library Function 60 ms, Faster than 97.32 %, 14.6 MB, Less than 5.12%
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        ans = []
        
        for i in range(0, len(nums), 2):
            
            ans += (nums[i] * [nums[i+1]])
        
        return ans