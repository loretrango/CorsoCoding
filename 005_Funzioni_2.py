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


## CICLO FOR
# 1. Scrivi una funzione che stampa i numeri da 1 a 10
 

# 2. Scrivi una funzione che somma i numeri da 1 a 10


# 3. Scrivi una funzione che che stampa tutta la tabellina del 5


# 4. Scrivi una funzione che stampa i quadrati da 0 a 10


#PositivoNegativo()
#saluta()
#confronta()
cicloFor()
