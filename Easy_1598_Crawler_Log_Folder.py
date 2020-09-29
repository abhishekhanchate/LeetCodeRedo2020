class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for i in range(len(logs)):
            if logs[i] == "../" and count == 0:
                count = count + 0
            elif logs[i] == "../" and count != 0:
                count = count - 1
            elif logs[i] == "./":
                count = count + 0
            else:
                count = count + 1
        return count