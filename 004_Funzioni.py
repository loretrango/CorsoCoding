# come si scrive una funzione
# Una funzione è come un piccolo programma
# all'interno del programma.
# Potete scrivere più funzioni dentro allo stesso file,
# e le potete richiamare quando volete

def ciao():
    nome = input("Come ti chiami?: ")
    print("ciao",nome,"!!")

def somma():
    #a = 2
    #b = 3
    a = float(input("a:"))
    b = float(input("b:"))
    somma = a + b
    print(somma)

def AreaQuadrato():
    l = float(input("lato:"))
    A = l*l
    print(A)

def AreaTriangolo():
    b = float(input("base:"))
    h = float(input("Altezza:"))
    a = b*h /2
    print(a)


# Se togliete il commento richiamate la funzione
#ciao()
#somma()
#AreaQuadrato()
AreaTriangolo()  # questo richiama la funzione AreaTriangolo()