class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        length = 0
        
        # Bỏ qua các khoảng trắng ở cuối chuỗi
        while i >= 0 and s[i] == " ":
            i -= 1
            
        # Đếm các ký tự của từ cuối cùng
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
            
        return length