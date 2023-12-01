# Importation de la bibliothèque 'time'
import time

# Création d'un tuple
heure_actuelle_tuple = (0, 0, 0)

# Transformation de mon tuple en liste pour permettre les modification des valeurs nécessaires dans le programme
heure_actuelle = list(heure_actuelle_tuple)
heure, minute, seconde = map(int, input("Réglez votre heure : ").split())
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
   

def config_alarme():
    # Rappelle de la variable "alarme" et attribution de la même valeur en tuple que le réglage
    global alarme
    active_alarme = "y" # Variable qui contient un caractère pour qui servira à activer la configuration de l'alarme
    refus_alarme = "n"
    reponse = str(input("Appuyez sur 'y' pour configurer l'alarme, ou 'n' pour ne pas la configurer : "))
    if reponse == active_alarme: # Apres la question , si j'appuis sur 'y' ca me demande de régler l'heure de mon alarme
        heure_alarme, minute_alarme, seconde_alarme = map(int, input("Réglez votre heure d'alarme : ").split())
        alarme = [heure_alarme, minute_alarme, seconde_alarme]
        print(f"Alarme configurée pour {alarme[0]}:{alarme[1]}:{alarme[2]}")

    # Si je met 'n' l'heure défile normalement, sans alarme configurer
    elif reponse == refus_alarme:
        afficher_heure()
        actualiser_heure

    # Si je met autre chose que 'y' ou 'n' ca m'indique de bien faire le choix entre mes 2 lettres, ca me repose la question
    else:
        print("Veuillez rentrée 'y' ou 'n' pour la configuration de l'alarme")
        config_alarme()    

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

# Rappelle des fonction pour un bonne fonctionnalité du script
regler_heure(heure, minute, seconde)
config_alarme()

# Rajoute d'une boucle pour continuer d'actualiser l'heure peut importe l'action
while True:
    actualiser_heure()



#--------------------------------------Kevin Peretti-Malaguti---------------------------------------------------------------
