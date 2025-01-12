class DossierPersonnel:
    def __init__(self, etat_civil, numero_telephone, adresse, mail):
        self.etat_civil = etat_civil
        self.numero_telephone = numero_telephone
        self.adresse = adresse
        self.mail = mail

    def mettre_a_jour(self, new_etat_civil, new_numero_telephone, new_adresse, new_mail):
        self.etat_civil = new_etat_civil
        self.numero_telephone = new_numero_telephone
        self.adresse = new_adresse
        self.mail = new_mail


class Eleve:
    def __init__(self, nom, age, sexe):
        self.nom = nom
        self.age = age
        self.sexe = sexe

    def consulter_copie(self):
        # Logic for consulting a copy
        print(f"{self.nom} is consulting their copy.")


class Classe:
    def __init__(self, annee, nbr_eleves):
        self.annee = annee
        self.nbr_eleves = nbr_eleves
        self.eleves = []  # Composition: A class contains and manages Eleve objects

    def ajouter_eleve(self, eleve):
        if len(self.eleves) < 30:  # Cardinality constraint
            self.eleves.append(eleve)
            self.nbr_eleves += 1
        else:
            print("Cannot add more students. Maximum capacity reached.")

    def retirer_eleve(self, eleve):
        if eleve in self.eleves:
            self.eleves.remove(eleve)
            self.nbr_eleves -= 1


class Professeur:
    def __init__(self, nom, age, matiere_enseignee):
        self.nom = nom
        self.age = age
        self.matiere_enseignee = matiere_enseignee
        self.dossier_personnel = None  # Aggregation: Assigned externally

    def attribuer_classe(self, classe):
        # Usage relation
        print(f"Professor {self.nom} is assigned to class {classe.annee}.")

    def ajouter_note():
        # Logic to add grades
        pass
