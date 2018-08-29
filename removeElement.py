# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ls = []
        for i in range(len(nums)):
            if nums[i] == val:
                ls.append(i)
        for i in range(len(ls)):
            nums.remove(nums[ls[i] - i])
        return len(nums)
    
removeElement([0,1,2,2,3,0,4,2], 2)