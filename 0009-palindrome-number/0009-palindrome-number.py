class Solution:
    def isPalindrome(self, x: int) -> bool:
        m = str(x)
        y = m[::-1]

        return m == y
        