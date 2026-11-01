class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Lọc chỉ lấy chữ cái và chữ số, sau đó chuyển thành chữ thường
        clean_s = ""
        for char in s:
            if char.isalnum():
                clean_s += char.lower()
                
        n = len(clean_s)
        i = 0
        
        # Chỉ cần kiểm tra đến một nửa chuỗi là đủ để biết có đối xứng không
        while i < n // 2:
            if clean_s[i] != clean_s[n - i - 1]:
                return False
            i += 1
            
        return True