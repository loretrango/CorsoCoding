''' 
CALCOLO DELLE AREE 
Esempio di programma che permette di calcolare le aree
dati alcuni valori. La figura geometrica viene scelta
attraverso un menu di scelta.
Sono state definite delle funzioni per calolare le aree
delle figure, e per inserire i dati.
Definire delle funzioni con dei parametri, permette di 
rendere più riutilizzabile il codice.
'''

# Queste funzioni calcolano il valore delle aree e ritornano il valore
def AreaRettangoloParallelogramma(base, altezza):  # necessitano dei parametri "base" e "altezza"
    area = base*altezza  # calcola l'area
    #print(area)
    return area  # restituisce il valore "area"

def AreaQuadrato(lato):
    area = lato**2
    #print(area)
    return area

def AreaTrapezio(baseMagg, baseMin, altezza):
    area = (baseMagg+baseMin)*altezza/2
    #print(area)
    return area

def AreaRombo(diaMagg, diaMin):
    area = diaMagg*diaMin/2
    #print(area)
    return area


# Stampa il valore dell'area
def stampa(area):  # la funzione necessita del parametro "area"
    print("Area è = ", area)


# Queste funzioni gestiscono gli input e ritornano il valore inserito
def inputLato():
    lato = float(input("Inserisci la lato: "))  # accetta l'input
    return lato  # ritorna il contenuto della variabile "lato"

def inputBase():
    base = float(input("Inserisci la base: "))
    return base

def inputAltezza():
    altezza = float(input("Inserisci l'altezza: "))
    return altezza

def inputBaseMagg():
    baseMagg = float(input("Inserisci la base maggiore: "))
    return baseMagg

def inputBaseMin():
    baseMin = float(input("Inserisci la base minore: "))
    return baseMin

def inputDiaMagg():
    diaMagg = float(input("Inserisci la diagonale maggiore: "))
    return diaMagg

def inputDiaMin():
    diaMin = float(input("Inserisci la diagonale minore: "))
    return diaMin


# Questo menu permette di scegliere tra le varie figure
# Stampa il menu
def menu():
    print()
    print("PROGRAMMA PER IL CALOLO DELLE AREE\nDELLE FIGURE PIANE")
    print()
    print("Fare una scelta dal seguente menu (digitare il numero)")
    print("1 - Area quadrato")
    print("2 - Area rettangolo o  parallelogramma")
    print("3 - Area trapezio")
    print("4 - Area rombo")

    # Aspetta l'input della scelta e lo inserisce nella variabile "scelta"
    # L'utente deve inserire un numero
    scelta = None  # inizializza la variabile con un valore vuoto "None"
    
    # il ciclo while continua finche non è stata fatta una scelta corretta

    scelta = input("Fai una scelta: ")
        
    while scelta not in ["1","2","3","4"]:  # continua se la scelta non è tra questi valori
        scelta = input("Valore inserito non corretto, riprova: ")
    
    print()
    # In base alla scelta fatta attiva la funzione giusta
    if scelta == "1":
        lato = inputLato()
        area = AreaQuadrato(lato)
        stampa(area)
    elif scelta == "2":
        base = inputBase()
        altezza = inputAltezza()
        area = AreaRettangoloParallelogramma(base, altezza)
        stampa(area)
    elif scelta == "3":
        baseMagg = inputBaseMagg()
        baseMin = inputBaseMin()
        altezza = inputAltezza()
        area = AreaTrapezio(baseMagg,baseMin,altezza)
        stampa(area)
    elif scelta == "4":
        diaMagg = inputDiaMagg()
        diaMin = inputDiaMin()
        area = AreaRombo(diaMagg, diaMin)
        stampa(area)

# esegue la funzione menu() dalla quale parte il programma
menu()  