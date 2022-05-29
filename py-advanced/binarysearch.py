#%%
def bst(arr, t):
    low = 0
    high = len(arr) - 1
    mid = 0 
    while low<=high:
        mid = (high+low)//2
        if arr[mid] < t: #ignore left half if t is greater
            low = mid+1
        elif arr[mid] > t:#ignore right half if t is greater
            high = mid -1 
        else:
            return mid
        
    
arr = [-1,0,3,6,9,11,12]
t = 9
bst(arr, t)