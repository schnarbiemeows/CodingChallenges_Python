class LargestPerimeter:
    def largestPerimeter(self, A):
        """
        : 976
        : ha! beat 99.08%
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        k = len(A)-1
        while k>1 and A[k]>=(A[k-1]+A[k-2]):
            k-=1
        if k==1:
            return 0
        return A[k]+A[k-1]+A[k-2]
