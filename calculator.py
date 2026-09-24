print("Moj kalkulator")
liczbax = input("podaj liczbe x:")
liczbay = input("podaj liczbe y:")
try:
    int(liczbax)
    int(liczbay)
except ValueError:
    print("Nastepnym razem podaj prawidłowe liczby")
    exit()
print("wybierz działanie: dodawanie, odejmowanie, mnożenie, dzielenie")
działanie = input("wybierz działanie:")
działanie = działanie.lower().strip()
if działanie == "dodawanie":
    print("wynik dodawania to:", int(liczbax) + int(liczbay))
elif działanie == "odejmowanie":
    print("wynik odejmowania to:", int(liczbax) - int(liczbay))
elif działanie == "mnożenie":
    print("wynik mnożenie to:", int(liczbax) * int(liczbay))
elif działanie == "dzielenie":
    if int(liczbay) == 0:
        print("Nie można dzielić przez 0")
    else:
        print("wynik dzielenia to", int(liczbax) / int(liczbay))
else:
    print("Nieprawidłowe działanie")