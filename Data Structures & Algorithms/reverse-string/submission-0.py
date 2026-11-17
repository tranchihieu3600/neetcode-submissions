class Solution:
    def reverseString(seft, s: list[str]) -> None:
        left, right = 0, len(s) - 1
    
        while left < right:
            # Swap giá trị thông qua biến tạm
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
        
            # Di chuyển 2 con trỏ vào giữa
            left += 1
            right -= 1