class Kalkulator:
    def __init__(self):
        self.history = []

    def dodawanie(self, a, b):
        result = a + b

        calculation = f"{a} + {b} = {result}"
        self.history.append(calculation)
        return result

    def odejmowanie(self, a, b):
        result = a - b

        calculation = f"{a} - {b} = {result}"
        self.history.append(calculation)
        return result 

    def mnożenie(self, a, b):
        result = a * b
    
        calculation = f"{a} * {b} = {result}"
        self.history.append(calculation)
        return result 

    def dzielenie(self, a, b):
        try:
            result = a / b
        except ValueError:
            print("Nastepnym razem podaj prawidłowe liczby")
        calculation = f"{a} / {b} = {result}"
        self.history.append(calculation)
        return result


    def pokaz_historie(self):
        for calculation in self.history:
            print(calculation)


kalkulator = Kalkulator() 

kalkulator.dodawanie(5, 3)
kalkulator.dodawanie(2, 10)

kalkulator.pokaz_historie()
print(kalkulator.history)


        