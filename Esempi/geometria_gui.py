import tkinter as tk
from tkinter import messagebox

def AreaRettangoloParallelogramma(base, altezza):
    return base * altezza

def AreaQuadrato(lato):
    return lato ** 2

def AreaTrapezio(baseMagg, baseMin, altezza):
    return (baseMagg + baseMin) * altezza / 2

def AreaRombo(diaMagg, diaMin):
    return diaMagg * diaMin / 2

def calcola_area():
    figura = figura_var.get()

    try:
        if figura == "Quadrato":
            lato = float(entry_vars[0].get())
            area = AreaQuadrato(lato)
        elif figura == "Rettangolo o Parallelogramma":
            base = float(entry_vars[0].get())
            altezza = float(entry_vars[1].get())
            area = AreaRettangoloParallelogramma(base, altezza)
        elif figura == "Trapezio":
            baseMagg = float(entry_vars[0].get())
            baseMin = float(entry_vars[1].get())
            altezza = float(entry_vars[2].get())
            area = AreaTrapezio(baseMagg, baseMin, altezza)
        elif figura == "Rombo":
            diaMagg = float(entry_vars[0].get())
            diaMin = float(entry_vars[1].get())
            area = AreaRombo(diaMagg, diaMin)
        else:
            messagebox.showerror("Errore", "Seleziona una figura geometrica.")
            return

        messagebox.showinfo("Risultato", f"L'area è: {area}")
    except ValueError:
        messagebox.showerror("Errore", "Inserisci valori numerici validi.")

def aggiorna_input():
    figura = figura_var.get()

    for widget in input_frame.winfo_children():
        widget.destroy()

    entry_vars.clear()

    if figura == "Quadrato":
        tk.Label(input_frame, text="Lato:").grid(row=0, column=0)
        var = tk.StringVar()
        entry_vars.append(var)
        tk.Entry(input_frame, textvariable=var).grid(row=0, column=1)
    elif figura == "Rettangolo o Parallelogramma":
        tk.Label(input_frame, text="Base:").grid(row=0, column=0)
        tk.Label(input_frame, text="Altezza:").grid(row=1, column=0)
        for i in range(2):
            var = tk.StringVar()
            entry_vars.append(var)
            tk.Entry(input_frame, textvariable=var).grid(row=i, column=1)
    elif figura == "Trapezio":
        tk.Label(input_frame, text="Base Maggiore:").grid(row=0, column=0)
        tk.Label(input_frame, text="Base Minore:").grid(row=1, column=0)
        tk.Label(input_frame, text="Altezza:").grid(row=2, column=0)
        for i in range(3):
            var = tk.StringVar()
            entry_vars.append(var)
            tk.Entry(input_frame, textvariable=var).grid(row=i, column=1)
    elif figura == "Rombo":
        tk.Label(input_frame, text="Diagonale Maggiore:").grid(row=0, column=0)
        tk.Label(input_frame, text="Diagonale Minore:").grid(row=1, column=0)
        for i in range(2):
            var = tk.StringVar()
            entry_vars.append(var)
            tk.Entry(input_frame, textvariable=var).grid(row=i, column=1)

# Creazione della finestra principale
root = tk.Tk()
root.title("Calcolo delle Aree")

# Selezione della figura geometrica
figura_var = tk.StringVar(value="Seleziona")
tk.Label(root, text="Seleziona la figura geometrica:").pack()
figura_menu = tk.OptionMenu(root, figura_var, "Quadrato", "Rettangolo o Parallelogramma", "Trapezio", "Rombo", command=lambda _: aggiorna_input())
figura_menu.pack()

# Frame per i campi di input
input_frame = tk.Frame(root)
input_frame.pack()

entry_vars = []  # Lista per contenere le variabili associate agli entry

# Bottone per calcolare l'area
tk.Button(root, text="Calcola Area", command=calcola_area).pack()

# Avvio dell'applicazione
root.mainloop()

