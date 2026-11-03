class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        target = []
        nums.sort()

        i = 0
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    target.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif total < 0:
                    j += 1
                else:
                    k -= 1

            i += 1

            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1

        return target