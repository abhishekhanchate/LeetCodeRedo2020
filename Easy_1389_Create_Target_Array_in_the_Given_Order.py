#1389. Create Target Array in the Given Order

# Using Insert() 36 ms, Faster than 48.55%, 14.1 MB, Less than 5.03%
#class Solution:
#    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
#        target = []
        
#        for i in range(len(nums)):
            
#            val = nums[i]
#            ind = index[i]
            
#            target.insert(ind, val)
        
#        return target

# Without Using Insert() 32 ms, Faster than 74.52%, 14.1 MB, Less than 6.92%
#class Solution:
#    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
#        target = []
        
#        for i in range(len(index)):
            
#            target = target[:index[i]] + [nums[i]] + target[index[i]:]
        
#        return target
 
# Using Insert() and Pop() 28 ms, Faster than 92.13%, 14.2 MB, Less than 5.03 %
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        target = []
        
        for num in nums:
            target.insert(index.pop(0), num)
            
        return target