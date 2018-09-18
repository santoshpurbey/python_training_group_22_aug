## Functions can be referred by variables
def greet():
    print('im greet funtion!')

a = greet
a()

## Functions can be passed as arguments to another function
def greet():
    print('im greet funtion!')

def hello(func):
    func()
    print('im hello function')
hello(greet)
## Functions can be defined inside another function
def say_hello():
    i = 'abc'
    print('hello')
    def say_welcome():
        print('welcome')
        print(i)
    say_welcome()

a = say_hello()

## Functions can return references to another function
def say_hello():
    i = 'abc'
    print('hello')
    def say_welcome():
        print('welcome')
        print(i)
    return say_welcome

a = say_hello()
a()
