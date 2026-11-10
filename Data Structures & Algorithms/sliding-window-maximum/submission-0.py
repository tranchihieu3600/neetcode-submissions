from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()  # Lưu các index, giữ giá trị giảm dần từ trái sang phải
        res = []
        
        for i, num in enumerate(nums):
            # 1. Loại bỏ các index đã trôi qua (nằm ngoài cửa sổ kích thước k)
            if dq and dq[0] <= i - k:
                dq.popleft()
                
            # 2. Loại bỏ các phần tử ở cuối nhỏ hơn phần tử hiện tại (vì chúng vô dụng)
            while dq and nums[dq[-1]] < num:
                dq.pop()
                
            # 3. Đưa index hiện tại vào cuối hàng đợi
            dq.append(i)
            
            # 4. Khi cửa sổ đã đủ kích thước k, bắt đầu ghi nhận kết quả
            if i >= k - 1:
                res.append(nums[dq[0]])
                
        return res