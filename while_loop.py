#!/usr/bin/env python3

# import time
# a = 1
# while a <=10:
#     print(a)
#     a +=1
#     time.sleep(1)

# # Infinte while loop
# a = 'santosh'
# while True:
#     print(a)

#breaking loop
# a = 2
# while 1==1:
#     print(a)
#     a += 2
#     if a > 20:
#         break


# break and continue loop

a = 0
while True:
    a +=1
    print(' hahaha ')
    if a % 2 == 0:
        continue
    print('{:*^20}'.format('santosh'))
    if a >= 16:
        break
    print(a)
