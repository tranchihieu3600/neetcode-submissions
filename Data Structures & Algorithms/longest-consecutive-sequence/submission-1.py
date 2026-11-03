class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0
        
        for num in num_set:
            # Chỉ bắt đầu đếm khi 'num' là số đầu tiên của một chuỗi
            # (nghĩa là số đứng liền trước nó không tồn tại)
            if (num - 1) not in num_set:
                current_num = num
                current_tam = 1
                
                # Vòng lặp đếm tiếp các số liên sau
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_tam += 1
                    
                if current_tam > max_len:
                    max_len = current_tam
                    
        return max_len