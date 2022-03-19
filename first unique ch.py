#%%
from collections import Counter

def unique(str):
    c = Counter(str)
    lst=[]
    for i in c:
        if c[i] == 1:
            return str.index(i)
    return -1

str2 = "loveleetcode"       
str1 = "aabb"       
str="aabcdde"
# unique(str1)
# %% 
#very expensive
def unique1(s):
    for i in s:
        if s.count(i) == 1:
            return s.index(i)
    return -1
s = "leetcode"
s2  = "loveleetcode" 
unique1(s2)
# %%
#same as previous method but with cache. Improves speed by 8x
def unique2(s):    
    cache = set()
    for item in s:
        if item not in cache:
            if s.count(item) == 1:
                return s.index(item)
            else:
                cache.add(item)

    return -1
s = "leetcode"
s2  = "loveleetcode" 
unique2(s2)