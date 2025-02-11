## Legge di Ohm: calcolatore di corrente, tensione e resistenza

def calcola_corrente(voltaggio, resistenza):
    return voltaggio / resistenza

def calcola_voltaggio(corrente, resistenza):
    return corrente * resistenza

def calcola_resistenza(voltaggio, corrente):
    return voltaggio / corrente

def mostra_menu():
    print("\n--- Calcolatore Legge di Ohm ---")
    print("1. Calcolare l'intensità di corrente (I)")
    print("2. Calcolare la differenza di potenziale (V)")
    print("3. Calcolare la resistenza (R)")
    print("4. Uscire")

while True:
    mostra_menu()
    
    try:
        scelta = int(input("\nSeleziona un'opzione (1-4): "))
        
        if scelta == 1:
            V = float(input("Inserisci la differenza di potenziale (V) in Volt: "))
            R = float(input("Inserisci la resistenza (R) in Ohm: "))
            if R == 0:
                print("Errore: La resistenza non può essere zero!")
            else:
                I = calcola_corrente(V, R)
                print(f"L'intensità di corrente è {I:.2f} A")
        
        elif scelta == 2:
            I = float(input("Inserisci l'intensità di corrente (I) in Ampere: "))
            R = float(input("Inserisci la resistenza (R) in Ohm: "))
            V = calcola_voltaggio(I, R)
            print(f"La differenza di potenziale è {V:.2f} V")
        
        elif scelta == 3:
            V = float(input("Inserisci la differenza di potenziale (V) in Volt: "))
            I = float(input("Inserisci l'intensità di corrente (I) in Ampere: "))
            if I == 0:
                print("Errore: L'intensità di corrente non può essere zero!")
            else:
                R = calcola_resistenza(V, I)
                print(f"La resistenza è {R:.2f} Ohm")
        
        elif scelta == 4:
            print("Uscita dal programma.")
            break  # Aggiunto per terminare il loop

        else:
            print("Errore: Seleziona un'opzione valida (1-4).")

    except ValueError:
        print("Errore: Inserisci un numero valido.")