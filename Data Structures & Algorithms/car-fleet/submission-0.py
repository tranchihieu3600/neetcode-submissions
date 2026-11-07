class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Ghép cặp (vị trí, tốc độ) và sắp xếp giảm dần theo vị trí (vì đảm bảo xe được xét hiện tại sẽ xuất phát sau xe đã xét)
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = []
        
        for pos, spd in cars:
            # Tính thời gian để xe hiện tại đến đích (dùng phép chia số thực)
            time = (target - pos) / spd
            
            # Nếu ngăn xếp rỗng hoặc xe hiện tại đến đích chậm hơn đoàn xe phía trước
            # thì nó sẽ tạo thành một đoàn xe mới
            if not stack or time > stack[-1]:
                stack.append(time)
                
        # Số lượng phần tử trong ngăn xếp chính là tổng số đoàn xe
        return len(stack)

