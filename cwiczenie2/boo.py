import cwiczenie.foo

def nrStolikow():
    nrStolikow = [1,2,3]
    print("Goście: ")
    cwiczenie.foo.listaGosci()
    print(" będą siedzieć przy stolikach: " + str(nrStolikow))
    print("a goście z mojego modułu to:" )
    listaGosci()

def listaGosci():
    lista1 = ["Tomek", "Paweł", "Grzegorz"]
    print(lista1)