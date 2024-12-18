class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for index,value in enumerate(nums):
            if index==0:
                continue
            nums[index] = nums[index] + nums[index
            -1]
        return nums
        