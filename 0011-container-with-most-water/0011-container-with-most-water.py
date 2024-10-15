class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        area = 0
        h,w=0,0
        while l < r:
            area =max(min(height[l], height[r]) * (r - l), area)
            if height[l] > height[r]:
                r-=1
            else:
                l+=1
        return area



        