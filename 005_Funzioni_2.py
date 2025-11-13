# con import vengono importati moduli esterni (che rapresentano librerie di funzioni)
import random
###

# MENU: Esempio di come si può realizzare un menu, per scegliere cosa fare
# tra varie funzioni
def menu():
    # Stampa il menu
    print("1. Stampa i numeri da 1 a 10")
    print("2. Somma i numeri da 1 a 10")
    print("3. Tabellina del 5")
    print("4. Quadrati da 0 a 10")

    # Chiede all'utente di scegliere un'opzione
    scelta = int(input("Scegli un'opzione: "))

    # Esegue la funzione corrispondente alla scelta
    if scelta == 1:
        stampaNumeri()
    elif scelta == 2:
        sommaNumeri()
    elif scelta == 3:
        tabellina5()
    elif scelta == 4:
        quadrati()


# dice se un numero è positivo, negativo o zero
def PositivoNegativo():
    n = 0
    n = int(input("Inserisci numero: "))
    
    if n > 0:
        print("Positivo")
    elif n < 0:
        print("Negativo")
    elif n==0:
        print("Zero")

# chiede il nome e vi saluta dicendo il vostro nome
def saluta():
    nome = input("Come ti chiami? ")
    print("Ciao", nome)

'''
Scrivi un programma che chieda all'utente di inserire due numeri.
    • Stampa quale dei due numeri è maggiore.
    • Se sono uguali, stampa: "I numeri sono uguali."

    Usate int(input("Inserisci numero: ")) 
'''

# Confronta due numeri
def confronta():
    n1 = int(input("Inserisci n1: "))
    n2 = int(input("Inserisci n2: "))

    if n1 > n2:
        print(n1, "è maggiore di", n2)
    elif n1 < n2:
        print(n2, "è maggiore di", n1)
    elif n1 == n2:
        print("I due numeri sono uguali")

# Ciclo for: serv a ripeter un blocco di codice
def cicloFor():
    for i in range(10):
        print(i)

# Problema di geometria pag.101 es.14
# Un bersaglio per le freccette è fatto da cerchi concentrici
def bersaglio():
    pi = 3.14
    r9 = 1.75
    r4 = 1.75 + 5*1.7
    print("r4",r4)
    r5 = 1.75 + 4*1.7
    print("r5",r5)
    r8 = 1.75 + 1.7

    A4 = pi*r4**2
    print("A4",A4)
    A5 = pi*r5**2
    print("A5",A5)
    Ac4 = A4 - A5
    print("Ac4",Ac4)

    print("A4",A4)
    A5 = pi*r5**2
    print("A5",A5)
    Ac4 = A4 - A5
    print("Ac4",Ac4)

    A8 = pi*r8**2
    print("A8",A8)
    A9 = pi*r9**2
    print("A9",A9)
    Ac8 = A8 - A9
    print("Ac8",Ac8)

## CICLO FOR
# 1. Scrivi una funzione che stampa i numeri da 1 a 10
def stampaNumeri():
    for i in range(1,11):
        print(i)

# 2. Scrivi una funzione che somma i numeri da 1 a 10
def sommaNumeri():
    somma = 0
    for i in range(1,11):
        somma = somma + i
    print(somma)

# 3. Scrivi una funzione che che stampa tutta la tabellina del 5
def tabellina5():
    for i in range(1,11):
        print(i*5)

# 4. Scrivi una funzione che stampa i quadrati da 0 a 10
def quadrati():
    for i in range(11):
        print(i**2)

# 5. Scrivi una funzione che stampa i numeri da 1 a 10, i loro quadrati e la radice quadrata
def tavNum():
    for n in range(1,11):
        print(n,n**2,round(n**0.5,2))  # round arrotonda il numero a 2 decimali



# stampa 10 numeri casuali
def NumCasuale():
    for i in range(10):
        print(random.randint(1,100))  # randint(a,b) restituisce un numero casuale tra a e b


# una funzione che stampa tutte le tabelline da 1 a 10
def tabelline():
    for i in range(1,11):
        for j in range(1,11):
            print(i*j, end = "\t")
        print()



# superficie cilindro: calcola l'area laterale, la base e totale di un cilindro
def cilindro():
    h = 13.4
    d = 5.4

    # a) Area laterale
    C = d*3.14
    print("C", C)
    Al = C*h
    print("Al", Al)

    # b) Area della base
    r = d/2
    Ab = 3.14*r**2
    print("Ab", Ab)

    # c) Area totale
    At = 2*Ab + Al
    print("At", At)

# stessa funzione cilindro() ma con parametri
def cilindroParametri(h,d):
    # a) Area laterale
    C = d*3.14
    print("C", C)
    Al = C*h
    print("Al", Al)

    # b) Area della base
    r = d/2
    Ab = 3.14*r**2
    print("Ab", Ab)

    # c) Area totale
    At = 2*Ab + Al
    print("At", At)


# ciclo while (finchè): ripete un blocco di codice finchè una condizione è vera
# es. stampa i numeri da 1 a 10
def cicloWhile():
    n = 1
    while n<=10:
        print(n)
        n = n + 1

def SommaCasuali():
    a = random.randint(1,10)
    b = random.randint(1,10)
    somma = a + b
    
    print("a", a)
    print("b", b)
    print(a,"+", b, "=", somma)

# Quiz, somma numeri casuali e restituisci punteggio
def GiocoSommaNumeri():
    print("Gioco somma numeri")
    punteggio = 0
    num_operazioni = int(input("Digita il numero di operazioni da fare: "))
    for i in range(num_operazioni):
        a = random.randint(1,10)
        b = random.randint(1,10)
        somma = a + b
        # f-string (formatted string) permette di inserire variabili in una stringa
        # mettendo la variabile tra parentesi graffe
        print(f"{a} + {b} =") 
        risposta = int(input())
        if risposta == somma:
            punteggio = punteggio + 1
    print(f"Punteggio: {punteggio}/{num_operazioni}")

## funzione somma
def somma(a,b):
    somma = a + b
    return somma

def inserisciA():
    a = int(input("Inserisci a: "))
    return a

def inserisciB():
    b = int(input("Inserisci b: "))
    return b

a = inserisciA()
b = inserisciB()

somma = somma(a,b)
#print("Somma = ", somma)
print(f"Somma = {somma}")
# CTRL + ALT + [

##############################################
## CHIAMATE ALLE FUNZIONI
## Qui sotto ci sono le chiamate alle funzioni (se sono commentate non vengono eseguite)

#GiocoSommaNumeri()
#SommaCasuali()
#cilindro()
#PositivoNegativo()
#saluta()
#confronta()
#cicloFor()
#stampPrimiDieci()
#bersaglio()
#tavNum()
#tabelline()

##############################################
