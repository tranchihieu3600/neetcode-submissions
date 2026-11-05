class MinStack:
    def __init__(self):
        # Khởi tạo ngăn xếp. Mỗi phần tử sẽ là một tuple: (val, current_min)
        self.stack = []

    def push(self, val: int) -> None:
        # Nếu ngăn xếp rỗng, giá trị nhỏ nhất chính là val
        if not self.stack:
            self.stack.append((val, val))
        else:
            # Lấy ra giá trị nhỏ nhất hiện tại ở trên cùng của ngăn xếp
            current_min = self.stack[-1][1]
            # Đẩy val mới vào, kèm theo giá trị nhỏ nhất được cập nhật
            self.stack.append((val, min(val, current_min)))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0] # Lấy giá_trị_thực_tế

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1] # Lấy giá_trị_nhỏ_nhất_tính_đến_hiện_tại