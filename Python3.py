from lijst import boodschappen
def menu():
    print("""1. Bekijk alle producten.

2. Voeg een product toe.

3. Verwijder een product.

4. Wijzig een product.

5. Boodschappen doen.""")

def toon_lijst():
    for key, value in boodschappen.items():
                print(key, value)
def toevoegen():
    product = input("Welk product wil je toe voegen? ")
    prijs = int(input("Hoeveel kost het? "))    
    boodschappen[product] = prijs
def verwijder():
    delete = input("Welk product wil je verwijderen? ")
    del boodschappen[delete]
def wijzig():
    change = input("Welk product wil je wijzigen? ")
    verander = input("Wat is de nieuwe naam? ")
    anders = input("Wat is de nieuwe prijs? ")
    del boodschappen[change]
    boodschappen[verander] = anders
def boodschappen_doen():
    totaal = []
    Kopen = True
    while Kopen:
        koop = input("Wat wil je kopen? ")
        if koop == "stop":
            print("De totaal prijs van je boodschappen is" , sum(totaal), "euro.")
            Kopen = False
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
