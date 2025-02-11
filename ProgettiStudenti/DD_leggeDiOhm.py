## Legge di Ohm: calcolatore di corrente, tensione e resistenza

def intensita():
   T = int(input("Scrivi qua la Tensione: "))
   if T == 0:
    print("Amico, questo numero non puoi scriverlo!!")
    T = int(input("Scrivi qua la Tensione: "))
   print(" ")
   R = int(input("Scrivi qua la Resistenza: "))
   if R == 0:
    print("Amico, questo numero non puoi scriverlo!!")
    R = int(input("Scrivi qua la Resistenza"))
   I = T / R
   print(" ")
   print("Ecco tutti i dati:")
   print(" ")
   print("Questa è la Tensione:", T)
   print(" ")
   print("Questa è la Resistenza:", R)
   print(" ")
   print("Infine, questa è l'Intensità:", I)
   print(" ")

   continuare()

def tensione():
   I = int(input("Scrivi qua l'Intensità: "))
   if I == 0:
    print("Amico, questo numero non puoi scriverlo!!")
    R = int(input("Scrivi qua l'Intensità: "))
   print(" ")
   R = int(input("Scrivi qua la Resistenza: "))
   if R == 0:
    print("Amico, questo numero non puoi scriverlo!!")
    R = int(input("Scrivi qua la Resistenza"))
   T = I / R
   print(" ")
   print("Ecco tutti i dati:")
   print(" ")
   print("Questa è l'Intensità:", I)
   print(" ")
   print("Questa è la Resistenza:", R)
   print(" ")
   print("Infine, questa è la Tensione:", T)
   print(" ")
   
   continuare()

def resistenza():
   T = int(input("Scrivi qua la Tensione: "))
   if T == 0:
    print("Amico, questo numero non puoi scriverlo!!")
    I = int(input("Scrivi qua la Tensione: "))
   print(" ")
   I = int(input("Scrivi qua l'Intensità: "))
   if I == 0:
    print("Amico, questo numero non puoi scriverlo!!")
    R = int(input("Scrivi qua l'Intensità"))
   R = T/I
   print(" ")
   print("Ecco tutti i dati:")
   print(" ")
   print("Questa è la Tensione:", T)
   print(" ")
   print("Questa è l'Intensità:", I)
   print(" ")
   print("Infine, questa è la Resistenza:", R)
   print(" ")

   continuare()

def Legge():

 print ("  ██╗    ███████╗ ██████╗  ██████╗ ███████╗    ██████╗ ██╗     ██████╗ ██╗  ██╗███╗   ███╗██╗")
 print("  ██║    ██╔════╝██╔════╝ ██╔════╝ ██╔════╝    ██╔══██╗██║    ██╔═══██╗██║  ██║████╗ ████║██║")
 print("  ██║    █████╗  ██║  ███╗██║  ███╗█████╗      ██║  ██║██║    ██║   ██║███████║██╔████╔██║██║")
 print("  ██║    ██╔══╝  ██║   ██║██║   ██║██╔══╝      ██║  ██║██║    ██║   ██║██╔══██║██║╚██╔╝██║╚═╝")
 print ("  ██████╗███████╗╚██████╔╝╚██████╔╝███████╗    ██████╔╝██║    ╚██████╔╝██║  ██║██║ ╚═╝ ██║██╗")
 print("  ══════╝╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝    ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝") 

 print(" ")
 print("______________________________________________________________________________________________________")
 print(" ")
 print("Ciao! sono Ohmmino! E oggi ti aiuto a calcolare la Legge di Ohm!!")
 print(" ")
 print("Allora, devi sapere che la legge di Ohm è una legge che aiuta a misurare l'Intensità, la Tensione e la Resistenza della corrente elettrica. Le unità di misura sono:")
 print("- Amper(A) per l'Intensità")
 print("- I Volt(V) per la Tensione")
 print("- Gli Ohm(Ω)per la Resistenza")
 print(" ")
 print(" ")
 print(" Ora che sai tutto, scegli il calcolo che vuoi fare!!")
 print(" ")
 print("1.Calcolare l'Intensità")
 print("2.Calcolare la Tensione")
 print("3.Calcolare la Resistenza")
 print(" ")
 print("Sicuramente ti starai chiedendo come si fanno questi calcoli, infatti eccomi qua!")
 print(" ")
 print("Per calcolare l'intensità, bisogna fare Tensione fratto Resistenz a[T/R]")
 print(" ")
 print("Invece, per calcolare la Tensione bisogna fare Intensità per Resistenza [IxR]")
 print(" ")
 print("Infine, per calcolare la Resistenza, bisogna fare Tensione fratto Intensità [T/I]")
  
 scelta =int( input("Scrivi il numero!: "))
 
 if scelta == 1:
   intensita()
 elif scelta == 2:
   tensione()
 elif scelta ==3:
   resistenza()
 else:
    print("Amico, questa scelta non è disponibile!!")
    print(" ")
    print("scegli il calcolo che vuoi fare!!")
    print(" ")
    print("1.Calcolare l'Intensità")
    print("2.Calcolare la Tensione")
    print("3.Calcolare la Resistenza")
    print(" ")
    scelta =int( input("Scrivi il numero!: "))

def continuare():
  
    print("Finito, vuoi continuare a farne altri?")
    print("1.Si")
    print("2.No")
    H = int(input("Vuoi continuare?: "))

    if H == 1:
        Legge()

    elif H == 2:
        print("Ok, Arrivederci!!!")
        print(" ")

    else:
        print("Amico, questa risposta non è valida!!")
        H =int(input("Vuoi continuare a fare altri calcoli?: "))
    if H == 1:
      Legge()

    elif H == 2:
     print("Ok, Arrivederci!!!")
    print(" ")

Legge()