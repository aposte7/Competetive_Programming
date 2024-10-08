class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        length  = len(nums)
        z =0
        for i in range(len(nums)-1):
            if(nums[i]==nums[i+1]):
                nums[i] =  nums[i]*2
                nums[i+1] = 0
            if(nums[i]!=0 and nums[z]==0):
                nums[z], nums[i] = nums[i], nums[z]
                z+=1
            if nums[z]!=0:
                z+=1
        if(nums[len(nums)-1]!=0 and nums[z]==0):
                nums[z], nums[len(nums)-1] = nums[len(nums)-1], nums[z]
                z+=1
        
        return nums
        
        