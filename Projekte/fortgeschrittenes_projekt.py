#Teil A: Start & Eingaben

name = input("Wie heißen Sie? \n")
print("Wilkommen, ", name ,"!")

budget_eingabe = input("Wie hoch ist das verfügbare Budget?\n")
budget = float(budget_eingabe)

#Variable für die Gesamtsumme
zwischensumme = 0.0

#Teil B: Artikel erfassen
print("Bitte gib jetzt 3 Artikel ein: \n")

#Artikel 1
art1_name = input("Artikel 1: \n")
art1_preis = float(input("Stückpreis für " + art1_name + ": "))
art1_menge = int(input("Menge für " + art1_name + ": "))
pos1_preis = art1_preis * art1_menge
zwischensumme = zwischensumme + pos1_preis
print(zwischensumme)

#Artikel 2
art2_name = input("Artikel 2: \n")
art2_preis = float(input("Stückpreis für " + art2_name + ": "))
art2_menge = int(input("Menge für " + art2_name + ": "))
pos2_preis = art2_preis * art2_menge
zwischensumme = zwischensumme + pos2_preis
print(zwischensumme)

#Artikel 3
art3_name = input("Artikel 3: \n")
art3_preis = float(input("Stückpreis für " + art3_name + ": "))
art3_menge = int(input("Menge für " + art3_name + ": "))
pos3_preis = art3_preis * art3_menge
zwischensumme = zwischensumme + pos3_preis
print(zwischensumme)

print("Hinzugefügt: " , art1_name , art2_name , art3_name)

#Teil C: Rabatt auswählen
print("Wählen eine Rabattart: ")
print("0= Kein Rabatt")
print("1 = Student (10%)")
print("2 = VIP (15%)")
print("3 = Gutschein (5€)")

rabatt_wahl = input("Deine Wahl: \n")
rabatt_betrag = 0.0

if rabatt_wahl == "1":
    rabatt_betrag = zwischensumme*0.10

elif rabatt_wahl == "2":
    rabatt_betrag = zwischensumme*0.15

elif rabatt_wahl == "3":
    if zwischensumme >= 20:
        rabatt_betrag = 5.0
    else:
        print("Gutschein wird nicht angewendet (Zwischensumme < 20€).")
    
else:
    rabatt_betrag = 0.0

endpreis = zwischensumme - rabatt_betrag

#Abschlussrechnung
print("--- QUITTUNG ---")
print("Zwischensumme: " , zwischensumme , "€")
print("Rabatt: " , rabatt_betrag , "€")
print("Endpreis: " , endpreis , "€")

if endpreis > budget:
    print("Dein Budget von " , budget , "€ wurde überschritten")

      