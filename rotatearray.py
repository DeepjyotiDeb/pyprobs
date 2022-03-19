#%%
#works but leetcode doesnt see nums for some reason
def rotator(nums, k):
    lst = [0]*len(nums)
    for i in nums:
        if nums.index(i)+k< len(nums):
            lst[nums.index(i)+k] = i
        else:
            lst[(nums.index(i)+k)%len(nums)] = i# (i+k)%len(arr) = index from where the leftover values must be inserted
    nums = list(lst)
    return nums

nums = [11, 2, 56, 4, 32]
k = 3
# rotator(nums, k)
# %%
#from yt
#again pointer hell
def rotator1(nums, k):
    k = k % len(nums) # Now k could be greater than the length of the array.
    l, r = 0, len(nums) - 1 #l starts from 0, r starts from the end of array
    while l<r: #reversing the main array
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l+1, r-1
    
    l,r = 0, k-1#l starts from 0, r start from the rotation value, ie k 
    while l<r: # reversing the beginning portion before k
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l+1, r-1

    l, r = k, len(nums)-1#l starts from the rotation value, r is the len of array
    while l<r: #reversing the postion after k
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l+1, r-1
    # l,r 
    # return nums

nums = [1,2,3,4,5,6]
k = 3
rotator1(nums, k)