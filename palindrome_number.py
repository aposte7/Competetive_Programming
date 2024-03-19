class Solution:
    def isPalindrome(self, x: int) -> bool:
        hold = 0
        y = x
        if x < 0:
            x = x * -1
        while x != 0:
            hold = hold * 10 + (x % 10)
            x = x // 10

        if hold == y:
            return True

        return False
