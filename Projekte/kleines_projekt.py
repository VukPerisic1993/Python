#Begrüßung + Name abfragen
name = (input("Wie heißt du? "))
print("Wilkommen",name,"!")

#Operation wählen
print("Welche Operation möchtest du durchführen?") 
print("1 = Addition")
print("2 = Subtraktion")
print("3 = Multiplikation")
print("4 = Division")

auswahl = input("Wähle eine Operation aus (1/2/3/4): ")
if auswahl != 1:
    print("Zahl ist ungültig! 1-4 ist erlaubt.")
elif auswahl != 2:
    print("Zahl ist ungültig! 1-4 ist erlaubt.")
elif auswahl != 3:
    print("Zahl ist ungültig! 1-4 ist erlaubt.")
elif auswahl != 4:
    print("Zahl ist ungültig! 1-4 ist erlaubt.")

auswahl = input("Wähle eine Operation aus (1/2/3/4): ")

#Zahlen abfragen
zahl1 = float(input("Gib die erste Zahl ein: "))
zahl2 = float(input("Gib deine zweite Zahl ein: "))

#Berechnung und Logik
if auswahl == "1":
    ergebnis = zahl1 + zahl2
    print(ergebnis)

elif auswahl == "2":
    ergebnis = zahl1 - zahl2
    print(ergebnis)

elif auswahl == "3":
    ergebnis = zahl1 * zahl2
    print(ergebnis)

elif auswahl == "4":
    if zahl2 == 0:
        print("Division durch 0 nicht erlaubt!")

elif auswahl == "4":
    ergebnis = zahl1 / zahl2
    print(ergebnis)

else:
    print("Ungültige Eingabe")

