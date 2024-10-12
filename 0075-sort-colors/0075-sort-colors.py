class Solution:

    def sortColors(self, nums: List[int]) -> None:
        zero = 0
        l = len(nums)
        two = l - 1
        
        i = 0
        while i <= two:
            num = nums[i]
            if num == 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
                i += 1
            elif num == 2:
                nums[i], nums[two] = nums[two], nums[i]
                two -= 1
            else:
                i += 1

        return nums
                

                
        """
        Do not return anything, modify nums in-place instead.
        """
        