class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n <= 0:
            return True

        m = len(flowerbed)
        prev_empty = True  # Coi như sát mép trái luôn trống (tương đương i == 0)

        for i, f in enumerate(flowerbed):
            if f == 1:
                prev_empty = False
                continue

            next_empty = (i == m - 1) or (flowerbed[i + 1] == 0)
            if prev_empty and next_empty:
                n -= 1
                if n == 0:
                    return True
                prev_empty = False  # Vừa trồng hoa tại i nên ô i không còn trống
            else:
                prev_empty = True

        return False