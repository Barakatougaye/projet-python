# Importer les bibliothèques 
import tkinter as tk
from tkinter import messagebox

# Créer la fenêtre principale avec le titre "TIC-TAC-TOE"
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Définir la taille de la fenêtre
root.geometry("400x450")
root.resizable(False, False)

#Définir la liste
chiffres = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#- Initialiser la variable
mark = ''

#- la variable de comptage
count = 0

#- Liste appelée panneau avec 10 elements
panneaux = ['panneau', 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Styles - avec des couleurs 
btn_font = ('Helvetica', 24, 'bold')
label_font = ('Helvetica', 16, 'bold')
button_bg = '#282828'  # Fond gris foncé pour les boutons
button_fg = '#FFCC00'  # Texte jaune pour les boutons
button_active_bg = '#444444'  # Couleur active un peu plus claire
label_color = '#FFCC00'  # Texte jaune pour l'étiquette
bg_color = '#1c1c1c'  # Fond noir/gris foncé pour la fenêtre

# Changer la couleur de fond de la fenêtre
root.configure(bg=bg_color)

# Fonction pour vérifier le gagnant
def win(mark):
    # Combinaisons gagnantes
    winning_combinations = [
        [1, 2, 3],  # Ligne 1
        [4, 5, 6],  # Ligne 2
        [7, 8, 9],  # Ligne 3
        [1, 4, 7],  # Colonne 1
        [2, 5, 8],  # Colonne 2
        [3, 6, 9],  # Colonne 3
        [1, 5, 9],  # Diagonale
        [3, 5, 7]   # Diagonale
    ]
    return any(all(panneaux[i] == mark for i in combo) for combo in winning_combinations)


# Fonction pour gérer les clics sur les boutons
def verifier(chiffre, bouton):
    global count, mark, chiffres, panneaux

    if chiffre in chiffres:
        # Mettre à jour le plateau et désactiver le bouton
        panneaux[chiffre] = mark
        bouton.config(text=mark, state="disabled", disabledforeground=button_fg)
        chiffres.remove(chiffre)

        # Vérifier si un joueur a gagné
        if win(mark):
            messagebox.showinfo("Fin du jeu", f"Le joueur {'1' if mark == 'X' else '2'} gagne !")
            root.destroy()
        else:
            count += 1  # Augmenter le compteur de mouvements
            if count >= 9:  # Si tous les mouvements sont effectués
                messagebox.showinfo("Fin du jeu", "Match à égalité.")
                root.destroy()
            else:
                # Alterner entre les joueurs X et O
                mark = 'O' if mark == 'X' else 'X'
                label_joueur.config(text=f"Joueur actuel : {mark}")
    else:
        print("Sélection invalide.")

# Création des boutons pour le plateau de jeu
buttons = []
for i in range(1, 10):
    bouton = tk.Button(root, text="", width=5, height=2, font=btn_font,
                       bg=button_bg, fg=button_fg, activebackground=button_active_bg,
                       activeforeground=button_fg, command=lambda i=i: verifier(i, buttons[i-1]))
    buttons.append(bouton)

# Placement des boutons dans une grille 
for i in range(3):
    for j in range(3):
        buttons[i * 3 + j].grid(row=i, column=j, padx=10, pady=10)

# Étiquette pour afficher le joueur actuel
label_joueur = tk.Label(root, text="Joueur actuel : X", font=label_font, bg=bg_color, fg=label_color)
label_joueur.grid(row=3, column=0, columnspan=3, pady=20)

# Le joueur "X" commence
mark = 'X'

# Lancer la fenêtre principale
root.mainloop()
