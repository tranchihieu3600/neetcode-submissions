class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count = 1
                for j in range (i + 1, len(nums)):
                    if nums[j] == 1:
                        count += 1
                    else: 
                        break
                if count > max:
                    max = count
        return max