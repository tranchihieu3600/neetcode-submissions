class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # sắp xếp chọn
        n = len (nums)
        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                if nums[min_index] > nums[j]:
                    min_index = j
            temp = nums[i]
            nums[i] = nums[min_index]
            nums[min_index] = temp
                
        return nums