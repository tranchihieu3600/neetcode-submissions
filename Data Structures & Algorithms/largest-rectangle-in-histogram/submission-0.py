class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)  # Thêm số 0 vào cuối để "vét cạn" stack
        
        for i, h in enumerate(heights):
            # Khi thanh hiện tại (h) thấp hơn thanh ở đỉnh Stack
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]  # Lấy chiều cao của thanh ở đỉnh ra tính toán
                
                # Tính chiều rộng:
                # - Nếu stack trống, nghĩa là thanh này nhỏ nhất từ đầu đến giờ -> rộng = i
                # - Nếu stack còn, biên trái chính là phần tử mới nằm ở đỉnh stack hiện tại
                width = i if not stack else i - stack[-1] - 1
                
                max_area = max(max_area, height * width)
                
            stack.append(i)  # Đưa index hiện tại vào stack
            
        return max_area