#%%
num = 1012
digits = []
while num:
    digit = num % 10
    digits.append(digit)
    num = num // 10
print(digits)
if digits == num:
    print("palindrome")