# String as a Character Array: 48 ms, Faster than 95.47%, 14 MB, Less than 11.18%
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = list(s)

        for i in range(len(s)):
            arr[indices[i]] = s[i]

        return "".join(arr)