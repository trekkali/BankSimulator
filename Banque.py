from operation import menu, creer_compte, retrait, consultation, versement

choix1 = 0

while choix1 != 5:
    choix1 = int(menu())
    
    if choix1 == 1:
        creer_compte()
    elif choix1 == 2:
        retrait()
    elif choix1 == 3:
        versement()
    elif choix1 == 4:
        consultation()
    elif choix1 == 5:
        print("Au revoir et à bientôt !")
        break
    else:
        print("Choix invalide, veuillez réessayer.")
        continue

    while True:
        print("~~~~")
        print("~~~~")
        choix2 = input("Voulez-vous retourner au menu (1) ou quitter (2) ? ")
        if choix2 == "1":
            break
        elif choix2 == "2":
            print("Au revoir et à bientôt !")
            exit()
        else:
            print("Choix invalide, veuillez réessayer.")
