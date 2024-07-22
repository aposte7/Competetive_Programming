class Solution:
    def printVertically(self, s: str) -> List[str]:
        if len(s) <= 0:
            return
        hold = s.split(" ")
        max_len = max(len(item) for item in hold)
        for i, item in enumerate(hold):
            if len(item) < max_len:
                value = item + (" " * (max_len - len(item)))
                hold[i] = value
    
        result = ["".join(item) for item in zip(*hold)]
        
        for i, item in enumerate(result):
            result[i] = item.rstrip()
        return result

            
