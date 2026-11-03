class Solution:
    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            # Gắn độ dài và ký tự '#' vào trước mỗi chuỗi
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        res, i = [], 0
        
        while i < len(s):
            j = i
            # Tìm vị trí của dấu '#' tiếp theo
            while s[j] != '#':
                j += 1
                
            # Lấy ra chiều dài của chuỗi
            length = int(s[i:j])
            
            # Cắt chuỗi dựa trên chiều dài đã biết
            # s[j+1 : j+1+length] chính là nội dung chuỗi
            res.append(s[j + 1 : j + 1 + length])
            
            # Cập nhật con trỏ i để nhảy đến chuỗi tiếp theo
            i = j + 1 + length
            
        return res