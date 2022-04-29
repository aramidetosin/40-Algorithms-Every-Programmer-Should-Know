class Person:
    number_of_people = 0  # Class attribute

    def __init__(self, name):
        self._name = name
        # Person.number_of_people += 1
        Person.add_person()

    # Class method
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


p1 = Person('Tosin')
p2 = Person('Dayo')

# print(Person.number_of_people)
print(Person.number_of_people_())