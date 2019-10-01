import os

def addMultipleAttributes(*args):
    counter = 0
    for el in args:
        counter += el
    return counter

def addKeywordedArgumenst(**kwargs):
    message = ""
    #iterujemy po itemach (parze klucz - wartość) słownika, a nie samym kluczu,
    #stąd konieczność użycia funkcji items() na słowniku kwargs
    for el, key in kwargs.items():
        message += el + " " + key + "\n"
    return message

if __name__ == '__main__':
    pass
    #args i kwargs
    #Dodaj nieznaną liczbę argumentów jako lista
    liczba = addMultipleAttributes(1,5,78,4)
    print(liczba)

    #Dodaj nieznaną liczbę argumentow w formacie słownika (para klucz - wartość)
    # wiadomosc = addKeywordedArgumenst(first = "1", second="2", third="3")
    # print(wiadomosc)
    # wiadomosc2 = addKeywordedArgumenst(kobieta = "Ania", mezczyzna = "Robert")
    # print(wiadomosc2)

    #Operacje na plikach
    text = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit,",
            " sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
            " Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi",
            " ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit",
            " in voluptate velit esse cillum dolore eu fugiat nulla pariatur. ",
            "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia",
            " deserunt mollit anim id est laborum."]
    print(len(text))

    #Tryb zapisu ('w'): tworzy nowy plik i nadpisuje jego zawartość
    #Tryb append('a'): otwiera istniejacy plik i dodaje do niego nowy tekst
    #Tryb read('r'): plik otwarty tylko do odczytu
    #Tryb create('c'): tworzy plik
    #Tryb zapisz/odtworz ('w+'): tworzy plik, nadpisuje ale i odczytuje
    #sposób pierwszy otwierania pliku (tryb zapisu)
    file = open("plikByOpen.txt", "w")
    file.writelines(text)
    file.write("Cos ode mnie")
    # zawsze trzeba zamknac plik
    file.close()

    #sposób drugi otwierania pliku (tryb zapisu)
    # with open("plikByOpen.txt", "w+") as file:
    #     file.write("Otwieramy plik za pomoca with w trybie write\n")
    #     lines = file.readlines()
    # with open("plikByOpen.txt", "a") as file:
    #     for line in text:
    #         file.write(line + "\n")
    # with open("plikByOpen.txt", "r") as file:
    #     lines = file.readlines()
    #     for line in lines:
    #         print(line)

    #sprawdz gdzie jestem
    print(os.getcwd())

    #przejdz do innego katalogu
    os.chdir("..")
    print(os.getcwd())
    os.chdir("D:\Pycharm Projects\PodstawyPythona2")
    print(os.getcwd())

    # #stworz nowy folder/katalog
    # os.mkdir("mojaSciezka")

    #usun folder/katalog
    os.rmdir("mojaSciezka")





