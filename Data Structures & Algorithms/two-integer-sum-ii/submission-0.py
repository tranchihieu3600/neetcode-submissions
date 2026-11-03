class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while (l != r):
            tong = numbers[l] + numbers[r]
            if (tong > target):
                r = r - 1
            elif (tong < target):
                l = l + 1
            else:
                break
        return [l + 1, r + 1]
