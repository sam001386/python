import time
import functools

def display_time(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()
        print(t2 - t1)
    return wrapper

def is_prime(n):
    if n <= 1:
        return False
    for num in range(2, n):
        if n % num == 0:
            return False
    return True

@display_time
def prime_nums(): 
    for i in range(2, 10000):
        if is_prime(i):
            print(i)

prime_nums()
