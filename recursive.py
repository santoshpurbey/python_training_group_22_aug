a = 0
def factorial(n):
    global a
    if n == 1:
        a = 5
        return n
    else:
        return n*factorial(n-1)

print(factorial(5))
print(a)
