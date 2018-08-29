# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 21:41:48 2018

@author: RAHUL MISHRA
"""
#Given an array with n objects colored red, white or blue, sort them in-place
#so that objects of the same color are adjacent, with the colors in the order 
#red, white and blue.

def sortColors(nums):
    count = 0
    while count < len(nums):
        for i in range(len(nums)):
            if nums[count] < nums[i]:
                nums[count], nums[i] = nums[i], nums[count]
        count += 1
    return nums
    
    
    
    
#Input: [2,0,2,1,1,0]
#Output: [0,0,1,1,2,2]