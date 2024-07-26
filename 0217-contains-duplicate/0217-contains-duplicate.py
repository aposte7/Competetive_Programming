class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        original_num =len(nums)
        check = len(set(nums))
        return original_num > check