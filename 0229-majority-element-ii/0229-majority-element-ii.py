from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        x = Counter(nums)

        l=filter(lambda i:x.get(i) > len(nums) / 3, x)
        return l
        