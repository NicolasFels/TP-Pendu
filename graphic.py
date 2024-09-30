'''
Nicolas FELS
30/09/2024
But: Jeu du pendu en version graphique
A faire:'''

import tkinter as tk

class Jeu():
    def __init__(self):
        self.dico = {"bjr"}
        self.chance = 8


class Fenetre():
    def __init__(self, root):
        self.nom = "Jeu du pendu"
        self.jeu = Jeu()
        root.title(self.nom)
        self.image = [tk.PhotoImage(file = f"bonhomme{i}.gif" for i in range(1,9))]
        self.canvas = tk.Canvas(root, width = self.imag[0].width(), height = self.image[0].height())
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor = "nw", image = self.image[4])
        self.input = tk.Entry()
        self.input.pack()
        self.bouton = tk.Button(root, txt = "ENTRY", command = Jeu.''(self.iput.get()))
        self.bouton.pack()


