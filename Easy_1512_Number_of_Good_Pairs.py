# Method 1: Brute Force: 36 ms, Faster than 51.55%, 14.3 MB, Less than 5.09%
# class Solution:
#    def numIdenticalPairs(self, nums: List[int]) -> int:
#        count = 0
#        for i in range(len(nums)):
#            for j in range(i+1, len(nums)):
#                if nums[i] == nums[j]:
#                    count = count + 1
#        return count

# Method 2:
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        i = 0
        for j in range(i + 1, len(nums)):
            if nums[j] != nums[i]:
                continue
            count = count + 1
            i = j

        return count