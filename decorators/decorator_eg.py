def decor(func):
    def wrapper():
        print('*********')
        func()
    return wrapper

@decor
def greet():
    print('hello')

greet()
greet()
greet()
greet()
