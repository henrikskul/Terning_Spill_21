from terning import *
from spiller import *
# import terning as t


# lager klassen TerningSpill
class TerningSpill:
    # definerer variablene
    def __init__(self, spiller_input):  # legg til: =Spiller()
        self.__sum = 0
        self.__terning = Terning()
        self.__spiller = spiller_input

    @property
    def spiller(self):
        return self.__spiller

    @property
    def sum(self):
        return self.__sum

    # spiller første runde, hvor terningen skal trilles tre ganger og blir lagt til i summen til hver av spillerene
    def forste_runde(self):
        # henter hver objekt enkeltvis, bruker dette mye.
        for id_spiller in self.__spiller:
            self.__sum = 0
            # trille rterningen 3 ganger, og legger til i spill-objektet sin sum.
            for i in range(3):
                self.__terning.kast()
                self.__sum += self.__terning.verdi
            # setter spiller-objektet sin sum lik spill-objektet sin sum
            id_spiller.poengsum = self.__sum
        print("\nPoengsummene til spillerene er:")
        for id_s in self.__spiller:  # printer ut spiller informasjon etter første runde
            print(id_s)

    # Spiller runde 2, hvor spillerene skal kunne velge om de vil trille terningen på nytt.
    def neste_runde_vol2(self):
        self.__sum = 0
        spill = 0  # setter variabel som blir 1 når spillet et ferdig får å bryte whileløkka
        ant_spillere = 0
        print("\nforste runde ferdig.")
        for id_spiller in self.__spiller:  # setter tallet for antall spillere
            ant_spillere += 1
        # hovedløkka
        while spill == 0:
            # hoved for-løkke, hvor alle spillerene skal hver for seg spille en runde, med mindre de er ferdig
            for id_spiller in self.__spiller:
                tall = 0
                if id_spiller.ferdig:  # sjekker om spiller er ferdig
                    tall = 1
                # Går inn i denne løkka hvis spiller ennda er med
                while tall == 0:
                    print("\nSpiller:")  # printer info om spilleren
                    print(id_spiller)
                    ny_runde = input("Vil Du spille en ny runde? (ja/nei)")  # spiller velger om det skal spilles en til runde
                    if ny_runde == "ja":  # hvis ja, terningen trilles om summen blir lakt til den eksisterende summen til spilleren
                        self.__sum = id_spiller.poengsum
                        self.__terning.kast()
                        self.__sum += self.__terning.verdi
                        id_spiller.poengsum = self.__sum
                        print("Ny poengsum: ", id_spiller.poengsum)
                        tall = 1  # kommer ut av whileløkka
                        if id_spiller.poengsum > 21:  # setter poengsum til 0 viss den er over 21
                            id_spiller.poengsum = 0
                            id_spiller.ferdig = True
                            print("Du Tapte, poengsum ble over 21.")
                    elif ny_runde == "nei":  # hvis nei, setter ferdig-attributen til spiller lik TRUE.
                        print(id_spiller.navn, "har valgt og avslutte spillet")
                        print("Din sluttsum ble: ", id_spiller.poengsum)
                        id_spiller.ferdig = True
                        tall = 1  # kommer ut av whileløkka
                    else:  # gjentar whileløkka så spilleren får ny sjangse til å skrive gyldig verdi
                        print("Du skrev inn en ugyldig vedi, prøv igjen.")
            ferdig_test = 0
            # sjekker om alle er ferdig
            for id_spiller in self.__spiller:
                if id_spiller.ferdig:
                    ferdig_test += 1
            if ferdig_test == ant_spillere:
                spill = 1

    # Sjekker hvem som vinner, gjelder å være nermest 21 men ikke over
    def vinner(self):
        liste = []  # bruker denne lista til å legge alle poengsummene i
        print("\n")
        for id_spiller in self.__spiller:  # skiver ut nåværende summer
            print(id_spiller.navn, "sin sum ble:", id_spiller.poengsum)
            liste.append(id_spiller.poengsum)  # legger poengsummene inn i lista
        vinner_sum = max(liste)  # sjekker maksverdien på lista
        ant_vinnere = 0
        # sjekker hvor mange som har høyeste sum
        for id_spiller in self.__spiller:
            if id_spiller.poengsum == vinner_sum:
                ant_vinnere += 1
        # hvis mer en en har høyeste sum, blir det printet uavgjort mellom spillerene
        if ant_vinnere > 1:
            print("\nDet ble uavgjort mellom: ")
            for id_spiller in self.__spiller:
                if id_spiller.poengsum == vinner_sum:
                    print("-", id_spiller.navn)
        else:
            # hvis det bare er en spiller, blir denne forløkka kjørt.
            for id_spiller in self.__spiller:
                if id_spiller.poengsum == vinner_sum:
                    print("\n")
                    print(id_spiller.navn, "har vunnet!\nSpillet vil nå avsluttes, start på nytt viss ønskelig")


# lager en liste med objekter fra klassen "Spillere" som blir sendt til objektet "spill" i "spill_terning" funksjonen
def start_tering_spill():
    spiller = []
    # setter input inn i en whileløkke slik at bruker blir tvingt til å skrive inn riktig verdi
    tall = 0
    while tall == 0:
        try:
            antall_spillere = int(input("Skriv inn antall spillere (positiv heltallsverdi): "))
            if antall_spillere > 0:
                for i in range(antall_spillere):
                    navn = input("skriv inn navnet på spiller ")
                    spiller.append(Spiller(navn))
                return spiller
            else:
                raise ValueError
        except ValueError:
            print('Du skrev inn noe ugyldig')

# hovedfunksjonen som lager et spillobjekt av klassen "Terningspill" ved bruk av "start_terning_spill funksjonen.
def spill_terning():
    spill = TerningSpill(start_tering_spill())
    # kaller på metodene til objektet "Spill" for å kjøre spillet.
    spill.forste_runde()
    spill.neste_runde_vol2()
    spill.vinner()


if __name__ == '__main__':
    spill_terning()
