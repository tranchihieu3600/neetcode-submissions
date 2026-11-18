class Node:
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Lưu trữ key -> Node
        
        # Khởi tạo dummy head và tail để dễ quản lý thêm/xóa ở 2 đầu
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """Hàm phụ trợ: Xóa một node ra khỏi danh sách liên kết đôi"""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self, node: Node):
        """Hàm phụ trợ: Thêm một node vào ngay sau head (mới sử dụng gần đây nhất)"""
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Đưa node vừa truy cập lên đầu danh sách
            self._remove(node)
            self._add_to_head(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            # Cập nhật lại vị trí: đưa lên đầu danh sách
            self._remove(node)
            self._add_to_head(node)
        else:
            if len(self.cache) >= self.capacity:
                # Xóa phần tử ít sử dụng nhất (nằm ở ngay trước tail)
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
            
            # Tạo node mới và thêm vào đầu danh sách
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)