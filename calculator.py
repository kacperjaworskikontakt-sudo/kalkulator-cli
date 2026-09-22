print("Moj kalkulator")
liczbax = input("podaj liczbe x:")
liczbay = input("podaj liczbe y:")
print("wybierz działanie: dodawanie, odejmowanie")
działanie = input("wybierz działanie:")
if działanie == "dodawanie":
    print("wynik dodawania to:", int(liczbax) + int(liczbay))
elif działanie == "odejmowanie":
    print("wynik odejmowania to:", int(liczbax) - int(liczbay))
print("test")