class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        x = [0] * len(nums)  
        
        for i in range(len(nums)):
            x[(i + k) % len(nums)] = nums[i]
        
        for i in range(len(nums)):
            nums[i] = x[i]
    