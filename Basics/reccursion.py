# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)


# print(factorial(5))


#exponential number

def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent-1) 
        #background: 2 * (2 * 2) => 2 * (2 * 1) => return 1
    


print(power(2,3))