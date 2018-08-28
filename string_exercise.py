my_string = input('Enter a string:')

if len(my_string)>1:
    print(my_string[:2]+my_string[-2:])
else:
    print('Empty string')

