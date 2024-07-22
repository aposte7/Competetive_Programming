class Solution:
    def freqAlphabets(self, s: str) -> str:
        result =""
        hold = s.split('#')

        for i, item in enumerate(hold):
            if len(item) == 1:
                result += chr(96 + int(item))

            elif len(item) == 2 and i != len(hold) - 1:
                result += chr(96 + int(item))

            elif len(item) >= 2:
                result += ''.join(map(lambda x: chr(96 + int(x)) , item))

                if i != len(hold)-1:
                    result=result[:-2] + chr(96 + int(item[-2:]))
                
        return result
        
        