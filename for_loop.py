# print 0, 1 , 2 to 9
# for i in range(10):
#     print(i)
#
# #  print table of 17
# for j in range(17, 171, 17):
#     print(j)
#
# # print odd no.
# for i in range(20):
#     if i%2 == 0:
#         pass
#     else:
#         print(i)

# prime no
# e.g: 2, 3, 5, 7, 11, 13, 17, 19, 23 ......

for n in range(1, 50):
    for x in range(2, n):
        if n%x == 0:
            # print(n, 'equals', x, '*', n/x)
            break
    else:
        print(n, 'is prime no.')
