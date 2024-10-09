class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_zeros = [0] * (n + 1)
        right_ones = [0] * (n + 1)
        
        # Calculate prefix sums for zeros on the left
        for i in range(1, n + 1):
            left_zeros[i] = left_zeros[i - 1] + (1 if nums[i - 1] == 0 else 0)
        
        # Calculate prefix sums for ones on the right
        for i in range(n - 1, -1, -1):
            right_ones[i] = right_ones[i + 1] + (1 if nums[i] == 1 else 0)
        
        max_score = 0
        res = []
        
        # Calculate the maximum score and collect indices
        for i in range(n + 1):
            division_score = left_zeros[i] + right_ones[i]
            if division_score > max_score:
                max_score = division_score
                res = [i]
            elif division_score == max_score:
                res.append(i)
        
        return res
