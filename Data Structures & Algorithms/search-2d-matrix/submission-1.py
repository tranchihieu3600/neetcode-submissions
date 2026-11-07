class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        m, n = len(matrix), len(matrix[0])
        
        # Bước 1: Tìm kiếm nhị phân trên các hàng (dựa vào cột đầu và cột cuối)
        top = 0
        bottom = m - 1
        
        while top <= bottom:
            row = (top + bottom) // 2
            
            # Nếu target lớn hơn phần tử cuối cùng của hàng giữa, nó phải nằm ở các hàng dưới
            if target > matrix[row][-1]:
                top = row + 1
            # Nếu target nhỏ hơn phần tử đầu tiên của hàng giữa, nó phải nằm ở các hàng trên
            elif target < matrix[row][0]:
                bottom = row - 1
            # Nếu nằm trong khoảng của hàng này, ta đã tìm đúng hàng
            else:
                break
                
        # Nếu top vượt qua bottom, nghĩa là target không thuộc bất kỳ hàng nào
        if top > bottom:
            return False
            
        # Bước 2: Tìm kiếm nhị phân tiêu chuẩn trên hàng mục tiêu đã xác định
        target_row = (top + bottom) // 2
        left = 0
        right = n - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if matrix[target_row][mid] == target:
                return True
            elif matrix[target_row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False