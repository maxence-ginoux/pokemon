# class Poke:
#     def __init__(self, img, nom, point_de_vie,point_de_vie_max, niveau, puissance_attaque, defense, types, evolution):
#         self.img = img
#         self.nom = nom
#         self.point_de_vie = point_de_vie
#         self.point_de_vie_max = point_de_vie_max
#         self.niveau = niveau
#         self.puissance_attaque = puissance_attaque
#         self.defense = defense
#         self.types = types
#         self.evolution = evolution

#     def vie(self):
#         return self.point_de_vie > 0    

#     def opponent_data(self):
#         return {
#             "img": self.img,
#             "nom": self.nom,
#             "point_de_vie": self.point_de_vie,
#             "niveau": self.niveau,
#             "puissance_attaque": self.puissance_attaque,
#             "defense": self.defense,
#             "types": self.types,
#             "evolution": self.evolution
#         }

# player_pokemon = Poke("img_player", "nom_player", 100, 5, 50, 30, ["Type1", "Type2"], "evolution_player")
# opponent_pokemon = Poke("img_opponent", "nom_opponent", 100, 5, 50, 30, ["Type3", "Type4"], "evolution_opponent")


# Modifiez votre classe Poke dans le fichier poke.py
class Poke:
    def __init__(self, img, nom, point_de_vie, point_de_vie_max, niveau, points_expérience, points_expérience_max, puissance_attaque, defense, types, evolution, attaques):
        self.img = img
        self.nom = nom
        self.point_de_vie = point_de_vie
        self.point_de_vie_max = point_de_vie_max
        self.niveau = niveau
        self.points_expérience = points_expérience  #pour représenter la progression et l'expérience acquise
        self.points_expérience_max = points_expérience_max
        self.puissance_attaque = puissance_attaque
        self.defense = defense
        self.types = types
        self.evolution = evolution
        self.attaques = attaques  # Liste d'attaques avec leurs dégâts

    def gagner_points_experience(self, amount):
        self.points_expérience += amount
        if self.points_expérience >= self.points_expérience_max:
            self.monter_niveau()

    def monter_niveau(self):
        self.niveau += 1
        self.points_expérience = 0  # Réinitialiser points_expérience
        self.points_expérience_max = self.niveau * 100  
        self.ameliorer_stats()  # Mettre à jour les statistiques en fonction du niveau

    def ameliorer_stats(self):
        # Ajuste les améliorations de statistiques en fonction du niveau
        self.point_de_vie_max += 10
        self.puissance_attaque += 5
        # On peut mettre d'autres statistiques à améliorer

    def attaquer(self, adversaire, attaque_index):
        # Implémente la logique d'attaque en fonction de l'attaque choisie
        degats = self.attaques[attaque_index]['degats']
        adversaire.subir_degats(degats)

    def subir_degats(self, degats):
        self.point_de_vie -= degats
        if self.point_de_vie < 0:
            self.point_de_vie = 0

