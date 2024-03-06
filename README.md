Ce programme est une simulation basique d'un système de gestion de comptes bancaires avec le language python. 
Il offre une interface utilisateur permettant d'effectuer diverses opérations bancaires, telles que la création de comptes, 
les retraits, les versements et la consultation des soldes.

Lorsque le programme démarre, il affiche un menu principal avec plusieurs options. 
L'utilisateur peut choisir parmi ces options en entrant le numéro correspondant à l'opération souhaitée. 
Les options comprennent la création de comptes, les retraits, les versements, la consultation des soldes et la sortie du programme.

Si l'utilisateur choisit de créer un compte, il est invité à fournir un nom d'utilisateur et un mot de passe. 
Un numéro de compte aléatoire est alors généré et enregistré dans un fichier texte avec les informations du compte.

Les fonctions de retrait et de versement permettent à l'utilisateur de manipuler le solde de son compte. 
Pour cela, il doit fournir son numéro de compte et son mot de passe. Si les informations sont correctes et si le solde est suffisant pour un retrait, 
le montant est retiré du solde. De même, pour un versement, le montant est ajouté au solde.

La fonction de consultation permet à l'utilisateur de vérifier le solde de son compte en fournissant son numéro de compte et son mot de passe. 
Si les informations sont correctes, le solde actuel est affiché à l'utilisateur.

Après chaque opération, l'utilisateur a la possibilité de retourner au menu principal pour effectuer d'autres opérations ou de quitter le programme.

En résumé, ce programme offre une interface conviviale pour la gestion des comptes bancaires, 
en permettant aux utilisateurs d'effectuer diverses transactions et de consulter leur solde, 
le tout à travers une boucle de menus et des fonctions interagissant avec un fichier de données.
