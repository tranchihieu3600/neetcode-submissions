class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:  # Xử lý trường hợp s rỗng
            return True
            
        ns = len(s)
        nt = len(t)
        i = 0
        j = 0
        
        while i < nt and j < ns:
            if t[i] == s[j]:
                j += 1
            i += 1
            
        return j == ns