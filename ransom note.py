#%%
#from magazine m, create ransom note
def ransom(rn , m):
    # return all(rn.count(c)<=m.count(c) for c in rn)
    for c in m:
        # if rn.count(c)<=m.count(c):
            print(m.count(c))

rn = "aac"
m = "aab"
ransom(rn ,m)
# %%
#youtube
def ransom1(rn , m):
    if len(rn)>len(m):
        return False #edgecase
    dict = {}
    for i in m:
        if i in dict: #creating a dictionary out of magazine
            dict[i] += 1
        else:
            dict[i] = 1
    #remember that it also possible to compare between lists and dictionaries
    for char in rn:
        if char not in dict: #if the ransom character is not in the magazine, then false
            return False #another edge case
        if dict[char] == 0: #gotta return false, if there arent enough characters to fill up
            return False #meaning that the char does not exist
        dict[char] -= 1 #decrement the value in magazine dict by 1, since its counterpart was found in ransomNote
    return True #if no false is encountered then true...duh

rn = "aac"
m = "aab"
ransom1(rn ,m)
# %%
def ransom2(ransomNote, magazine):
    for i in set(ransomNote): #sets dont keep copies
        if magazine.count(i) < ransomNote.count(i): #if the no. of i's in ransom is 
            return False #less than no. of i's in magazine then false
    return True

rn = "aac"
m = "aab"
ransom2(rn ,m)