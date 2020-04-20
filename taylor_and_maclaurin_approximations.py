import derivative
import numpy as np
import math

def taylor_series(function, n):
    pass

def maclaurin_series(function, n):
    pass

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num*=i
    return num

def DP_factorial(n):
    temp_arr = [1 for _ in range(n+1)]
    for i in range(1, n+1):
        temp_arr[i] = temp_arr[i-1]*i
    return temp_arr

def taylor_trig(x_val, type = "cos", nth_term = 5):
    # takes in radian, returns in degrees
    nth_val = np.zeros(nth_term+1)
    factoral_array = DP_factorial(2*nth_term)
    print(factoral_array)
    if type == "cos":
        # summation from 0 to infinity of  ( (-1)^n * x^2n) / (2n)!
        for i in range(nth_term):
            print(2*i,  (x_val**(2*i)), factoral_array[2*i])
            nth_val[i] = ((-1)**i) * (x_val**(2*i)) / factoral_array[2*i]

    elif type == "sin":
        # summation from 0 to infinity of ((-1)^n * x^2n+1) / (2n+1)!
        pass
    elif type == "tan":
        pass
    print(nth_val)
    return sum(nth_val)%360


x = taylor_trig(math.radians(15), "cos", 10)
print(x)
print(math.cos(15))