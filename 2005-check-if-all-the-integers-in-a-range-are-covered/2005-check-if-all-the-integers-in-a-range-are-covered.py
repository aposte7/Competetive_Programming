class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = set(range(left, right + 1))
        for start, end in ranges:
            covered -= set(range(start, end + 1))
        return not covered