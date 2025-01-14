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

bersaglio()
## CICLO FOR
# 1. Scrivi una funzione che stampa i numeri da 1 a 10


# 2. Scrivi una funzione che somma i numeri da 1 a 10


# 3. Scrivi una funzione che che stampa tutta la tabellina del 5


# 4. Scrivi una funzione che stampa i quadrati da 0 a 10

def tavNum():
    for n in range(1,11):
        print(n,n**2,round(n**0.5,2))

tavNum()

def menu():
    print("1. Stampa i numeri da 1 a 10")
    print("2. Somma i numeri da 1 a 10")
    print("3. Tabellina del 5")
    print("4. Quadrati da 0 a 10")
    scelta = int(input("Scegli un'opzione: "))
    if scelta == 1:
        stampaNumeri()
    elif scelta == 2:
        sommaNumeri()
    elif scelta == 3:
        tabellina5()
    elif scelta == 4:
        quadrati()



#PositivoNegativo()
#saluta()
#confronta()
#cicloFor()
#stampPrimiDieci()

