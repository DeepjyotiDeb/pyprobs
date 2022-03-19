# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 19:17:01 2022

@author: Deepjyoti
"""
#following kadane's approach to solve the problem
#WE ARE ONLY RETURNING THE MAXIMUM SUM, NOT SUBARRAY HERE
def maxSub(arr:int)->int:
    current_sum = max_sum = arr[0] #set the max and current value
    for i in arr[1:]: #looping thru array
        # print(i) #adding the num to the current sum
        current_sum += i 
        if current_sum<i: #if the value at index is greater than current_sum
            current_sum=i #change current sum to value at index(i)
        if max_sum<current_sum: #max sum set at beginning
            max_sum=current_sum #if currentsum > maxsum, 
    # print(max_sum) #switch maxsum to currentsum
    return max_sum

arr = [1,-2,3,5]
print(maxSub(arr))