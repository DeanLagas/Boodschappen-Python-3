from lijst import boodschappen

def menu():
    print("""1. Bekijk alle producten.

2. Voeg een product toe.

3. Verwijder een product.

4. Wijzig een product.

5. Boodschappen doen.

type 'stop' om te stoppen.""")

#hiermee toont het programma een lijst van de producten die op dat moment in de library zijn.
def toon_lijst():
    for key, value in boodschappen.items():
                print(key, value)

#hiermee kan je een product aan de library toevoegen.
def toevoegen():
    product = input("Welk product wil je toe voegen? ")
    if product in boodschappen:
        print("Sorry, maar dat is geen product.")
    else:
        prijs = input("Hoeveel kost het? ")
        try:
            prijs_as_an_integer = int(prijs)
            boodschappen[product] = int(prijs)
            print("Je product is toegevoegd.")

        except ValueError:
            print("Dat is geen nummer.")

#hiermee is het mogelijk om een al bestaand product van de library te verwijderen.
def verwijder():
    delete = input("Welk product wil je verwijderen? ")
    if delete not in boodschappen:
        print("Sorry, maar dat is geen product.")
    else:
        del boodschappen[delete]
        print("Het product is verwijderd.")

#hiermee kan je een al bestaand product van de library te wijzigen.
def wijzig():
    wijziging = True
    while wijziging:
        change = input("Welk product wil je wijzigen? ")
        if change not in boodschappen:
            print("Sorry, maar dat is geen product.")
            wijziging = False
        else:
            verander = input("Wat is de nieuwe naam? ")
            anders = input("Wat is de nieuwe prijs? ")
            try:
                anders_as_an_integer = int(anders)
                del boodschappen[change]
                boodschappen[verander] = int(anders)
                print("Het product is gewijzigd.")
                wijziging = False

            except ValueError:
                print("Dat is geen nummer.")
                wijziging = False

#hiermee kan je de producten die op dat moment in de library zitten kopen.
def boodschappen_doen():
    totaal = []
    Kopen = True
    print("type 'stop' om te stoppen.")
    while Kopen:
        koop = input("Wat wil je kopen? ")
        if koop == "stop":
            print("De totaal prijs van je boodschappen is" , sum(totaal), "euro.")
            Kopen = False
        elif koop not in boodschappen:
            print("Sorry dat is niet beschikbaar")
        else: totaal.append(boodschappen[koop])

def main():
    Run = True
    while Run:
        menu()

        start = input("Wat wil je doen? ")
        if start == "1":
            toon_lijst()
        elif start == "2":
            toevoegen()
        elif start == "3":
            verwijder()
        elif start == "4":
            wijzig()
        elif start == "5":
            boodschappen_doen()
        elif start == "stop":
            Run = False

main()
