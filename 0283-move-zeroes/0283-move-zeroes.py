class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        z = 0
        for i in range(0,len(nums)):
            if nums[z]==0 and nums[i]!=0:
                nums[z],nums[i] = nums[i],  nums[z]
                z+=1
            if nums[z]!=0:
                z+=1
        return nums
            
        


        """
        Do not return anything, modify nums in-place instead.
        """
        