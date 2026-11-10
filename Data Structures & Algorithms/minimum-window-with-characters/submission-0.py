from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        # Đếm tần suất các ký tự cần có trong t
        dict_t = Counter(t)
        required = len(dict_t)  # Số ký tự duy nhất cần thỏa mãn số lượng
        
        # Biến đếm số ký tự duy nhất trong cửa sổ đạt đủ số lượng yêu cầu
        formed = 0
        window_counts = {}
        
        # Lưu trữ kết quả: (độ dài, left, right)
        ans = float("inf"), None, None
        
        l, r = 0, 0
        while r < len(s):
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1
            
            # Nếu tần suất của ký tự hiện tại đạt đúng yêu cầu của t, tăng `formed` lên 1
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
                
            # Khi cửa sổ đã đủ tất cả các ký tự yêu cầu, tiến hành thu hẹp từ bên trái
            while l <= r and formed == required:
                character = s[l]
                
                # Cập nhật kết quả nếu tìm được cửa sổ nhỏ hơn
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                    
                # Loại bỏ ký tự ở bên trái ra khỏi cửa sổ
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                    
                l += 1
            
            r += 1
            
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]