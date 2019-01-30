class PrimeNumberOfBits:
    def countPrimeSetBits(self, L, R):
        """
        : # 762, difficulty - EASY
        : didn't say how well I did
        :type L: int
        :type R: int
        :rtype: int
        """
        count = 0
        choices = {2:1,3:1,5:1,7:1,11:1,13:1,17:1,19:1}
        for i in range(L,R+1):
            item = i
            bitcount = 0
            while item>0:
                bitcount+=int(item%2)
                item=int(item/2)
            count+=choices.get(bitcount,0)
        return count