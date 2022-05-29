
#%%
def middlevalue(a,b,c):
    if a > b and a < c or a >c and a<b:
        print(a, " is middle")
    elif b>a and b<c or b<a and b>c:
        print(b, " is middle")
    else:
        print(c, " is middle")

a=10
b=10
c=9
middlevalue(a,b,c)