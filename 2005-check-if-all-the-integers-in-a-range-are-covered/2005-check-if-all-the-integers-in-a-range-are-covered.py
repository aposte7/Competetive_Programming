class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        set_1={x for x in range(left,right+1)}
        set_2=set()
        for start,end in ranges:
            set_2 |= {x for x in range(start,end+1)}
            
        return not set_1 - set_2