class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        for a in range(int(c**0.5) +1):
            b_squared = c - a**2
            if b_squared >= 0:
                b = int(b_squared**0.5)
                if b**2 == b_squared:
                    return True
        return False