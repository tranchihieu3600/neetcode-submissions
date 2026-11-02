
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        # Bước 1: Đếm số lần xuất hiện của từng số
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        # Bước 2: Tạo danh sách lưu các số theo tần suất
        # freq = [[] for _ in range(len(nums) + 1)]

        # Tạo danh sách freq
        freq = []

        # Tạo len(nums) + 1 danh sách rỗng bên trong
        for i in range(len(nums) + 1):
            freq.append([])

        # Bước 3: Đưa mỗi số vào vị trí tương ứng với số lần xuất hiện
        for num in count:
            frequency = count[num]
            freq[frequency].append(num)

        # Bước 4: Lấy ra K phần tử xuất hiện nhiều nhất
        result = []

        for frequency in range(len(freq) - 1, 0, -1):

            for num in freq[frequency]:
                result.append(num)

                if len(result) == k:
                    return result

        return result
