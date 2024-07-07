class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = {x for x in range(left, right + 1)}
        for start, end in ranges:
            covered -= {x for x in range(start, end + 1)}
        return not covered