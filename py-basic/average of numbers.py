#%%
n = int(input("enter  range"))
a=[]
for i in range(0, n):
    ele = int(input("enter"))
    a.append(ele)

print(a)    
avg = sum(a)/n
print(avg)