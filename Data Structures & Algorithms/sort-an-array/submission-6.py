import random
from typing import List


class Solution:
    def sortArray(
        self, nums: List[int], low: int = 0, high: int | None = None
    ) -> List[int]:
        if high is None:
            high = len(nums) - 1

        if low < high:
            # Chọn pivot ngẫu nhiên để tránh trường hợp xấu nhất O(n^2)
            rand_idx = random.randint(low, high)
            nums[rand_idx], nums[high] = nums[high], nums[rand_idx]

            pivot = nums[high]
            store_idx = low

            for j in range(low, high):
                if nums[j] <= pivot:
                    nums[store_idx], nums[j] = nums[j], nums[store_idx]
                    store_idx += 1

            nums[store_idx], nums[high] = nums[high], nums[store_idx]

            self.sortArray(nums, low, store_idx - 1)
            self.sortArray(nums, store_idx + 1, high)

        return nums