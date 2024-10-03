class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index_1, item in enumerate(nums):
            x = target - item
            try:
                index_2 = nums.index(x, index_1 + 1)
            except ValueError:
                continue 
            if index_2:
                return [index_1, index_2]
        return []