class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rmax = -1
        for i in range(len(arr) - 1, -1, -1):
            # Lưu lại giá trị hiện tại trước khi nó bị đè bởi rmax
            temp = arr[i] 
            arr[i] = rmax
            rmax = max(rmax, temp)
        return arr