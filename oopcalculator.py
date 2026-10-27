class Kalkulator:
#dodac tryby naukowwe dodać moduły math, statistics
#zrobic takie menu:
#[1] Podstawowy — dodawanie, odejmowanie, mnożenie, dzielenie.
#[2] Naukowy — pierwiastki, potęgi, silnia, logarytmy i trygonometria.
#[3] Statystyczny — średnia, mediana, dominanta i odchylenie standardowe.
#[4] Historia — wyświetlanie wcześniejszych obliczeń zapisanych w pliku.

    def start(self):
        #otwiera/czysci plik historia.txt, wywoluje wybor
        self.history = []
        open("historia.txt", "w", encoding="utf-8").close()
        self.menu()

    def menu(self):
        #skonczyc menu
        print("-----------Kalkulator-----------")
        print("""   Menu:
        [1] Podstawowy — dodawanie, odejmowanie, mn ożenie, dzielenie.
        [2] Naukowy — pierwiastki, potęgi, silnia, logarytmy i trygonometria.
        [3] Statystyczny — średnia, mediana, dominanta i odchylenie standardowe.
        [4] Historia — wyświetlanie wcześniejszych obliczeń zapisanych w pliku.
        """)
        try:
            t = int(input("Wybierz opcje z powyższych:"))
        except:
            self.menu()
            return
        if t == 1:
            self.wybor()
        elif t == 2:
            pass
        elif t == 3:
            pass
        elif t == 4:
            pass
        else:
            pass



    def wybor(self):
        #zaczyna, pyta o licze i wywoluje działanie
        try:
            a = int(input("Podaj a:"))
            b = int(input("Podaj b:"))
        except:
            print("Podaj prawidłowe liczby")
            self.wybor()
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
        for calculation in self.history:
            print(calculation) 
        with open("historia.txt", "a", encoding="utf-8") as plik:
            plik.write(f"{calculation}\n")

        self.petla()

    def petla(self):
        try:
            q = int(input("Czy chcesz kontunuować?\nTak[1]/Nie[2]:"))
        except:
            print("Zdecyduj się")
            self.petla()
        if q == 1:
            self.wybor()
        else:
            with open("historia.txt", "r", encoding="utf-8") as plik:
                print(plik.read())
            return 



kalkulator = Kalkulator() 
#wywołuje start, zaczyna program
kalkulator.start()