''' 
Calcolo figure geometriche
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

## Cerchio

def AreaCerchio(raggio):
    area = raggio**2*3.14
    return area

# Calcola la circonferenza del cerchio dal raggio
def Circonfrenza(raggio):    
    C = raggio*2*3.14
    return C

# Calcola la circonferenza del cerchio dal diametro
def CirconfrenzaDiametro(diametro):    
    C = diametro*3.14
    return C

# Dall'area del cerchio al raggio:
def DaAreaRaggioCerchio(area):
    raggio = (area/3.14)**(1/2)
    return raggio

# Dalla circonferenza al raggio:
def DaCirconferenzaRaggio(circonferenza):
    raggio = circonferenza/(2*3.14)
    return raggio

# Stampa il valore dell'area
def stampa(area):  # la funzione necessita del parametro "area"
    print("Area è = ", area)

######################################################################
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

def inputRaggio():
    raggio = float(input("Inserisci il raggio: "))
    return raggio

def inputDiametro():
    diametro = float(input("Inserisci il diametro: "))
    return diametro

# Questo menu permette di scegliere tra le varie figure
# Stampa il menu
def menu():
    while True:
        print()
        print("PROGRAMMA PER IL CALOLO DELLE AREE\nDELLE FIGURE PIANE")
        print("- premi INVIO per continuare")
        print("- premi 'e' per uscire")
        print()
        if input(": ") == "e":
            break

        print()
        print()
        print("Fare una scelta dal seguente menu (digitare il numero)")
        print("1 - Area quadrato")
        print("2 - Area rettangolo o  parallelogramma")
        print("3 - Area trapezio")
        print("4 - Area rombo")
        print("6 - Area cerchio")
        print("7 - Circonferenza cerchio dal raggio")
        print("8 - Circonferenza cerchio dal diametro")
        print("9 - Raggio dall'area del cerchio")
        print("10 - Raggio dalla circonferenza del cerchio")  
        print("e - per uscire")
        print()

        # Aspetta l'input della scelta e lo inserisce nella variabile "scelta"
        # L'utente deve inserire un numero
        scelta = None  # inizializza la variabile con un valore vuoto "None"
        
        # il ciclo while continua finche non è stata fatta una scelta corretta

        scelta = input("Fai una scelta: ")
            
        while scelta not in ["1","2","3","4","6","7","8","9","10","e"]:  # continua se la scelta non è tra questi valori
            scelta = input("Valore inserito non corretto, riprova: ")
        
        print()
        # In base alla scelta fatta attiva la funzione giusta
        if scelta == "1":
            print("Area quadrato")
            lato = inputLato()
            area = AreaQuadrato(lato)
            stampa(area)
        elif scelta == "2":
            print("Area rettangolo o parallelogramma")
            base = inputBase()
            altezza = inputAltezza()
            area = AreaRettangoloParallelogramma(base, altezza)
            stampa(area)
        elif scelta == "3":
            print("Area trapezio")
            baseMagg = inputBaseMagg()
            baseMin = inputBaseMin()
            altezza = inputAltezza()
            area = AreaTrapezio(baseMagg,baseMin,altezza)
            stampa(area)
        elif scelta == "4":
            print("Area rombo")
            diaMagg = inputDiaMagg()
            diaMin = inputDiaMin()
            area = AreaRombo(diaMagg, diaMin)
            stampa(area)
        elif scelta == "6":
            print("Area cerchio")
            raggio = inputRaggio()
            area = AreaCerchio(raggio)
            stampa(area)
        elif scelta == "7":
            print("Circonferenza cerchio dal raggio")
            raggio = inputRaggio()
            C = Circonfrenza(raggio)
            print("Circonferenza = ", C)
        elif scelta == "8":
            print("Circonferenza cerchio dal diametro")
            diametro = inputDiametro()
            C = CirconfrenzaDiametro(diametro)
            print("Circonferenza = ", C)
        elif scelta == "9":
            print("Raggio dall'area del cerchio")
            area = float(input("Inserisci l'area: "))
            raggio = DaAreaRaggioCerchio(area)
            print("Raggio = ", raggio)   
        elif scelta == "10":
            print("Raggio dalla circonferenza del cerchio")
            circonferenza = float(input("Inserisci la circonferenza: "))
            raggio = DaCirconferenzaRaggio(circonferenza)
            print("Raggio = ", raggio)     
        elif scelta == "e":
            break

# Finestra di tkinter per la scelta della figura
'''def finestra():
    import tkinter as tk
    from tkinter import messagebox
    # Funzioni per il calcolo delle aree
    def area_quadrato():
        lato = float(entry.get())
        area = AreaQuadrato(lato)
        messagebox.showinfo("Area quadrato", "Area = "+str(area))
'''
#finestra()

# esegue la funzione menu() dalla quale parte il programma
menu()  