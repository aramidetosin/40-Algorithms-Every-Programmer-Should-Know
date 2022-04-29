# import collections
from collections import Counter
from string import ascii_letters
from random import choice

# containers that store collections
# list
# set
# dict
# tuple- immutable

# Types
# counter
# deque
# namedTuple()
# orderedDict
# defaultdict

# x = [choice(ascii_letters) for i in range(10)]
# print(''.join(x))

c = Counter(''.join([choice(ascii_letters) for i in range(10)]))
print(c)

d = Counter({'a':1, 'b': 3})
print(d)

e = Counter(dogs=2, cats=5)
print(e)

print(list(e.elements()))
print(e.values())

print(c.most_common(2))

new_c = Counter(a=4, b=2, c=0, d=-2)
new_d = ['a', 'b', 'b', 'c']

new_c.subtract(new_d)
print(new_c)
new_c.update(new_d)
print(new_c)



from collections import namedtuple
Point = namedtuple('Point', 'x y z')
newP = Point(2,4,5)
print(newP.x)

PointList = namedtuple('PointList', ['x', 'y', 'z'])
newP2 = PointList(1,2,3)
print(newP2)
print(newP2._asdict())
print(newP2._fields)
zz = newP2._replace(y=6)
print('=====')
print(zz)
PointDict = namedtuple('PointDict', {"x": 0, "y": 0, "z" :0})
print(PointDict(3,4,5))

p22 = Point._make(['a', 'b', 'c'])
print(p22)

from collections import deque
d = deque("Aramide")
print(d)
d.append('o')
d.appendleft('a')
print(d)
print(d[0])

# pop and popleft
# extend and extendleft

d.rotate(-2)
print(d)
d.rotate(2)
print(d)

e = deque("Tosin", maxlen=5)
print(e)
e.append('A')
print(e)
