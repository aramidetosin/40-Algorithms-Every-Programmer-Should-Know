import logging

logging.basicConfig(level=logging.INFO, filename='log.log', filemode='w', format="%(asctime)s - %(levelname)s - %("
                                                                                 "message)s")
logger = logging.getLogger(__name__)
handler = logging.FileHandler('dog.log')
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)


class Dog:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # def age(self, age):
    #     return age+1
    #
    # def bark(self):
    #     logger.info(f"bark")

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def name(self):
        return self._name

    def age(self):
        return self._age

    def set_age(self, x):
        return self._age + x


d = Dog("Tim", 35)
logger.info(f"{d.get_name()}")
logger.info(f"{d.get_age()}")
logger.info(d.set_age(30))