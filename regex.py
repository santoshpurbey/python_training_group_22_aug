import re

# re.compile(signature) # create a regex object, arg -> pattern or signature

# re.search() # find a pattern in a string() , arg -> string object

# re.match()
# re.findall() # return all matches in a string
# re.group() # get matched string

# re.search(pattern, string)

# \w # alpha and num [a-zA-z0-9_]
# \d # any numeric digit [0-9]
# \s whitespace character (space, newline , tab)
# \D not numeric
# \W not word digit or undersore
# \S not whitespace character

#  + # 1 ore more
#  * # 0 or more
#  ?: # 0 or 1
# {n} # exactly integer k occurence
# {m,n} # m to n occurance inclusive
# . # matches any character except new line
# ^ # start of the string
# $ # end of the string
# \ # escape character

test_string = "Mon, 22 Aug 2016 13:15:39 +0200|178.57.66.225|santosh| - |user logged in| -"
d_pattern = r'(.{0,25}\w+)'
a_pattern = r'-.\|([a-z0-9\s]+)\|.-'
u_pattern = r'\|(\w+)\|'
i_pattern = r'\|(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\|'
compiled_obj = map(lambda x: re.compile(x), [d_pattern, u_pattern, i_pattern ,a_pattern])

# activity_pattern = re.compile(a_pattern)
# user_pattern = re.compile(u_pattern)
# ip_pattern = re.compile(i_pattern)

# activity = activity_pattern.search(test_string).group(1)
# user = user_pattern.search(test_string).group(1)
# ip = ip_pattern.search(test_string).group(1)
date, user, ip, activity = map(lambda x: x.search(test_string).group(1), compiled_obj)
print(date,user, ip, activity)
