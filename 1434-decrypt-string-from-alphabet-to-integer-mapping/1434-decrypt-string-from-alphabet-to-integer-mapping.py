class Solution:
    def freqAlphabets(self, s: str) -> str:
        start = 96
        cons = False
        result =""
        if '#' in s:
            hold = s.split('#')
        else: 
            hold = list(s)
        
        
        k=1
        if(len(hold[-1])==0):
            cons  = True
            k=2

        for i, item in enumerate(hold):
            if len(item) == 1:
                result+=chr(start+int(item))
            elif len(item) == 2 and i != len(hold) - 1:
                result+=chr(start+int(item))
            elif len(item) >= 2:
                result += ''.join(map(lambda x: chr(start + int(x)) , item))
                if i!=len(hold)-1:
                    result=result[:-2] + chr(start+int(item[-2:]))
                
        return result
        
        