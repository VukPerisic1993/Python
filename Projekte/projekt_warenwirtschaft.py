# MODUL 1: Eingabe der Artikelnummer mit fehler abfangen
def artikelnummer_eingabe():
    artikelnummer = int(input("Geben Sie die Artikelnummer ein: Drücke (0) zum beende! \n"))
    while artikelnummer != 0:
        try:
            if artikelnummer == 17:
                einzelpreis = 2.20
            elif artikelnummer == 22:
                einzelpreis = 24.50
            elif artikelnummer == 38:
                einzelpreis = 15.00
            elif artikelnummer == 47:
                einzelpreis = 9.95
            elif artikelnummer == 125:
                einzelpreis = 12.95
            else:
                raise ValueError("Falsche Eingabe, nur Artikelnummer 17, 22, 38, 47, 125 dürfen eingegeben werden")
        except ValueError:
            print("Falsche Eingabe!")
            
# MODUL 2: Eingabe der Menge
def menge_eingabe():
    menge = int(input("Geben Sie die gewünschte Menge ein: \n"))
    while menge > 0:
        try:
            if menge <= 0:
                print("Ungültige Eingabe, Menge muss positiv sein!")
        except ValueError:
            print("Die Eingabe muss eine Zahl sein!")
    print(menge, "Artikel wurde(n) hinzugefügt!")
    
# MODUL 3: ermitteln des Preises
def preis_ermittlung():
    gesamtrechnungssumme = 0
    artikelgesamtpreis = 0
    menge*einzepreis = artikelgesamtpreis
    
    