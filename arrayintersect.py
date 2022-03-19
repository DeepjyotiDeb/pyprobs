#find if array exists in the other array (made by me)
# %%
# arr1=[4,9,5]
# arr2=[9,4,9,8,4]
arr1= [1]
arr2 = [1]
def arrayIntersect(arr1:int, arr2:int)->int:
    arrdict = dictMake(arr1)
    arrdict1 = dictMake(arr2)
    lst=[]
    if arr1 == arr2: return arr1
    for key in arrdict:
        common= {}
        if (key in arrdict1 and arrdict[key] == arrdict1[key]):
            common[key]=arrdict[key]
            for i in common.items():
                lst = list(i)
            return lst

def dictMake(arr):
    arrdict={}
    for i in arr:
        if arr.index(i)<len(arr)-1:
            arrdict[i] = arr[arr.index(i)+1]
    return arrdict


print(arrayIntersect(arr1, arr2))