#find if array exists in the other array (from yt)
#collections is used here
# %%
from collections import Counter

def arrayIntersect(arr1, arr2):
    c = Counter(arr1)#creates a dict with the list of occurences of each value
    output = []
    for i in arr2:
        if c[i]>0:#compare the keys of array2 with array1, obviously if a value exists in array1, then its counter value will > 0
         output.append(i)
         print(c[i])
         c[i] = c[i] - 1#smart way, by making the number of times a value appear as 0,
    return output   #loop never continues

# arr1 = [4,9,5]
# arr2 = [9,4,9,8,4]
# arrayIntersect(arr1, arr2)
# %%
##when the arrarys are sorted
def arrayIntersect1(arr1, arr2):
    output = []
    i,j = 0,0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            i+=1
        elif arr1[i]>arr2[j]:
            j+=1
        else: 
            output.append(arr1[i]) #if neither condition gets satisfied, then obviously the element exists in both arrays
            i+=1 #MUST ADD!!!! goes into unending loop if not added. 
            j+=1
            print(output)
    return output
arr1 = [4,5,9]
arr2 = [1,3,4,5]
arrayIntersect1(arr1, arr2)