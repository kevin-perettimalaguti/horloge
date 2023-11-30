# Importation de 'time'
import time 

 # Réglage de l'heure
heures, minutes, secondes = map(int, input("Règler votre heure : ").split())

# Classe avec toutes les fonctions de l'Horloge
class clock:    
    def afficher_heure(heures, minutes, secondes):
        print(f"{heures:02d}:{minutes:02d}:{secondes:02d}")   
        
    
            
        
        
   
    #def regler_alarme():


# Actualisation de l'heure toutes les secondes    
while True:
    clock.afficher_heure(heures, minutes, secondes) #Appelle de la fonction d'affichage

    # Incrémente les secondes
    secondes += 1
    if secondes == 60:
        secondes = 0
        minutes += 1
        if minutes == 60:
            minutes = 0
            heures += 1
            if heures == 24:
                heures = 0
        
    time.sleep(1) # cPause d'une seconde




