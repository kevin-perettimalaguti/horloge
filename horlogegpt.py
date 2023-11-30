#Importation de la bibliothèque 'time'
import time

heure_actuelle = (0, 0, 0)
alarme = None

def afficher_heure():
    global heure_actuelle
    heure_str = '{:02d}:{:02d}:{:02d}'.format(heure_actuelle[0], heure_actuelle[1], heure_actuelle[2])
    print(heure_str)

def regler_heure(heures, minutes, secondes):
    global heure_actuelle
    heure_actuelle = (heures, minutes, secondes)
    afficher_heure()

def regler_alarme(heures, minutes, secondes):
    global alarme
    alarme = (heures, minutes, secondes)

def verifier_alarme():
    global heure_actuelle, alarme
    if alarme is not None and heure_actuelle == alarme:
        print("Réveillez-vous ! C'est l'heure")

def actualiser_heure():
    global heure_actuelle
    while True:
        time.sleep(1)
        heure_actuelle = (heure_actuelle[0], heure_actuelle[1], heure_actuelle[2] + 1)
        if heure_actuelle[2] == 60:
            heure_actuelle = (heure_actuelle[0], heure_actuelle[1] + 1, 0)
            if heure_actuelle[1] == 60:
                heure_actuelle = (heure_actuelle[0] + 1, 0, 0)
        afficher_heure()
        verifier_alarme()

# Remplissage des valeurs
regler_heure(21, 30, 0)
regler_alarme(8, 30, 0)  

actualiser_heure()  
