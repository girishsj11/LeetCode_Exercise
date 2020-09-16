# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 21:46:55 2020

@author: giri
"""

def findMedianSortedArrays(nums1, nums2):
    nums1.extend(nums2)
    nums1.sort()
    length = len(nums1)
        
    if(length%2==0):
        index = length//2
        return ((nums1[index]+nums1[index-1])/2)
    else:
        return nums1[length//2]
    
    
    
print(findMedianSortedArrays([1,3],[2]))
print()
print(findMedianSortedArrays([1,2], [3,4]))
print()
print(findMedianSortedArrays([0,0], [0,0]))
print()
print(findMedianSortedArrays([2],[]))
