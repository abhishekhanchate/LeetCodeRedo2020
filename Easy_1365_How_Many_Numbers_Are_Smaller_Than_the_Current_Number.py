# Brute Force 440 ms, Faster than 27.85%, 14.1 MB, Less than 9.41%
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        ans = []

        for i in range(len(nums)):

            count = 0
            target = nums[i]

            for j in range(len(nums)):
                if target - nums[j] > 0:
                    count = count + 1

            ans.append(count)

        return ans

