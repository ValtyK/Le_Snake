import time
import curses

# affichage du titre
titre =['  _______     _________ _    _  ____  _   _    _____ _   _          _  ________ ',
        ' |  __ \ \   / |__   __| |  | |/ __ \| \ | |  / ____| \ | |   /\   | |/ |  ____|',
        ' | |__) \ \_/ /   | |  | |__| | |  | |  \| | | (___ |  \| |  /  \  |   /| |__   ',
        ' |  ___/ \   /    | |  |  __  | |  | | . ` |  \___ \| . ` | / /\ \ |  < |  __|  ',
        ' | |      | |     | |  | |  | | |__| | |\  |  ____) | |\  |/ ____ \| . \| |____ ',
        ' |_|      |_|     |_|  |_|  |_|\____/|_| \_| |_____/|_| \_/_/    \_|_|\_|______|']

def affichage_titre(titre):
  for i in titre:
    print(i)
    time.sleep(0.5)

affichage_titre(titre)

# création de la fenêtre
def affichage_aire_de_jeu(hauteur, largeur, titre):
    # Création d'une nouvelle fenètre en 0, 0
    win = curses.____
    # Les séquences d'échapement sont générés par certaines touches, les autres n'ont aucun effet
    win.keypad(__)
    # L'écho des caractères saisis est désactivé
    curses.noecho()
    # Pas de curseur visible
    curses.curs_set(__)
    # La saisie de caractère est non bloquante
    win.nodelay(1)
    # La fenètre a une bordure standard
    win.____
    # Définition d'une couleur pour le titre : texte en rouge sur fond blanc
    # Voir dans la documentation la table "lists the predefined colors"
    curses.init_pair(1, curses.____, curses.____)
    # Affichage du titre
    win.addstr(0, 27, titre, curses.color_pair(1))
    # Raffraichissement de la fenêtre
    win.____
    # Emission d'un beep
    curses.____
    # retourner la fenêtre
    return ____

