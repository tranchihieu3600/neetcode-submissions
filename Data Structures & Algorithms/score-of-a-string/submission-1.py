class Solution:
    def scoreOfString(self, s: str) -> int:
        tong = 0
        for i in range(len(s)-1):
           tong += abs( ord(s[i]) - ord(s[i+1]))

        return tong