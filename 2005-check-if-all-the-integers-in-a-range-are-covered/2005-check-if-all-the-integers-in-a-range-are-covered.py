class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort(key=lambda x: x[0])
        left_1 = min(ranges, key=lambda x: x[0])[0]
        right_1 = max(ranges, key=lambda x: x[1])[1]
        print(ranges)
        for i in range(0, len(ranges)):
            if ranges[i][1] < left:
                continue
            if ranges[i][0] > left:
                return False
            if ranges[i][1] >= right:
                return True    
            left = ranges[i][1] + 1

        if not ((left_1 <= left) and (right_1 >= right)):
            return False