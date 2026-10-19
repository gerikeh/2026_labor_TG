import tkinter as tk
from tkinter import ttk
import random

root = tk.Tk()
root.title("Kockázás")
root.geometry("600x400")
# root.minsize(500, 300)
# root.maxsize(800, 500)
# root.resizable(False, False)


def dobas():
    try:
        db = int(dobas_szam.get())
        if db < 1:
            raise ValueError
    except ValueError:
        eredmeny_cimke.config(text="Adj meg egy pozitív egész számot!")
        return

    dobasok = [random.randint(1, 6) for _ in range(db)]
    eredmeny_cimke.config(
        text=f"Dobások: {', '.join(map(str, dobasok))}\nÖsszeg: {sum(dobasok)}"
    )


cim_cimke = ttk.Label(root, text='Kockajáték', font='Arial 16 bold')
cim_cimke.pack(pady=10)

dobas_szam = tk.StringVar(value="10")
dobas_szam_be = ttk.Entry(root, textvariable=dobas_szam, width=10)
dobas_szam_be.pack(pady=5)

dobas_gomb = ttk.Button(root, text='Dobás', command=dobas)
dobas_gomb.pack(pady=5)

eredmeny_cimke = ttk.Label(root, text='', wraplength=550, justify='center')
eredmeny_cimke.pack(pady=10)

kilepes_gomb = ttk.Button(root, text='Kilépés', command=root.destroy)
kilepes_gomb.pack(pady=5)

root.mainloop()