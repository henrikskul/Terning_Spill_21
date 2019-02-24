class Spiller:
    # setter id telleren
    __id_teller = 1

    # definerer instansvariablene
    def __init__(self, navn="ugitt", poengsum=0):
        self.__id = self.__id_teller
        self.__navn = navn
        self.__poengsum = poengsum
        self.__ferdig = False
        Spiller.__id_teller += 1

    # setter gettere
    @property
    def id(self):
        return self.__id

    @property
    def navn(self):
        return self.__navn

    @property
    def poengsum(self):
        return self.__poengsum

    @property
    def ferdig(self):
        return self.__ferdig

    # setter settere
    @navn.setter
    def navn(self, navn):
        if navn == "":
            raise ValueError("navnet må ha en verdi")
        else:
            self.__navn = navn

    @poengsum.setter
    def poengsum(self, poengsum):
        if poengsum < 0:
            raise ValueError("Poengsummen må være over null")
        else:
            self.__poengsum = poengsum

    @ferdig.setter
    def ferdig(self, ferdig):
        if ferdig == True:
            self.__ferdig = True

# setter en streng som blir printet ut når objektet selv blir printet
    def __str__(self):
        return "\nSpiller {} | Navn: {} | Poengsum: {}".format(self.__id, self.__navn, self.__poengsum)
