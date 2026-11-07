class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = [] # Dùng để lưu chỉ số (index) của các ngày chưa tìm được ngày ấm hơn

        for i, temp in enumerate(temperatures):
            # Nếu stack không rỗng và nhiệt độ hiện tại cao hơn nhiệt độ của ngày ở đỉnh stack
            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index # Tính số ngày chờ
            
            # Đưa chỉ số ngày hiện tại vào stack để tiếp tục chờ ngày ấm hơn
            stack.append(i)

        return res