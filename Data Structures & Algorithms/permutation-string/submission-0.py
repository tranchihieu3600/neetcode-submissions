class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Dictionary lưu tần suất của chuỗi mẫu s1
        s1_count = {}
        for char in s1:
            s1_count[char] = 1 + s1_count.get(char, 0)
            
        window_count = {} # Dictionary lưu tần suất của cửa sổ trượt
        
        # required: Số lượng ký tự ĐỘC LẬP cần phải khớp. 
        # (VD: s1 = "aab" thì required = 2 vì chỉ có 'a' và 'b')
        required = len(s1_count) 
        formed = 0 # Số lượng ký tự đã đạt đủ tần suất yêu cầu
        
        l = 0
        for r in range(len(s2)):
            # 1. THÊM KÝ TỰ BÊN PHẢI VÀO CỬA SỔ
            char_in = s2[r]
            window_count[char_in] = 1 + window_count.get(char_in, 0)
            
            # Nếu ký tự này có trong s1 và số lượng vừa đạt mức hoàn hảo -> tăng formed
            if char_in in s1_count and window_count[char_in] == s1_count[char_in]:
                formed += 1
                
            # 2. RÚT GỌN CỬA SỔ NẾU NÓ BỊ PHÌNH TO QUÁ CHIỀU DÀI S1
            if r - l + 1 > len(s1):
                char_out = s2[l]
                
                # Nếu ký tự bị nhả ra đang ở mức hoàn hảo -> làm hỏng sự hoàn hảo -> giảm formed
                if char_out in s1_count and window_count[char_out] == s1_count[char_out]:
                    formed -= 1
                    
                window_count[char_out] -= 1
                
                # Dọn dẹp rác: nếu số lượng về 0 thì xóa hẳn khỏi dictionary cho nhẹ
                if window_count[char_out] == 0:
                    del window_count[char_out]
                    
                l += 1 # Đẩy mép trái lên
                
            # 3. KIỂM TRA ĐIỀU KIỆN THẮNG
            if formed == required:
                return True
                
        return False