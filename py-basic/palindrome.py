#%%
# Run a While loop with condition as temp number < 0.
# Using modulo operator, extract the last digit from the number.
# Using the formula reverse = reverse * 10 + remainder , we’ll keep updating the reverse variable.
# Using the divide operator, we’ll shorten the number.
# Check if the reversed number matches the original number.
n = int(input('enter number'))
temp = n
rev = 0
while temp > 0:
    rem = temp % 10 #extracting the last digit
    rev = rev * 10 + rem #updating the variable with the last digit
    temp = temp // 10 #get the absolute quotient of the number (shortening it)

if n == rev: print('palindrome', temp, rev)
else: print('not palin', n, rev)
