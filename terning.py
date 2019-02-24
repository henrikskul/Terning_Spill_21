import random


class Terning:
    def __init__(self, antall_sider=6):
        self.__verdi = 1
        self.__sider = antall_sider

    def kast(self):
        self.__verdi = random.randint(1, self.__sider)

    @property
    def verdi(self):
        return self.__verdi
