class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        mid=num//3
        result=[]
        result.append(mid-1)
        result.append(mid)
        result.append(mid+1)
        if sum(result) == num:
            return result
        return []
        