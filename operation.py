import numpy as np

def menu():
    print("Que souhaitez-vous faire ?")
    print("1 - Créer un compte")
    print("2 - Effectuer un retrait")
    print("3 - Effectuer un versement")
    print("4 - Consulter votre solde")
    print("5 - Quitter")
    choix = input("Entrez votre choix : ")
    return choix

# Fonction pour créer un compte bancaire
def creer_compte():
    solde=0
    nom_utilisateur = input("Entrez votre nom d'utilisateur : ")
    mot_de_passe = input("Entrez un mot de passe : ")
    numero_de_compte = str(int(np.random.random() * 1e16))
    # le nouveau compte est ajouter ici au fichier "comptes_bancaires.txt"
    with open("comptes_bancaires.txt", "a") as fichier:
        fichier.write("A,"+str(solde)+"," + numero_de_compte + "," + mot_de_passe + "," + nom_utilisateur + "," + "\n")
    print("Compte créé avec succès.")
    print("votre numero de compte est", numero_de_compte, "veuillez l'enregistrer")


# Fonction pour effectuer un retrait
def retrait():
    numero_de_compte = input("Entrez votre numéro de compte : ")
    mot_de_passe = input("Entrez votre mot de passe : ")

    # Lire le fichier "comptes_bancaires.txt" et convertir chaque ligne en une liste
    with open("comptes_bancaires.txt", "r") as fichier:
        lignes = fichier.readlines()

    comptes = []
    for ligne in lignes:
        comptes.append(ligne.strip().split(","))

    # Rechercher le numéro de compte et vérifier le mot de passe
    compte_trouve = False
    for compte in comptes:
        if compte[0] == "A" and compte[2] == numero_de_compte and compte[3] == mot_de_passe:
            compte_trouve = True
            solde = float(compte[1])
            montant = float(input("Entrez le montant à retirer : "))
            if solde >= montant:
                solde -= montant
                compte[1] = str(solde)
                # Mettre à jour le fichier "comptes_bancaires.txt"
                with open("comptes_bancaires.txt", "w") as fichier:
                    for compte in comptes:
                        fichier.write(",".join(compte) + "\n")
                print("votre Retrait a été effectué avec succès.")
            else:
                print("Désolé, votre solde insuffisant.")
            break

    if not compte_trouve:
        print("désolé, le numéro de compte ou le mot de passe est incorrect.")

# Fonction pour effectuer un versement
def versement():
    numero_de_compte = input("Entrez votre numéro de compte : ")
    mot_de_passe = input("Entrez votre mot de passe : ")

    # Lire le fichier "comptes_bancaires.txt" et convertir chaque ligne en une liste
    with open("comptes_bancaires.txt", "r") as fichier:
        lignes = fichier.readlines()

    comptes = []
    for ligne in lignes:
        comptes.append(ligne.strip().split(","))

    # Rechercher le numéro de compte et vérifier le mot de passe
    compte_trouve = False
    for compte in comptes:
        if compte[0] == "A" and compte[2] == numero_de_compte and compte[3] == mot_de_passe:
            compte_trouve = True
            solde = float(compte[1])
            montant = float(input("Entrez le montant à verser : "))
            solde += montant
            compte[1] = str(solde)
            # Mettre à jour le fichier "comptes_bancaires.txt"
            with open("comptes_bancaires.txt", "w") as fichier:
                for compte in comptes:
                    fichier.write(",".join(compte) + "\n")
            print("Votre versement a été effectué avec succès.")
            break

    if not compte_trouve:
        print("Désolé, le numéro de compte ou le mot de passe est incorrect.")

# Fonction pour consulter le solde d'un compte
def consultation():
    numero_de_compte = input("Entrez votre numéro de compte : ")
    mot_de_passe = input("Entrez votre mot de passe : ")

    # Lire le fichier "comptes_bancaires.txt" et convertir chaque ligne en une liste
    with open("comptes_bancaires.txt", "r") as fichier:
        lignes = fichier.readlines()

    comptes = []
    for ligne in lignes:
        comptes.append(ligne.strip().split(","))

    # Rechercher le numéro de compte et vérifier le mot de passe
    compte_trouve = False
    for compte in comptes:
        if compte[0] == "A" and compte[2] == numero_de_compte and compte[3] == mot_de_passe:
            compte_trouve = True
            solde = float(compte[1])
            print("Votre solde actuel est de :", solde)
            break

    if not compte_trouve:
        print("Désolé, le numéro de compte ou le mot de passe est incorrect.")

