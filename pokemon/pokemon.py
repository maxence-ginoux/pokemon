class Pokemon:
    def __init__(self, nom ,niveau, type, points_de_vie, puissance_attaque, defense, evolution):
        self.nom = nom
        self.niveau = niveau
        self.points_de_vie = points_de_vie
        self.puissance_attaque = puissance_attaque
        self.defense = defense
        self.type = type
        self.evolution = evolution

    def afficher_informations(self):
            print(f"{self.nom} - Niveau {self.niveau}")
            print(f"Points de vie: {self.points_de_vie}")
            print(f"Puissance d'attaque: {self.puissance_attaque}")
            print(f"Défense: {self.defense}")
            print(f"Type: {', '.join(self.type)}")
            print(f"Evolution possible : {self.evolution}") 

    def modifier_point_de_vie(self, degats):
        self.points_de_vie -= degats

    def evoluer():
        pass

    

