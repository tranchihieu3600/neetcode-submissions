from typing import List


class Solution:

    def maxAscendingSum(self, nums: List[int]) -> int:
        tong = nums[0]
        max_sum = nums[0]  # Khởi tạo bằng phần tử đầu tiên thay vì 0

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                tong += nums[i]
            else:
                tong = nums[i]

            if tong > max_sum:
                max_sum = tong

        return max_sum