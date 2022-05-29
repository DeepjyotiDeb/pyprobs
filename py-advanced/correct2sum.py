# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 12:22:42 2022

@author: Deepjyoti
"""
#Return indices that add upto a number
def twoSum(arr, target):
    for i in range(len(arr)-1): #why avoid the last element? duplicate comes?
        for j in range(i+1, len(arr)): #avoid having same index
            if arr[i] + arr[j] == target:
                print(arr[i], arr[j], i , j)
#1. using enumerate to create a dict. key is the index and value is the array value
#2. remember switching values without using an extra variable? something like that is applied below
def twoSum1(arr, target):
    seen = {}
    nums = arr
    for i, num in enumerate(nums):#i is the index
        if target - num in seen: #if 2, which is 6-4 is in dict seen
            return ([seen[target-num], i])#i is the index, & the index of value from seen
        # print (i, num)
        elif num not in seen:
            seen[num]=i #adding to the dict(<dict_name>[key]= value)

arr = [1,4,3,6,5]
# twoSum(arr, 6)

print(twoSum1(arr, 6))