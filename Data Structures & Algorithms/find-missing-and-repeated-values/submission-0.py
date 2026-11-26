class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N = len(grid)
        seen = set()
        double = missing = 0

        for i in range(N):
            for j in range(N):
                if grid[i][j] in seen:
                    double = grid[i][j]
                seen.add(grid[i][j])

        for num in range(1, N * N + 1):
            if num not in seen:
                missing = num
                break

        return [double, missing]