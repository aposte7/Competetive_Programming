class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        m = max(arr1)
        l = len(arr1)
        l2 = len(arr2)
        count =  [0]* (m+1)
        res =[-1]*l
        for i in range(l):
            count[arr1[i]]+=1
        x=0

        for num in arr2:
            while count[num] > 0:
                res[x] = num
                count[num] -= 1
                x += 1

        for i in range(len(count)):
            while count[i] > 0:
                res[x] = i
                count[i] -= 1
                x += 1
        return res
        
        