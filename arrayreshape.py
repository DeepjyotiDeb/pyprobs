# %%
# by self #numpy takes too much
import numpy as np

def shaper(arr, r, c):
    ar = np.array(arr)
    if r*c == ar.size:
        ar = ar.reshape(r,c)
    else:
        return arr
    return ar

arr = [[1,2], [3,4]]
r = 2
c = 2
shaper(arr, r, c)
#%% 
def reshape(arr, r, c):
    count = 0
    for i in arr: #only counts the number of items in nested list
        count = count+len(i)
    lst = []
    for i in range(len(arr)):
        for j in arr[i]:
            lst.append(j)
    if r*c != count: return arr 

    ind = 0
    res = []
    for i in range(r):
        res.append([])
        for j in range(c):
            # print(lst[ind])
            res[i].append(lst[ind])
            ind+=1
    return res
arr = [[1,2,4],[3,4,5]]
r=3
c=2
reshape(arr,r,c)
