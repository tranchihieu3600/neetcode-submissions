class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setA = set(nums)
        listA = list(setA)
        if len(listA) == len(nums):
            return False
        else:
            return True