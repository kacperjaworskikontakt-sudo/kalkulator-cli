print("Moj kalkulator")
liczbax = input("podaj liczbe x:")
liczbay = input("podaj liczbe y:")
try:
    int(liczbax)
    int(liczbay)
except ValueError:
    print("podaj prawidłowe liczby")
    exit()
print("wybierz działanie: dodawanie, odejmowanie")
działanie = input("wybierz działanie:")
działanie = działanie.lower()
działanie = działanie.strip()
if działanie == "dodawanie":
    print("wynik dodawania to:", int(liczbax) + int(liczbay))
elif działanie == "odejmowanie":
    print("wynik odejmowania to:", int(liczbax) - int(liczbay))
