class Solution:
    def average(self, salary: List[int]) -> float:
        x =sorted(salary)
        return (sum(x) - x[0] - x[-1]) / (len(x) - 2)
        