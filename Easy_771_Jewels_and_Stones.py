# Method 1: Brute Force: 32ms, 14.2 MB
# class Solution:
#    def numJewelsInStones(self, J: str, S: str) -> int:
#        count = 0
#        for i in range(len(S)):
#            for j in range(len(J)):
#                if S[i] == J[j]:
#                    count = count + 1
#        return count

# Method 2: 24 ms, Faster than 93.78%, 14.2 MB, Less than 5.20%
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for i in range(len(S)):
            if S[i] in J:
                count = count + 1
        return count