class Solution:
    def isValid(self, s: str) -> bool:
        # Ngăn xếp để lưu các dấu ngoặc mở
        stack = []
        
        # Từ điển lưu các cặp ngoặc tương ứng để đối chiếu nhanh
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            # Nếu là ngoặc đóng (có trong chìa khóa của mapping)
            if char in mapping:
                # Lấy phần tử trên cùng của ngăn xếp ra. Nếu ngăn xếp rỗng thì gán bằng ký tự rác '#'
                top_element = stack.pop() if stack else '#'
                
                # Nếu ngoặc mở trên cùng không khớp với ngoặc đóng hiện tại -> Sai
                if mapping[char] != top_element:
                    return False
            else:
                # Nếu là ngoặc mở, nhét nó vào ngăn xếp
                stack.append(char)
                
        # Cuối cùng, nếu ngăn xếp trống trơn (đã bắt cặp hết) thì đúng, ngược lại là sai
        return not stack