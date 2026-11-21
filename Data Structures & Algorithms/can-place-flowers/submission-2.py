class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        i = 0

        while i < len(flowerbed):
            if flowerbed[i] == 0:
                if (i == 0 or flowerbed[i-1] == 0) and \
                   (i == len(flowerbed)-1 or flowerbed[i+1] == 0):

                    count += 1
                    flowerbed[i] = 1

            i += 1
        
        if count>= n:
            return True
        return False