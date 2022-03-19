# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 19:07:03 2022

@author: Deepjyoti
"""
#not proper coz extra memory# given that m+n = length of the nums1
def merge(nums1, m: int, nums2, n: int) -> None:
    nums1 = nums1[:m]+nums2[:n]
    print(sorted(nums1))
# %%    
def merge1(nums1, m: int, nums2, n: int) -> None:
    last = m+n -1 #the last index #m and n here are pointers for us
    while m>0 and n>0: #run loop with condition of m and n
        if nums1[m-1] > nums2[n-1]:#if the last proper value of nums is less than last value in nums2
            nums1[last] = nums1[m-1]#replace the last index of nums1 with last value of nums1
            m -= 1 #decrement m, its for loop
        else:
            nums1[last] = nums2[n-1] # the inverse case
            n -= 1 #moving nums2 array 1 to left, ie moving to next value
        last -= 1 #moving the value of array by 1 to the left
    while n > 0: #if the last value of nums2 > last value of nums1, n remains greater than 0 
        nums1[last] = nums2[n-1] #switch last value of nums2 with last value of nums1
        n, last = n-1, last-1 #decrementing the pointer so that they are zero
            #dont forget pointers
    print(nums1)
nums1 = [2,4,1,0,0,0]
nums2 = [1,5,6]
m=3
n=3
# merge(nums1, m , nums2, n)
merge1(nums1, m , nums2, n)
