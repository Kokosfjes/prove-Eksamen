# 2.1 Lister og søk

navn = ["Sebastian", "Montadar", "Susanna", "Sivert", "Sondre", "Bror", "Ludvig"]

while True:
    print("\n1) Vis deltakere")
    print("2) Søk etter deltaker")
    print("3) Avslutt")
    valg = input("Velg: ")

    if valg == "1":
        for n in sorted(navn):
            print(n)
    elif valg == "2":
        sok = input("Skriv navn: ")
        if sok in navn:
            print(sok, "finnes i lista")
        else:
            print(sok, "finnes ikke i lista")
    elif valg == "3":
        break
    else:
        print("Ugyldig valg")
