lazy import math
lazy import statistics

class Kalkulator:

    def start(self):
        #otwiera/czysci plik historia.txt, wywoluje wybor
        self.history = []
        open("historia.txt", "a", encoding="utf-8").close()
        print("-----------Kalkulator-----------")
        self.menu()

    def menu(self):

        print("""   Menu:
        [1] Podstawowy — dodawanie, odejmowanie, mn ożenie, dzielenie.
        [2] Naukowy — pierwiastki, potęgi, silnia, logarytmy i trygonometria.
        [3] Statystyczny — średnia, mediana, dominanta.
        [4] Historia — wyświetlanie wcześniejszych obliczeń zapisanych w pliku.
        """)
        try:
            t = int(input("Wybierz opcje z powyższych:"))
        except:
            self.menu()
            return
        if t == 1:
            self.podstawowy()
        elif t == 2:
            self.naukowy()
        elif t == 3:
            self.statystyki()
        elif t == 4:
            self.historia()
            return
        else:
            self.menu()
            return

    def naukowy(self):
        try:
            a = int(input("Podaj a:"))
            b = int(input("Podaj b:"))
        except:
            print("Podaj prawidłowe liczby")
            self.naukowy()
            return
        
        t = int(input("Pierwiastek[1]\nPotęga[2]\nSilnia[3]\nWybierz operacje:"))
        if t == 1:
            return self.pierwiastek(a, b)
        elif t == 2:
            return self.potega(a, b)
        elif t == 3:
            return self.silnia(a, b)
        else:
            print("Następnym razem wybierz prawidłowe działanie")

    def pierwiastek(self, a, b):
        result = math.sqrt(a), math.sqrt(b)

    
        calculation = f"√{a},  √{b} = {result}"
        self.history.append(calculation)
        self.pokaz_historie()

    def potega(self, a, b):
        result = a ** b
    
        calculation = f"{a} ** {b} = {result}"
        self.history.append(calculation)
        self.pokaz_historie() 

    def silnia(self, a, b):
        result = math.factorial(a), math.factorial(b)
    
        calculation = f"!{a}, !{b} = {result}"
        self.history.append(calculation)
        self.pokaz_historie() 

    def statystyki(self):
        try:
            a = int(input("Podaj a:"))
            b = int(input("Podaj b:"))
        except:
            print("Podaj prawidłowe liczby")
            self.statystyki()
            return
        
        t = int(input("Średnia[1]\nMediania[2]\nDominanta[3]\nOdchylenie standardowe[4]\nWybierz operacje:"))
        if t == 1:
            return self.srednia(a, b)
        elif t == 2:
            return self.mediana(a, b)
        elif t == 3:
            return self.dominanta(a, b)
        else:
            print("Następnym razem wybierz prawidłowe działanie")

    def srednia(self, a, b):
        result = (a + b)/2

        calculation = f"({a} + {b})/2 = {result}"
        self.history.append(calculation)
        self.pokaz_historie()
        pass

    def mediana(self, a, b):
        liczby = [a, b] 
        result = statistics.median(liczby)
    
        calculation = f"mediana {a} oraz {b} to {result}"
        self.history.append(calculation)
        self.pokaz_historie() 

    def dominanta(self, a, b):
        liczby = [a, b] 
        result = statistics.mode(liczby)
    
        calculation = f"dominanta {a} oraz {b} to {result}"
        self.history.append(calculation)
        self.pokaz_historie() 

    def historia(self):
        with open("historia.txt", "r", encoding="utf-8") as plik:
                print(plik.read())
 
    def podstawowy(self):
        #zaczyna, pyta o licze i wywoluje działanie
        try:
            a = int(input("Podaj a:"))
            b = int(input("Podaj b:"))
        except:
            print("Podaj prawidłowe liczby")
            self.podstawowy()
            return
        
        t = int(input("Dodawanie[1]\nOdejmowanie[2]\nmnożenie[3]\ndzielenie[4]\nWybierz operacje:"))
        if t == 1:
            return self.dodawanie(a, b)
        elif t == 2:
            return self.odejmowanie(a, b)
        elif t == 3:
            return self.mnozenie(a, b)
        elif t == 4:
            return self.dzielenie(a, b)
        else:
            print("Następnym razem wybierz prawidłowe działanie")

    def dodawanie(self, a, b):
        result = a + b

        calculation = f"{a} + {b} = {result}"
        self.history.append(calculation)
        self.pokaz_historie()

    def odejmowanie(self, a, b):
        result = a - b

        calculation = f"{a} - {b} = {result}"
        self.history.append(calculation)
        self.pokaz_historie()

    def mnozenie(self, a, b):
        result = a * b
    
        calculation = f"{a} * {b} = {result}"
        self.history.append(calculation)
        self.pokaz_historie() 

    def dzielenie(self, a, b):
        if b == 0:
            print("Nastepnym razem podaj prawidłowe liczby")
        else:
            result = a / b 
            calculation = f"{a} / {b} = {result}"
            self.history.append(calculation)
            self.pokaz_historie()
 
    def pokaz_historie(self):
        print(self.history[-1])
        with open("historia.txt", "a", encoding="utf-8") as plik:
            plik.write(f"{self.history[-1]}\n")

        self.petla()

    def petla(self):
        try:
            q = int(input("Czy chcesz kontunuować?\nTak[1]/Nie[2]:"))
        except:
            print("Zdecyduj się")
            self.petla()
        if q == 1:
            self.menu()
        else:
            for calculation in self.history:
                print(calculation)
            return 



kalkulator = Kalkulator() 
#wywołuje start, zaczyna program
kalkulator.start()