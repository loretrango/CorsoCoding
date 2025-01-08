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

PositivoNegativo()
saluta()