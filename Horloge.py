# Importation de la bibliothèque 'time'
import time

# Récupération des valeurs de l'utilisateur pour régler l'heure
heure, minute, seconde = map(int, input("Réglez votre heure : ").split())
heure_actuelle = [heure, minute, seconde]  # Modification des valeurs dans la liste

# Variable qui contient un caractère pour qui servira à activer la configuration de l'alarme
active_alarme = "h"

alarme = None  # Variable pour la configuration à suivre dans le programme

def afficher_heure():
    # Fonction pour afficher l'heure avec le format demandé
    global heure_actuelle
    heure_visuel = '{:02d}:{:02d}:{:02d}'.format(heure_actuelle[0], heure_actuelle[1], heure_actuelle[2])
    print(heure_visuel)

def regler_heure(heures, minutes, secondes):
    # Fonction simple qui rappelle la liste "heure_actuelle" et lui redonne la valeur du début
    global heure_actuelle
    heure_actuelle = [heures, minutes, secondes]
    afficher_heure()

def config_alarme():
    # Rappelle de la variable "alarme" et attribution de la même valeur en liste que le réglage
    global alarme
    reponse = input("Appuyez sur 'h' pour configurer l'alarme, ou 'non' pour ne pas la configurer : ")
    if reponse == active_alarme:
        heure_alarme, minute_alarme, seconde_alarme = map(int, input("Réglez votre heure d'alarme : ").split())
        alarme = [heure_alarme, minute_alarme, seconde_alarme]
        print(f"Alarme configurée pour {alarme[0]}:{alarme[1]}:{alarme[2]}")

def verifier_alarme():
    # Vérification de l'alarme et affichage du message si l'heure actuelle correspond à l'alarme
    global heure_actuelle, alarme
    if alarme is not None and heure_actuelle == alarme:
        print("Réveillez-vous ! C'est l'heure")

def actualiser_heure():
    # Actualisation de l'heure toutes les secondes
    global heure_actuelle
    while True:
        time.sleep(1)
        heure_actuelle[2] += 1
        if heure_actuelle[2] == 60:
            heure_actuelle[1] += 1
            heure_actuelle[2] = 0
            if heure_actuelle[1] == 60:
                heure_actuelle[0] += 1
                heure_actuelle[1] = 0
        afficher_heure()
        verifier_alarme()

# Remplissage des valeurs initiales
regler_heure(heure, minute, seconde)
config_alarme()

while True:
    actualiser_heure()








