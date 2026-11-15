class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Bước 1: Tạo hash map để lưu ánh xạ từ node gốc sang node bản sao
        old_to_new = {}
        
        # Lần duyệt 1: Tạo tất cả các bản sao node (chưa gán next/random)
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
            
        # Lần duyệt 2: Gán con trỏ next và random dựa vào hash map
        curr = head
        while curr:
            if curr.next:
                old_to_new[curr].next = old_to_new[curr.next]
            if curr.random:
                old_to_new[curr].random = old_to_new[curr.random]
            curr = curr.next
            
        # Trả về nút đầu tiên của danh sách mới
        return old_to_new[head]