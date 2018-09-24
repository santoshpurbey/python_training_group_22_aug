import csv
# with open('number.csv',) as f:
#     r = csv.reader(f)
#     print(''.join([ j for i in r for j in i]))


with open('furits_list.csv', 'w') as f:
    w = csv.DictWriter(f, fieldnames= ['fruit', 'season'])
    w.writeheader()
    w.writerows([{'fruit':'mango', 'season':'summer'},])
