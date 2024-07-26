class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, itm in enumerate(nums):
            complement = target - itm
            if complement in nums[idx+1:]:
                return [idx, nums.index(complement, idx+1, len(nums))]
        return []
