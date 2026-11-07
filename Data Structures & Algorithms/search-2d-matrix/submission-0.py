class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        m = len(matrix)       # số hàng
        n = len(matrix[0])    # số cột
        
        # Đặt con trỏ tìm kiếm nhị phân cho mảng 1D ảo
        left = 0
        right = m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Chuyển đổi chỉ số 1D sang tọa độ 2D
            row = mid // n
            col = mid % n
            mid_value = matrix[row][col]
            
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False