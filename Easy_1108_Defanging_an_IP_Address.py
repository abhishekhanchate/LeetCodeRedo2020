class Solution:
    def defangIPaddr(self, address: str) -> str:
        print(type(address))
        ans = address.replace(".", "[.]")
        return ans