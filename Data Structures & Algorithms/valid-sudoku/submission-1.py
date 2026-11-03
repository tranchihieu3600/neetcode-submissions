class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Khởi tạo ma trận 9x9 chứa toàn False
        # Ví dụ: rows[r][num] = True nghĩa là ở hàng r đã xuất hiện số num+1
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                if val == ".":
                    continue
                    
                # Ép kiểu ký tự sang số, và trừ 1 để đưa về index từ 0 đến 8
                # Ví dụ: chữ '5' -> số 4
                num = int(val) - 1 
                
                # Công thức tìm ô 3x3 như cũ
                box_index = (r // 3) * 3 + (c // 3)
                
                # Kiểm tra xem ô cờ tương ứng đã bị bật thành True chưa
                if rows[r][num] or cols[c][num] or boxes[box_index][num]:
                    return False
                    
                # Nếu chưa, bật cờ (đánh dấu) thành True
                rows[r][num] = True
                cols[c][num] = True
                boxes[box_index][num] = True
                
        return True