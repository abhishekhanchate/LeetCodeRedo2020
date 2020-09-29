# Brute Force O[n2]
# class Solution:
#    def twoSum(self, nums: List[int], target: int) -> List[int]:
#        for i in range(len(nums)):
#            for j in range(i+1, len(nums)):
#                if nums[i] + nums[j] == target:
#                    return [i, j]

# Dictionary Method O[n]
class Solution:
    def twoSum(self, nums: [], target: int):
        dict = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in dict.keys():
                indextwo = nums.index(complement)
                if (i != indextwo):
                    return sorted([i, indextwo])

            dict.update({nums[i]: i})
