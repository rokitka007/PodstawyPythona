import cwiczenie.foo
from cwiczenie2.boo import *

#Nawigacja: CTRL + Lewy przycisk myszki na elemencie
#Komentowanie/odkomentowywanie: CTRL + /
#Usuń linie: CTRL + Y

#Zmienne globalne
avar = "Globalna"

def lokalnie():
    #Wypisywanie zmiennej globalnej
    global avar
    print(avar)
    bvar = "lokalnie"
    avar = "globalnie -> lokalnie"
    print(avar)
    def zagniezdzenie():
        avar = "lokalnie -> zagniezdzenie"
        print(avar)
    zagniezdzenie()

#funkcja z atrybutem
def funckjaFor(lista):
    for i in lista:
        print(i)

#funkcja ze zwrotką
def zwrocImie(plec):
    if(plec):
        return "Agata"
    else:
        return "Tomek"


if __name__ == "__main__":
    # nrStolikow()
    # cwiczenie.foo.listaGosci()
    #
    #
    # #Przestrzeń nazw
    # #globalnie
    # print(avar)
    # lokalnie()
    # print(avar)

    # for i in [1,2,3]:
    #     print(str(i))
    # funckjaFor([5,8,9])
    # funckjaFor(["a", "b", "c"])
    # funckjaFor({"key":"valuue", "key2": "value2"})
    # funckjaFor("Kasia")

    zwrocImie(True)
    imie = zwrocImie(True)
    print(imie)
    imie2 = zwrocImie(False)
    print(imie2)


