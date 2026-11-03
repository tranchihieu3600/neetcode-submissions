import collections

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Tạo các Set để lưu trữ các số đã xuất hiện
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key sẽ là toạ độ (r//3, c//3)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Bỏ qua nếu là ô trống
                if val == ".":
                    continue
                
                # Nếu số này đã tồn tại trong hàng, cột, hoặc ô 3x3 tương ứng -> Sai luật
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in squares[(r // 3, c // 3)]):
                    return False
                
                # Nếu chưa có, thêm số này vào Set để đánh dấu là đã gặp
                rows[r].add(val)
                cols[c].add(val)
                squares[(r // 3, c // 3)].add(val)

        return True