class Pet:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def show(self):
        print(f'I am a {self._name} and i am {self._age} years old')


class Cat(Pet):
    def speak(self):
        print('Meow')


class Dog(Pet):

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self._color = color

    def speak(self):
        print('Bark')

    def show(self):
        print(f'I am a {self._name} and i am {self._age} years old and color {self._color}')


d = Pet('tim', 19)
d.show()

c = Cat('bill', 100)
c.show()
c.speak()

y = Dog('lol', 70, 'black')
y.show()
