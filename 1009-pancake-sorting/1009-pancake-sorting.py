class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n= len(arr)
        res =[]
        L = n
        while L > 0:
            idx=arr[:L].index(L) + 1
            if idx!=0:
                res.append(idx)
                arr[:idx] = arr[:idx][::-1]
            arr[:L] = arr[:L][::-1]
            res.append(L)
            L-=1
        return res




        