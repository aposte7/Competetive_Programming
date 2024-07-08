class Solution:
    def romanToInt(self, s: str) -> int:
        code ={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        result=0
        for x in range(len(s)):
            if x!=len(s)-1 and code[s[x]] < code[s[x+1]]:
                result-=code[s[x]]
            else:
                result+=code[s[x]]
        return result