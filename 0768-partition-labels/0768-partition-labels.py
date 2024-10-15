class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res=[]
        lastindex={}
        for i,item in enumerate(s):
            lastindex[item]=i
        sum=0
        j=0
        end = 0
        while j < len(s):
            sum+=1
            lst = lastindex[s[j]]
            end = max(end,lst)
            if j==end:
                res.append(sum)
                sum=0
            j+=1
        return res

        