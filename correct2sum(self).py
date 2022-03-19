# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 11:30:07 2022

@author: Deepjyoti
"""
"""THIS IS WRONG"""
class Solution:#__init__ takes arguments
    def __init__(self, arr, target):
        # lst = []
        arr_sums = 0
        for i in arr[0:]: #traversing array, first element
            for j in arr[0:]: #traversing the array
                if i != j:
                    arr_sums = i + j #finding all possible 2 sums in array
                # lst.append(arr_sums) #unnecessary
                if arr_sums == target: #if sum == target,show index
                    self.a, self.b = arr.index(j), arr.index(i)                
        # lst = set(lst)
        # print(lst)
    def show(self):
        return (self.a,self.b)
            
arr = [3,2,4]
a=Solution(arr, 6)
print(a.show())
