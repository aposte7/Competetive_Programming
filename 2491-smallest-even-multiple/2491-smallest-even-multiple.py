class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2 ==0:
            return n
        if n==0:
            return n
        for i in range(1, (2*n)+1):
            if (n*i) % 2 ==0:
                return n*i;
        