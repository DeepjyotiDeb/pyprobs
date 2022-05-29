# %%
#given 2 numbers that are the base and the power respectively
#evaluate the final value such that the result is a single digit integer
#formed from the sum of integers of the exponent. If the sum is not a 
#single digit, then keep adding the digits of the integer until single value reaches
def total(N):
    sum_tot = T**N #the exponent value
    print(sum_tot)
    solve(sum_tot) #pushing the exponent into the special foo

def solve(tot):
    sd = 0   
    for i in str(tot):
        sd += int(float(i)) #addin the integers

    print(sd)

    if len(str(sd)) <= 1: #if length of integer string < 1
        return sd #objective achieved
    else:
        solve(sd) #else run the foo recursively
    
T = 8
N = 8
total(N)
# T = int(float(input()))

# for _ in range(T):
#     N=int(float(input()))
#     out_ = solve(N)
#     print(out_)