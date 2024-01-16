class Poke:
    def __init__(self, img, nom, point_de_vie, niveau, puissance_attaque, defense, types, evolution):
        self.img = img
        self.nom = nom
        self.point_de_vie = point_de_vie
        self.niveau = niveau
        self.puissance_attaque = puissance_attaque
        self.defense = defense
        self.types = types
        self.evolution = evolution

    def vie(self):
        return self.point_de_vie > 0    

    def to_dict(self):
        return {
            "img": self.img,
            "nom": self.nom,
            "point_de_vie": self.point_de_vie,
            "niveau": self.niveau,
            "puissance_attaque": self.puissance_attaque,
            "defense": self.defense,
            "types": self.types,
            "evolution": self.evolution
        }

# Example initialization
player_pokemon = Poke("img", "nom", "point_de_vie", "niveau", "puissance_attaque", "defense", "types", "evolution")  # Replace with your actual initialization
opponent_pokemon = Poke("img", "nom", "point_de_vie", "niveau", "puissance_attaque", "defense", "types", "evolution")
