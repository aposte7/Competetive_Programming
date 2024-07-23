import itertools
class Solution:
    def printVertically(self, s: str) -> List[str]:
        if len(s) <= 0:
            return
        hold = s.split(" ")
        max_len = max(len(item) for item in hold)
        result = ["".join(item).rstrip() for item in itertools.zip_longest(*hold,fillvalue=" ")]
        return result

            
