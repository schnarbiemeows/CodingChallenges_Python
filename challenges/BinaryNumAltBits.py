class BinaryNumAltBits:
    def hasAlternatingBits(self, n):
        """
        : 693
        : EASY
        : first submission beat 100%
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        init = int(n%2)
        n=n>>1
        while n>0:
            if int(n%2)==init:
                return False
            init=int(n%2)
            n=n>>1
        return True
