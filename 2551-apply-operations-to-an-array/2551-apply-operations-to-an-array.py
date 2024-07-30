class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        length  = len(nums)
        for i in range(len(nums)-1):
            if(nums[i]==nums[i+1]):
                nums[i] =  nums[i]*2
                nums[i+1] = 0
          
        y = [x for x in nums if x != 0]
        y = y + [0] * (length-len(y))
        return y
        
        