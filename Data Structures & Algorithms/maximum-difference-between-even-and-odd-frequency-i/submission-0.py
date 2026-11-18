from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        # Đếm tần số xuất hiện của từng ký tự
        count = Counter(s)
        
        # Tìm tần số lẻ lớn nhất và tần số chẵn nhỏ nhất
        max_odd = max((freq for freq in count.values() if freq % 2 == 1), default=0)
        min_even = min((freq for freq in count.values() if freq % 2 == 0), default=len(s))
        
        return max_odd - min_even