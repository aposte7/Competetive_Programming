class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        sqr = 1
        com =[]
        while n > 0:
            sqr = sqr * 3
            if n < sqr:
                print(sqr)
                sqr /= 3
                if sqr in com:
                    return False
                com.append(sqr)
                n -= sqr
                sqr = 1
        if n == 0 or n ==-1:
            return True
        return False