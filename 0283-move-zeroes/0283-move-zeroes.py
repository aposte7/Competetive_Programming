class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        right = 1
        n = len(nums)
        while left < n and right < n:
            if nums[left]!=0:
                left+=1
            elif nums[right]==0:
                right+=1
            else:
                if right > left:
                    nums[left],nums[right] = nums[right], nums[left]
                    left+=1
                    right+=1
                else:
                    right+=1
        return nums



            
        

        