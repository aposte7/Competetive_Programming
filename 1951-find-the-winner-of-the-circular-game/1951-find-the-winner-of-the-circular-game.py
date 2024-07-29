class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        x = [x for x in range(1, n + 1)]

        idx = 0
        for _ in range(n - 1):
            idx = (idx + k - 1) % len(x)
            x.pop(idx)

        return x[0]