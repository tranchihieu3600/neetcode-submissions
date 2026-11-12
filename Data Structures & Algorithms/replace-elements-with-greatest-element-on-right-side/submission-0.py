
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        listA = [-1] * len(arr)

        for i in range(len(arr) - 1):
            max = -1

            for j in range(i + 1, len(arr)):
                if max < arr[j]:
                    max = arr[j]

            listA[i] = max

        return listA
