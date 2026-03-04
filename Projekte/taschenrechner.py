while True:
    print("\n--------------")
    print("Taschenrechner")
    print("--------------\n")
    print("1 ... Adition")
    print("2 ... Subtraktion")
    print("3 ... Multiplikation")
    print("4 ... Division")
    print("0 ... Programmende")

    try:
        user_input = int(input("\nBitte Rechnerart (1-4) wählen oder 0 für Programmende: "))
        print(f"Du hast dich für Option {user_input} entschieden.")
    except ValueError:
        print("Keine gültige Eingabe! Bitte eine Zahl 0-4 eingeben.")
        continue
    
    if user_input == 0:
        print("Programm beendet")
        break
    
    if user_input < 1 or user_input > 4:
        print(f"Die Option {user_input} gibt es nicht. Bitte nur Zahlen 0-4 eingeben!")
        continue
        
    while True: 
        try: 
            number1 = float(input("Bitte geben Sie die erste Zahl ein: "))
            break
        except ValueError:
            print("Keine gültige eingabe! Es sind nur Zahlen erlaubt. Bitte geben Sie eine gültige erste Zahl ein.")
            
    while True: 
        try: 
            number2 = float(input("Bitte geben Sie die zweite Zahl ein: "))
            break
        except ValueError:
            print("Keine gültige eingabe! Es sind nur Zahlen erlaubt. Bitte geben Sie eine gültige zweite Zahl ein.")

    if user_input == 1:
        result = number1 + number2
        print(f"Das Ergebnis deiner Addition ist {result}.")
    elif user_input == 2:
        result = number1 - number2
        print(f"Das Ergebnis deiner Subtraktion ist {result}.")
    elif user_input == 3:
        result = number1 * number2
        print(f"Das Ergebnis deiner Multiplikation ist {result}.")
    elif user_input == 4:
        if number2 != 0:
            result = number1 / number2
            print(f"Das Ergebnis deiner Division ist {result}.")
        else:
            print("Fehler: Division durch 0 nicht erlaubt!")
    else:
        print("Ungültige Eingabe! Bitte versuche es erneut.")
        
