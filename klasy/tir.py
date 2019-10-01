from klasy.car import Car

class Tir(Car):

    def __init__(self, marka, model, maxWeight):
        super(Tir, self).__init__(marka, model)
        self.maxWeight = maxWeight

    #Nadpisywanie metod
    def przyspiesz(self, delta):
        if(delta<5):
            super(Tir,self).przyspiesz(delta)
        else:
            super(Tir, self).przyspiesz(delta-5)


    def pokazLicznik(self):
        print("Twoj licznik wynosi: " + str(self.getPredkosc()))

