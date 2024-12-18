class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = [0]
        for i in range(len(nums)):
            self.arr.append(self.arr[i]+nums[i])

    def sumRange(self, left: int, right: int) -> int:
        return self.arr[right+1] - self.arr[left]
        
