class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            # Nếu khớp ký tự, dịch chuyển con trỏ của s lên
            if s[i] == t[j]:
                i += 1
            # Con trỏ của t luôn luôn dịch chuyển sau mỗi bước
            j += 1
            
        # Nếu i chạy hết chiều dài của s tức là tìm thấy đủ chuỗi con
        return i == len(s)