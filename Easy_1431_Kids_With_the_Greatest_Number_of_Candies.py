class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = max(candies)
        ans = []
        for i in range(len(candies)):
            candies[i] = extraCandies + candies[i]
            if candies[i] >= maxi:
                ans.append(1)
            else:
                ans.append(0)

        return ans
