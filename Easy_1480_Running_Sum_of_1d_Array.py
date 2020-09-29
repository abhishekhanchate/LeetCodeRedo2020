# Method 1: 1 additional Array, 1 Int, Runtime 40 ms, Faster than 70.45%, Memory 14.4 MB, Less than 5.04%
# class Solution:
#    def runningSum(self, nums: List[int]) -> List[int]:
#        sum = 0
#        runsum = []
#        for i in range(len(nums)):
#            sum = sum + nums[i]
#            runsum.append(sum)
#        return runsum

# Method 2: 1 Int, Runtime 40 ms, Faster than 70.45%, Memory 14.4 MB, Less than 5.04%
# class Solution:
#    def runningSum(self, nums: List[int]) -> List[int]:
#        sum = 0
#        for i in range(len(nums)):
#            sum = sum + nums[i]
#            nums[i] = sum
#        return nums

# Method 3: No additional, Runtime 36 ms, Faster than 87.58%, Memory 14.3 MB, Less than 5.04%
# class Solution:
#    def runningSum(self, nums: List[int]) -> List[int]:
#        for i in range(1, len(nums)):
#            nums[i] = nums[i] + nums[i-1]
#        return nums

# Method 4: Accumulate Function, Runtime 36 ms, Faster than 87.58%, Memory 14.3 MB, Less than 5.04%
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(accumulate(nums))