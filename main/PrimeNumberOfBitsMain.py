from challenges.PrimeNumberOfBits import *
# 762
# difficulty - EASY
# Given two integers L and R, find the count of numbers
# in the range [L, R] (inclusive) having a prime number of set bits in their binary representation.
if __name__ == '__main__':
    L = 10
    R = 15
    sol = PrimeNumberOfBits()
    answer = sol.countPrimeSetBits(L,R)
    print(str(answer))