
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        listA = [-1] * len(arr)
        rmax = -1
        for i in range(len(arr) - 1, -1, -1):
            listA[i] = rmax
            rmax = max(rmax, arr[i])

        return listA
