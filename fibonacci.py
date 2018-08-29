"""
Fibonacci series: 1, 1, 2, 3, 5, 8, 13, 21......
Logic: The sum of two element defines the next.
"""
# initial value
a, b = 0, 1

while True:
    a, b = b, a+b
    if a >50:
        break
    print(a)
