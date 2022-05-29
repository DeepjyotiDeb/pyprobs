#%%
#how does it work?
def badVersion(n,m):
    l, r = 1, n #assign left and right edge
    while l< r:
        mid = (l+r)//2 
        if (mid == m): #if the mid value == the bar version number
            r = mid #switch the right edge to mid
        else:
            l = mid+1 #else switch left edge to middle
    return l

n =7
m=3
badVersion(n,m)