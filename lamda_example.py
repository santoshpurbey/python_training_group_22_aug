# def increas(l):
#     r = []
#     for i in l:
#         r.append(i*1.2)
#     return r
#
price_list = [10, 20, 30, 40, 50, 40, 30, 20]
# reuslt = increas(price_list)
# print(reuslt)
# def a(arg):return arg*1.2

# reuslt = list(map(lambda x:x*1.2, price_list))
# print(reuslt)
#
# def table(n):
#     return list(map(lambda x: x*n, range(1, 11)))
#
# if __name__ == "__main__":
#     num  = int(input("enter any number:"))
#     print(table(num))


####### Filter ########
# data = range(-10, 10)
# print(list(data))
# f_data = list(filter(lambda x: x>0 and x%2 == 0, data))
# print(f_data)



########## Reduce ###
# from functools import  reduce
#
# s = reduce(lambda x,y: x+y, range(1, 6))
# print(s)



l1 = [4, 3, 6, 8, 2,0, 5]
l2 = [94, 88, 45, 99, 97, 22, 55]
l3 = [11, 55, 33, 77, 22, 88, 44]
print(l1,l2)
data = zip(l1,l2)
data.sort()
l1, l2 = zip(*data)
# l1, l2= map(lambda r: list(r), zip(*data))
print(l1, l2)
