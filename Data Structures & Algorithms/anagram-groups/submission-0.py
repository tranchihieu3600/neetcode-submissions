from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary lưu các nhóm, với value mặc định là một list
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Khởi tạo mảng đếm 26 phần tử cho 26 chữ cái tiếng Anh
            count = [0] * 26
            
            for char in s:
                # Tính khoảng cách từ ký tự hiện tại đến 'a' để xác định vị trí (0-25)
                count[ord(char) - ord('a')] += 1
            
            # Tuple là kiểu dữ liệu bất biến (immutable) nên có thể dùng làm key cho Hash Map
            # Các từ là anagram của nhau sẽ tạo ra cùng một tuple count giống hệt nhau
            anagram_map[tuple(count)].append(s)
            
        # Trả về danh sách các nhóm anagram
        return list(anagram_map.values())