class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = cnt = 0
        for num in nums:
            if num == 1:
                cnt += 1
            else: 
                cnt = 0
            res = max(res, cnt)
        return res