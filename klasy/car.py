
#Klasa jest modelem odwzorowyjącym rzeczywistość
class Car():

    def __init__(self, model, marka, color = "srebrny", rocznik = 1990):
        print("Hej, jestem w konstruktorze!")
        self.model = model
        self.marka = marka
        self.color = color
        self.rocznik = rocznik
        self.max = 150

    #Setter - ustawia wartosc atrybutu
    def setPredkosc(self, predkosc=0):
        self.predkosc = predkosc

    #Getter - zwrocic wartosc atrybutu
    def getPredkosc(self):
        return self.predkosc

    def przyspiesz(self, delta):
        #wyrzucanie wyjątków
        if (self.predkosc >= self.max):
            raise CarException("Predkosc juz jest maksymalna " + str(self.max))
        if(self.predkosc + delta >= self.max):
            self.predkosc = self.max
        self.predkosc += delta

    def hamuj(self, delta):
        #instrukcja warunkowa
        if(delta < self.predkosc):
            self.predkosc -= delta
        else:
            self.predkosc = 0

#dziedziczymy po Exception, słowko pass oznacza, ze nic w tej klasie nie zmieniamy
class CarException(Exception):
    pass