class NumOfOneBits:

    def Solution(self, num):
        """
        : beats 100%
        :type n: int
        :rtype: int
        """
        n = 0
        while num:
            num &= num - 1
            n += 1
        return n
