#!/usr/bin/env python3

import math
# S_N = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N
#      +2 + 2/2 + 2/3 + 2/4 + ... + 2/N
#     ...
#       M + M/2 + M/3 + M/4 + ... + M/N
#      
sum = 0.0
N=6000

for n in range(N):
    sum = sum + math.pow(1.0/(n+1),2)
    print(sum)
    
# \infty + 1 = \infty
# 1 - \infty = -\infty
# \infty + \infty = \infty
# \infty - \infty = ?

# sum1 = 1 + 2 + 3 + 4 + 5 + .. + n, n->\infty -> sum1 = \infty

# sum2 = 1^2 + 2^2 + 3^2 + 4^2 + 5^2 + .. + n^2, n->\infty -> sum2 = \infty

# sea  x el valor en sum1 tal que siempre corresponde un unico valor x^2 en la sum2.
