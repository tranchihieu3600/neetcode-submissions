class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        dientichmax = 0
        while (l != r):
            maxl = heights[l]
            maxr = heights[r]
            dientich = (r - l) * min(heights[l], heights[r])
            if dientich > dientichmax:
                dientichmax = dientich
            
            if (maxl <= maxr):
                l += 1
            else: 
                r -= 1    
        return dientichmax