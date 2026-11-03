class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        output = [1] * n
        
        # Bước 1: Duyệt từ trái sang phải để tính tích các số bên trái
        left_product = 1
        for i in range(n):
            output[i] = left_product
            left_product *= nums[i]
            
        # Bước 2: Duyệt ngược từ phải sang trái để tính tích các số bên phải
        # và nhân trực tiếp vào mảng output
        right_product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]
            
        return output