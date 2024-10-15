class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        i=0
        res=[]
        while i<len(s):
            idx =s.rfind(s[i])
            j =i+1
            while j < idx:
                jdx = s.rfind(s[j])
                if jdx > idx:
                    idx=jdx
                j+=1
            
            res.append(idx+1)
            s=s[idx+1:]
        return res

        