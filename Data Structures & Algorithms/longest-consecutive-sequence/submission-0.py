class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums.sort()
        max_len = 1
        tam = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue # Bỏ qua các số trùng lặp
            elif nums[i] == nums[i-1] + 1:
                tam += 1 # Tiếp tục chuỗi
            else:
                tam = 1  # Reset biến đếm khi đứt chuỗi
                
            if tam > max_len:
                max_len = tam
                
        return max_len