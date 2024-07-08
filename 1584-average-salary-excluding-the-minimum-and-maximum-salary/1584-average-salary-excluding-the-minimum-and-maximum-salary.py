class Solution:
    def average(self, salary: List[int]) -> float:
        x =sorted(salary)
        x = x[ 1:-1]
        return sum(x)/len(x)