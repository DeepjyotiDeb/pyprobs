#%%
def gen(numrows):
    res = [[1]] #creating the first row
    for i in range(numrows-1): #since we already have the first row
        temp = [0] + res[-1] + [0] #creating 0 on both ends for adding into triangle
        row = []
        for j in range(len(res[-1])+1): #entering into the last array
            row.append(temp[j]+temp[j+1]) #adding the elements in temp using index j
        res.append(row)
    return res

numrows = 5
gen(numrows)
