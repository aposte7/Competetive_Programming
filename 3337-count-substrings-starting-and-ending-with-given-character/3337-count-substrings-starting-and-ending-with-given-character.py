class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        count_c = 0
        total = 0

        for char in s:
            if char == c:
                count_c += 1
                total += count_c

        return total
