class Metro:
   
    def __init__(self, marque, modele, annee, couleur):
        """Initialise les attributs du véhicule"""
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.couleur = couleur
        self.vitesse = 0

    def vitesse(self, heure):
        """vitesse de Metro"""
        self.vitesse += heure

    def rapide(self, arriveaheure):
        """rapide de Metro"""
        self.vitesse = arriveaheure

    def afficher_info(self):
        """Affiche les informations sur le Metro"""
        print(f"{self.marque} {self.modele} ({self.annee}) de couleur {self.couleur}")
        print(f"vitesse : {self.vitesse} km/h")
Metro = Metro("RATP", "sncf", 2021, "Vert")
Metro.rapide(200)
Metro.afficher_info() 
