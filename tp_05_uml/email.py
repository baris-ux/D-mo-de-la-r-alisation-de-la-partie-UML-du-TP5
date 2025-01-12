class Fichier:
    def __init__(self, nom, taille, type_fichier):
        self.nom = nom
        self.taille = taille
        self.type_fichier = type_fichier

    def ouvrir(self):
        print(f"Opening file: {self.nom}")

    def telecharger(self):
        print(f"Downloading file: {self.nom} ({self.taille} KB)")


class Email:
    def __init__(self, titre, texte, expediteur, destination):
        self.titre = titre
        self.texte = texte
        self.expediteur = expediteur
        self.destination = destination
        self.fichiers_joints = []  # Composition: List of Fichier objects

    def envoyer(self):
        print(f"Sending email '{self.titre}' from {self.expediteur} to {self.destination}.")
        if self.fichiers_joints:
            print(f"Attachments: {[fichier.nom for fichier in self.fichiers_joints]}")
        else:
            print("No attachments.")

    def ajouter_fichier(self, fichier):
        self.fichiers_joints.append(fichier)
        print(f"Added file: {fichier.nom} to the email.")

    def retirer_fichier(self, fichier):
        if fichier in self.fichiers_joints:
            self.fichiers_joints.remove(fichier)
            print(f"Removed file: {fichier.nom} from the email.")
        else:
            print(f"File: {fichier.nom} not found in attachments.")
