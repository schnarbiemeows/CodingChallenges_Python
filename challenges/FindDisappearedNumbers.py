from typing import List

"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.
Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
this one was hard - I exceeded the time limit twice trying to use the commented out code
finally just changed to subtracting one set from the other and casting to a list
Runtime: 168 ms, faster than 58.63% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 23.2 MB, less than 5.39% of Python3 online submissions for Find All Numbers Disappeared in an Array.
"""
class FindDisappearedNumbers:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """

        :param nums:
        :return:
        """
        allNums = set(range(1,len(nums)+1))
        nums = set(nums)
        #for i in nums:
            #if i in allNums:
               # allNums.remove(i)
        return list(allNums-nums)


"""
the easy way would be to convert the list to a set, sort it, then for 1 to N,
if i is not in the set, add it to the answer list
or better, make a set out of 1 to N and a set out of the input list then return 
1 to N list - input list

"""