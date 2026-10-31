class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Dictionary lưu trữ dạng {số_từng_duyệt: index_của_số_đó}
        dic = {}
        for i in range(len(nums)):
            hieu = target - nums[i]

            if hieu in dic:
                return [dic[hieu], i]

            dic[nums[i]] = i
        return []