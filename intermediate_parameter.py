class Car:
    def __init__(self, make, model, year, condition='New', kms=0):
        self._make = make
        self._model = model
        self._year = year
        self._condition = condition
        self._kms = kms

    def display(self, showAll=True):
        if showAll:
            print(
                f"This is {self._make} {self._model} from {self._year}, it is a {self._condition} and has {self._kms}km")
        else:
            print(f"This is {self._make} {self._model} from {self._year}")


whip = Car('Ford', 'Fusion', 2012)
whip.display()


# Class method

class Person:
    population = 50

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @classmethod
    def get_population(cls):
        return cls.population

    @staticmethod
    def isAdult(age):
        return age >= 18

    def display(self):
        print(f"{self._name} is {self._age} years old")


person1 = Person('Tosin', 35)
print(Person.get_population())
print(Person.isAdult(35))
person1.display()

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

newList = []


def squareit(x):
    return x ** x


for i in li:
    newList.append(squareit(i))

print(newList)

print([squareit(i) for i in li if i % 2 == 0])

# map

print(list(map(squareit, li)))


# Filter

def isOdd(x):
    return x % 2 != 0


def add7(x):
    return x + 7


a = list(range(0, 11))
b = list(filter(isOdd, a))
print(b)

c = list(map(add7, filter(isOdd, a)))
print(c)

# Lambda

func2 = lambda x: x + 2
print(func2(1))

print((lambda x: x + 2)(1))


def new_func(x):
    func3 = lambda x: x + 5
    return func3(x) + 85


print(new_func(2))

print((lambda x, y: x + y)(1, 2))

print(list(map(lambda x: x ** x, list(range(0, 11)))))
print(list(map(lambda x: x + 7, filter(lambda x: x % 2 != 0, list(range(0, 11))))))
