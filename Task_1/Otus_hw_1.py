from operator import pow
from itertools import repeat
from math import sqrt
from functools import wraps
from timeit import default_timer


# This function returns a list of numbers to the power of a given number
# Using list comprehension
def power(nums, b = 2):
    return [pow(n, b) for n in nums]

my_list = [1, 2, 3, 4, 5]

print(power(my_list, 3))

# The same function (returning a list of numbers raised to a given power)
# Using map() function
def power(nums, b = 2):
    return list(map(pow, nums, repeat(b)))

my_list = [1, 2, 3, 4, 5]

print(power(my_list, 3))

# A decorator to calculate the execution time of a function
def timing_dec(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start_time = default_timer()
        func_result = func(*args, **kwargs)
        end_time = default_timer()
        print('Function execution time is {:.5f}'.format(end_time - start_time))
        return func_result
    return inner

# Constants to be used to show the type of filter
EVEN = 0
ODD = 1
PRIME = 2
# This function returns a list of all even/odd/simple numbers from a list
@timing_dec
def even_odd(nums, f_type):
    if f_type == EVEN:
        return list(filter(lambda x: x % 2 == 0, nums))
    elif f_type == ODD:
        return list(filter(lambda x: x % 2 == 1, nums))
    elif f_type == PRIME:
        return list(filter(is_prime, nums))

# This function checks if a number is prime
def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i ==0:
                return False
        return True

print(even_odd(my_list, PRIME))

# A decorator to trace calls made to the decorated function
def trace(func):
    func.level = 0
    @wraps(func)
    def inner(*args, **kwargs):
        print('____' * func.level + ' --> {}({})'.format(func.__name__, args[0]))
        func.level += 1
        f = func(*args, **kwargs)
        func.level -= 1
        print('____' * func.level + ' <-- {}({}) == {}'.format(func.__name__, args[0], f))
        return f
    return inner



# This function calculates the n-th number in the Fibonacci sequence
@trace
def fibonac(n):
    if n < 2:
        num = 1
    else:
        num = fibonac(n - 1) + fibonac (n - 2)
    return num

print(fibonac(5))
