#Brute Force O(n^2) 440 ms, Faster than 27.85%, 14.1 MB, Less than 9.41%  
#class Solution:
#    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

#        ans = []

#        for i in range(len(nums)):
            
#            count = 0
#            target = nums[i]
            
#            for j in range(len(nums)):
#                if target - nums[j] > 0:
#                    count = count + 1
            
#            ans.append(count)

#        return ans

#Binary Search O(n log n) 48 ms, Faster than 96.96%, 14.3 MB, Less than 5.02% O(n)
#import bisect
#class Solution:
#    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#        ans = []
#        sortednums = sorted(nums)
#        for i in range(len(nums)):
#            count = bisect.bisect_left(sortednums, nums[i])
#            ans.append(count)
#        return ans
           
        
#Running Sum 44 ms, Faster than 99.34%, 14.3 MB, Less than 5.02%  
#class Solution:
#    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#        count = [0 for _ in range(101)]
#        for num in nums:
#            count[num] += 1
#            
#        for i in range(1, 101):
#            count[i] += count[i - 1]
#            
#        ans = []
#        
#        for num in nums:
#            if num == 0:
#                ans.append(0)
#            else:
#                ans.append(count[num - 1])
#            
#        return ans

    
#Index of Sorted Array 64 ms, Faster than 72.34%, 14.1 MB, Less than 6.85%
#class Solution:
#    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#        ans = []
#        sortednums = sorted(nums)
#        for num in nums:
#            ans.append(sortednums.index(num))
#        return ans


#Clean Solution 268 ms, Faster than 47.56%, 14.2 MB, Less than 5.02%
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return [sorted(nums).index(num) for num in nums]
