from math import factorial

def coin_probability(n, k):
    nCk = factorial(n)/(factorial(k)*factorial(n-k))
    omega = 2**n
    return nCk/omega
print([coin_probability(5,k) for k in range(6)])

x = [1,3,4,4,5]
print(type(x))
