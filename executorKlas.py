from klasy.car import Car
from klasy.tir import Tir

if __name__ == "__main__":
    print("Egzekutor klas")

    #Inicjalizacja obiektów
    opel = Car("opel", "astra")
    bmw = Car("bmw", "x3", "czarny", 2008)

    print("Pierwsze auto:\n")
    print(opel.model + " " + opel.marka)
    print("kolor: " + opel.color + " rocznik: " + str(opel.rocznik))


    print("Drugie auto:\n")
    print(bmw.model + " " + bmw.marka)
    print("kolor: " + bmw.color + " rocznik: " + str(bmw.rocznik))

    bmw.setPredkosc(50)
    print("Moja predkosc bazowa: " + str(bmw.getPredkosc()))
    bmw.przyspiesz(50)
    print("Predkosc po przyspieszeniu: " + str(bmw.getPredkosc()))
    bmw.przyspiesz(100)
    # bmw.przyspiesz(50)
    bmw.hamuj(300)
    print("Predkosc po wyhamowaniu to: " + str(bmw.getPredkosc()))

    tir = Tir("Man", "500", 25)
    print(tir.model)
    tir.setPredkosc()
    tir.przyspiesz(50)
    tir.pokazLicznik()
    tir.przyspiesz(3)
    tir.pokazLicznik()

