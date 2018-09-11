def fibonacci(num):
    a, b, c = 0, 1, []
    while True:
        c.append(a)
        a, b = b, a+b
        if b>=num:
            break
    return  c

# g = fibonacci(50)
# print(g)
if __name__ == "__main__":
    f = fibonacci(50)
    print(f)
