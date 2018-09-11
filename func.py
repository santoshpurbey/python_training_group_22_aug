import  datetime


def sum_(args):
    """
    This is function return sum of args
    """
    return  sum(args)

def x():
    """
    args: None
    return: tuple
    """
    return 1,2,3,4

def info(name,*args,age=25):
    print(f'My name is {name} and age {age}, {args}')


# variable length arguments

# def inf_(*args):
#     print(type(args))

# variable length keyword arguments
def greet(**kwargs):
    print(kwargs, type(kwargs))
    print(datetime.datetime.now())
    print(f"Hello {kwargs['name']}, {kwargs['age']}!")



def  hello(name, *args, age=5, **kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)


hello('santosh', 'hahaah', 'hdhdh',      'hdhhhd', age=44,name1='yash', add='jdjdj')
