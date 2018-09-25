import re
# 4
given_list = [
'-rw-rw-r-- 1 root root 134801 Nov 2 14:27 aa_base-13.txt',
'-rw-rw-r-- 1 root root 134801 Nov 2 14:27 aaa_base-extras.txt',
'-rw-rw-r-- 1 root root 134801 Nov 2 14:27 aaa_base-extras.txt',
]
pattern = re.compile('([a-zA-Z0-9_-]+.txt)$')
output = []
for i in given_list:
    output.append(pattern.search(i).group(1))

print(output)
