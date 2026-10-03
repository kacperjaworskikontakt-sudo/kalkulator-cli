class Kalkulator:
    def __init__(self):
        pass

    def liczby(self):
        a = input("Podaj pierwsza liczbe")
        b = input("Podaj druga liczbe")
        return a, b

    
    def sprawdz(self, a, b):
        try:
            a = float(a)
            b = float(b)
            return a, b
        except ValueError: 
            print("Następnym razem podaj prawidłowe liczby")
            exit()
    
    def dodawanie(self, a, b):
        return(a + b)

    def odejmowanie(self, a, b):
        return(a - b)

    def mnożenie(self, a, b):
        return(a * b)

    def dzielenie(self, a, b):
        return(a/b)

    def procenty(self):
        pass

    def potega(self):
        pass

kalkulator = Kalkulator()

a, b = kalkulator.liczby()
a, b = kalkulator.sprawdz(a, b)

wynik = kalkulator.dodawanie(a, b)

print(wynik)