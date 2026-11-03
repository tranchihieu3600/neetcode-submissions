class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)

        prefix = [0] * n
        suffix = [0] * n

        # Tìm giá trị lớn nhất bên trái
        prefix[0] = height[0]

        for i in range(1, n):
            prefix[i] = max(prefix[i - 1], height[i])

        # Tìm giá trị lớn nhất bên phải
        suffix[n - 1] = height[n - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = max(suffix[i + 1], height[i])

        # Tính tổng lượng nước
        water = 0

        for i in range(n):
            water += min(prefix[i], suffix[i]) - height[i]

        return water