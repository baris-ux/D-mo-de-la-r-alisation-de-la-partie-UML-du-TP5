class Regime:
    def __init__(self, nom, quantite):
        self.nom = nom
        self.quantite = quantite

    def proposer_nourriture(self):
        print(f"Proposing {self.quantite} of {self.nom}.")


class PartiesCorps:
    def __init__(self, nom, fonction, taille):
        self.nom = nom
        self.fonction = fonction
        self.taille = taille


class Animaux:
    def __init__(self, nom, espece, sexe):
        self.nom = nom
        self.espece = espece
        self.sexe = sexe
        self.parties_corps = []  # Composition: Animaux manages PartiesCorps objects
        self.regime = None  # Association: Linked externally

    def ajouter_partie_corps(self, partie_corps):
        self.parties_corps.append(partie_corps)

    def manger(self):
        if self.regime:
            print(f"{self.nom} is eating {self.regime.nom}.")
        else:
            print(f"{self.nom} has no regime assigned.")

    def dormir(self):
        print(f"{self.nom} is sleeping.")

    def se_deplacer(self):
        print(f"{self.nom} is moving.")


class Habitat:
    def __init__(self, temperature, capacite, surface, emplacement):
        self.temperature = temperature
        self.capacite = capacite
        self.surface = surface
        self.emplacement = emplacement
        self.animaux = []  # Association: Contains Animaux objects

    def ajouter_animal(self, animal):
        if len(self.animaux) < self.capacite:
            self.animaux.append(animal)
            print(f"Added {animal.nom} to the habitat.")
        else:
            print("Cannot add more animals. Habitat is full.")

    def retirer_animal(self, animal):
        if animal in self.animaux:
            self.animaux.remove(animal)
            print(f"Removed {animal.nom} from the habitat.")
        else:
            print(f"{animal.nom} not found in the habitat.")
