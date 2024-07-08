class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        mid=num//3
        result=[mid-1,mid,mid+1]
        if sum(result) == num:
            return result
        return []
        