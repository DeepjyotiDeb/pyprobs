# brute force method, causes issues if array is unsorted. sorting recommended
# %%
def split( arr:int, lst:'list'=[]) -> int: #function annotation--> declare the type[int, string] inside the parentheses
    b= sum(arr)                            #outside parenthses, shown using ->. 
    lst = []                               #annotation is used for the user. Interpreter does not care
    print(b)
    for i in arr:
        if sum(lst) != b/2:
            lst.append(i)
        elif sum(lst) == b/2:
            return print(lst)
        else:
            print("array does not exist")
    return print(lst)

# a = [2,3,4,1]
# split(a)

def splitPoint(arr: int, lst:'list'=[])->int:
    leftsum = 0
    arrlen = len(arr)
    for i in range(0, arrlen):
        leftsum= leftsum+arr[i] #Creating the left sum list
        # print(leftsum)
    rightsum = 0  #initialze right sum
    for i in range(arrlen-1, -1, -1): #traverse from the end
        rightsum=rightsum+arr[i] #add numbers from the right end
        leftsum=leftsum-arr[i] #subtract the number from the left sum that was added to the right sum
        if rightsum==leftsum: #traverse until leftsum = rightsum
            return i  #return i which happens to be the index
    return -1 #if no mid point is found

def twoPart(arr:int)->list:
    val=splitPoint(arr)
    if val!=-1:
        print(arr[:val], arr[val:])
    else:
        print("not found")

b = [2,3,4,1]
twoPart(b)   
