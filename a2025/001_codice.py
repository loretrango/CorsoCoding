# esempio di codice
# come si stampa qualcosa a video
print("Ciao, mondo!") # ciao mondo

# Definizione di una Funzione
# come si scrive e come si richiama una funzione
# E' come uno strumento che possiamo riutilizzare
# Perché definire una funzione? Per organizzare meglio il codice, per
# evitare di riscrivere più volte lo stesso codice, per rendere il codice
# più leggibile
def saluta():
    print("Ciao!") # ciao

saluta()


# come si sommano due numeri
def somma_due_numeri():
    a = 5
    b = 7
    somma = a + b
    print("La somma di", a, "e", b, "è", somma) # la somma di 5 e 7 è 12

# come si fanno tutte le altre operazioni aritmetiche
def altre_operazioni():
    a = 5
    b = 7
    differenza = b - a
    prodotto = a * b
    quoziente = b / a
    print("Differenza:", differenza) # differenza: 2
    print("Prodotto:", prodotto)  # prodotto: 35
    print("Quoziente:", quoziente)    # quoziente: 1.4

# come si accetta un input dall'utente
def accetta_input():
    """
    Prompts the user to enter their name and prints a greeting message.

    This function asks the user for their name via standard input and then displays a greeting using the provided name.
    """
    nome = input("Come ti chiami? ")
    print("Ciao", nome) 

# quando si accetta un input con solo la funzione input(), il valore è sempre una stringa
# per convertire una stringa in un numero intero, si usa la funzione int()
def somma_input_utente():
    a = int(input("Inserisci un numero intero: "))
    b = int(input("Inserisci un altro numero intero: "))
    somma = a + b
    print("La somma di", a, "e", b, "è", somma) # la somma di X e Y è Z

def somma_input_utente_float():
    a = float(input("Inserisci un numero decimale: "))
    b = float(input("Inserisci un altro numero decimale: "))
    somma = a + b   
    print("La somma di", a, "e", b, "è", somma) # la somma di X e Y è Z

# esempoio ciclo for fatto in classe, con le potenze
def stampa_potenze_di_2():
    for esponente in range(1, 21):
        print("esponente: ", esponente, "potenza di 2: ", 2**esponente)

# codici relativi all'apprendimento delle potenze
def calcola_potenza():
    base = int(input("Inserisci la base: "))
    esponente = int(input("Inserisci l'esponente: "))
    potenza = base ** esponente
    print(base, "elevato alla potenza di", esponente, "è", potenza)

#calcola_potenza()


# crea un gioco a punti per fare operaizoni con le potenze con numeri casualiimport random
import random
def gioco_potenze():
    punti = 0
    for i in range(5):
        base = random.randint(1, 5)
        esponente = random.randint(1, 3)
        risposta_corretta = base ** esponente
        risposta_utente = int(input(f"Quanto fa {base} elevato alla potenza di {esponente}? "))
        if risposta_utente == risposta_corretta:
            print("Risposta corretta!")
            punti += 1
        else:
            print(f"Risposta sbagliata! La risposta corretta è {risposta_corretta}.")
    print(f"Hai totalizzato {punti} punti su 5.")   

#gioco_potenze()

b