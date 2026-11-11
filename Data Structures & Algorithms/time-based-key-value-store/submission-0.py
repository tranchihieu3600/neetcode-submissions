class TimeMap:

    def __init__(self):
        # Khởi tạo một dictionary để lưu trữ:
        # Key: Chuỗi khóa (key)
        # Value: Danh sách các tuple dạng (timestamp, value) được sắp xếp theo thời gian tăng dần
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        # Thêm cặp (timestamp, value) vào danh sách tương ứng của key
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # Nếu khóa không tồn tại, trả về chuỗi rỗng
        if key not in self.store:
            return ""

        values = self.store[key]
        left, right = 0, len(values) - 1
        res = ""

        # Sử dụng Binary Search để tìm mốc thời gian lớn nhất <= timestamp
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]  # Lưu lại giá trị tạm thời thỏa mãn điều kiện
                left = (
                    mid + 1
                )  # Tiếp tục tìm kiếm sang bên phải để xem có timestamp nào lớn hơn nữa không
            else:
                right = mid - 1  # Timestamp lớn hơn yêu cầu, thu hẹp khoảng tìm kiếm về bên trái

        return res

