class Pokemon:
    def __init__(self, img, nom, point_de_vie, point_de_vie_max, niveau, points_experience, points_experience_max, puissance_attaque, defense, types, attaques, rencontrer):
        # Initialisation pour les attributs 
        self.img = img 
        self.nom = nom
        self.point_de_vie = point_de_vie
        self.point_de_vie_max = point_de_vie_max
        self.niveau = niveau
        self.points_experience = points_experience  # Pour représenter la progression et l'expérience acquise
        self.points_experience_max = points_experience_max
        self.puissance_attaque = puissance_attaque
        self.defense = defense
        self.types = types
        self.attaques = attaques   # Initialisation de attaques comme une liste vide s'il est None
        self.rencontrer = rencontrer

    def get_nom(self):
        return self.nom
    def set_nom(self, nom):
        self.nom = nom

    def get_img(self):
        return self.img
    def set_img(self, img):
        self.img = img    

    def get_point_de_vie(self):
        return self.point_de_vie
    def set_point_de_vie(self, point_de_vie):
        self.point_de_vie = point_de_vie

    def get_point_de_vie_max(self):
        return self.point_de_vie_max
    def set_point_de_vie_max(self, point_de_vie_max):
        self.point_de_vie_max = point_de_vie_max

    def get_niveau(self):
        return self.niveau
    def set_niveau(self, niveau):
        self.niveau = niveau

    def get_points_experience(self):
        return self.points_experience
    def set_points_experience(self, points_experience):
        self.points_experience = points_experience

    def get_points_experience_max(self):
        return self.points_experience_max
    def set_points_experience_max(self, points_experience_max):
        self.points_experience_max = points_experience_max

    def get_puissance_attaque(self):
        return self.puissance_attaque
    def set_puissance_attaque(self, puissance_attaque):
        self.puissance_attaque = puissance_attaque

    def get_defense(self):
        return self.defense
    def set_defense(self, defense):
        self.defense = defense

    def get_types(self):
        return self.types
    def set_types(self, types):
        self.types = types

    def get_evolution(self):
        return self.evolution
    def set_evolution(self, evolution):
        self.evolution = evolution

    def get_attaques(self):
        return self.attaques
    def set_attaques(self, attaques):
        self.attaques = attaques

    def get_rencontrer(self):
        return self.rencontrer
    def set_rencontrer(self, rencontrer):
        self.rencontrer = rencontrer    

    def gagner_points_experience(self, amount):
        self.points_experience += amount
        while self.points_experience >= self.points_experience_max:
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
        if 0 <= attaque_index < len(self.attaques):
            degats = self.attaques[attaque_index]['degats']
            adversaire.subir_degats(degats)

    def subir_degats(self, degats):
        self.point_de_vie -= degats
        if self.point_de_vie < 0:
            self.point_de_vie = 0





