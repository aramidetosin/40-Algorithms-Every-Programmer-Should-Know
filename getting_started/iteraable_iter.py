iterable = ['Spring', 'Summer', 'Autumn', 'Winter']
iterator = iter(iterable)

next(iterator)
next(iterator)
next(iterator)
next(iterator)
# next(iterator)



# def first(iterable):
#     iterator  = iter(iterable)
#     try:
#         return next(iterator)
#     except StopIteration:
#         raise ValueError("iterable is empty")
#
#
# print(first([1,2,3]))
# print(first([]))



any([False, False, True])
all([True, True, True])

mon = [1,2,3,4,5]
sun = [6,7,8,8,9]
tue = [1,0,1,1,1]
for i,j in zip(mon, sun):
    print(f"average; {(i+j)/2}")

from itertools import chain

temp = chain(mon, sun, tue)

for i in temp:
    print(i)