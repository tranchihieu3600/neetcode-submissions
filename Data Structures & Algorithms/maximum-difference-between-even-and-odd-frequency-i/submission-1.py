class Solution:
    def maxDifference(self, s: str) -> int:
        # Mảng đếm tần số cho 26 chữ cái tiếng Anh
        counts = [0] * 26
        for char in s:
            counts[ord(char) - ord('a')] += 1
            
        max_odd = -1
        min_even = float('inf')
        
        for freq in counts:
            if freq > 0:  # Chỉ xét những ký tự thực sự xuất hiện trong chuỗi
                if freq % 2 == 1:
                    if freq > max_odd:
                        max_odd = freq
                else:
                    if freq < min_even:
                        min_even = freq
                        
        return max_odd - min_even