class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        tong = 0
        for i in range(n-1):
           tong += abs( ord(s[i]) - ord(s[i+1]))

        return tong