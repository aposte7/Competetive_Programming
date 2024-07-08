class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = []
        done = []
        sum_1 = 0
        for num in nums:
            if num not in done:
                count.append(nums.count(num))
            done.append(num)
        hold =[]
        for item in count:
            sum_1 += sum([x for x in range(item)])
        return sum_1