from decimal import *
import timeit

def fibonacci1(i: int) -> int:
    if i <= 1:
        return i
    else:
        return fibonacci1(i - 1) + fibonacci1(i -2)

def fibonacci2(i: int) -> int:
    n1: int = 0
    n2: int = 1
    n3: int = 0

    if i <= 1:
        return i
    
    for num in range(1, i):
        n3 = n1 + n2
        n1 = n2
        n2 = n3

    return n3

def fibonacci3(i: int) -> int:
    # Credit: https://medium.com/starts-with-a-bang/ask-ethan-what-explains-the-fibonacci-sequence-0dfc9822184f
    if i <= 1:
        return i
    length = len(str(i)) + 1
    length = 2 + (length % 2)

    quotient = 89

    quotient2 = str('{:9^' + str(length * 2) + '}').format(quotient)

    getcontext().prec = length * i

    # Strip off the leading 0.
    nums = str(Decimal('1') / Decimal(quotient2))[2:]

    j: int = int(length*i)
    k: int = int(length*(i+1))
    num = int(nums[j:k])

    return num


num = 10

print("fibonacci recursive:")
for i in range(num):
    print(fibonacci1(i))
print()

print("fibonacci iterative:")
for i in range(num):
    print(fibonacci2(i))
print()

print("fibonacci quotient:")
for i in range(num):
    print(fibonacci3(i))
print()

print("fibonacci recursive timeit:")
print(timeit.timeit("fibonacci1(10)", setup="from __main__ import fibonacci1"))
print()

print("fibonacci iterative timeit:")
print(timeit.timeit("fibonacci2(10)", setup="from __main__ import fibonacci2"))
print()

print("fibonacci quotient timeit:")
print(timeit.timeit("fibonacci3(10)", setup="from __main__ import fibonacci3"))
print()