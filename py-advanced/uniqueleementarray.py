# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 11:21:23 2022

@author: Deepjyoti
"""
#checking if the element exists in the array or not
def containsDuplicate(arr):
        arrset = set()#create empty set
        print(arrset)
        for i in arr: #traversing through elements in set
            if i in arrset: #if element is in set
                print(True) #return true
                return True
            arrset.add(i)# if not in set, add the number to the set
        print(False)
        return False
    
a=[1,2,3,4,1]
containsDuplicate(a)