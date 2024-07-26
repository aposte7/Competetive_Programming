from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        x = Counter(nums)
        return [i for i in x.keys() if x.get(i) > len(nums)/3]
        