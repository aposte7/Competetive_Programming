class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        l = len(nums) - 1
        while i < l:
            if nums[i]==0:
                nums.pop(i)
                nums.append(0)
                l=l-1
            else:
                i = i + 1
            


        """
        Do not return anything, modify nums in-place instead.
        """
        