# bool_vale = True
#
# while bool_vale:
#     print(f"Enter number")
#     response = input()
#     if int(response) % 2 == 0:
#         print(f"{response} divisible by 2")
#         bool_vale = False

# normal_str = "Tocsin"
# byte_str = b"Tocsin"
# print(normal_str[0])
# print(byte_str[0])
#
# print(list("Aramide")[0])

from urllib.request import urlopen

story = urlopen("http://sixty-north.com/c/t.txt")
story_words = [x.decode("utf8") for line in story for x in line.split()]
print(story_words)

s = [1, 2, 3]
r = s
print(s == r)

r[1] = 10
print(s)
print(r)


import copy

s = [1, 2, 3]
r = copy.deepcopy(s)
r[1] = 10
print(s)
print(r)

import time

print(time.time())
print(time.ctime())
print("iad12-br-agg-r4".partition('-'))
print("iad12-br-agg-r4".split('-'))

city,_,country = "Dublin:Ireland".partition(":")
print(f"{city}, {country}")

print("The age of {0} is {1}".format('Tosin', 35))
print("The age of {0} is {1}. {0}'s birthday is on {2}".format('Tosin', 35, 'Nov 25'))
print("The age of {} is {}".format('Tosin', 35))
print("The age of {name} is {age}".format(name='Tosin', age=35))

import datetime
print(f"The current time is {datetime.datetime.now().isoformat()}")


names_and_ages = [('Tosin', 35), ('Funto', 31)]
x= dict(names_and_ages)

gender = dict(M="Male", F="Female")
print(gender)

x.update(gender)
print(x)

FANG = {'Amazon', 'Google', 'Netflix', 'Facebook', 'Apple', 'Twitter'}
GOOD = {'Amazon', 'GS', 'Meta', 'Google'}

print(FANG.difference(GOOD))
print(GOOD.difference(FANG))
print(FANG.intersection(GOOD))
print(FANG.symmetric_difference(GOOD))
print(FANG.issubset(GOOD))
print(FANG.isdisjoint(GOOD))