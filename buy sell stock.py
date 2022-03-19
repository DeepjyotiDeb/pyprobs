# %%
#we use 2ptr solution here
#a 2ptr solution is one where we use 2 pointers who get
# get compared to each other and then have thier places switched
def buySell(prices): 
    leftptr = 0 #buy
    rightptr = 1 #sell
    max_prof = 0
    while rightptr < len(prices):
        if prices[leftptr] < prices[rightptr]:
            profit = prices[rightptr] - prices[leftptr]
            max_prof = max(profit, max_prof)
        else:
            leftptr = rightptr #switch lptr to rptr coz rptr is obviously
        rightptr += 1    #the smaller value
    return max_prof
    
prices = [7,1,5,3,6,4]
prices2 = [7,6,4,3,1]
buySell(prices)