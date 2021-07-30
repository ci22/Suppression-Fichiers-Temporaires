# Version 1.2.
# Open-Source licence GPL (GNU General Public Licence v3.0).
# Ce script permet la suppression des fichiers temporaires du poste client sur lequel il est exécuté.

# On commence par appeler les modules du système d'exploitation (variable d'environnement):
# On récupère le processus. -> Préciser dans le read-me quel processus.
import subprocess
import time
import paramiko


# Choisir poste local ou exécution sur le réseau.
print ("Ce programme est exécutable en local et en réseau")
choixMode = input("Pour exécution locale: saisir ''local'' - Pour exécution réseau: saisir ''reseau''")

# Confirmation du choix de l'utilisateur
print("Vous avez choisi le mode",choixMode)

# Lecture du choix du mode d'exécution.
if choixMode == "local":
# Exécution poste local
    print("Chargement du répertoire C:\Windows\Temp")
    time.sleep(5)
    print(". . .")


def obtenirTaille():
    # On récupère le processus. -> Préciser dans le read-me quel processus.
    import os

    # On commence avec une variable à 0
    tailleFichiers = 0
    # On déclare deux variables vides pour éviter des erreurs
    dossiersEtFichiers = None
    espaceOccupe = None

    # On précise le chemin où se trouvent les fichiers temporaires
    cheminAcces = 'C:\Windows\Temp'

    # On parcourt le chemin d'accès stocké dans la variable
    for chemin, repertoires, fichers in os.walk(cheminAcces):
        for taille in fichers:
            # On stocke le chemin de chaque fichier et sa taille dans la variable
            espaceOccupe = os.path.join(chemin, taille)
            # On associe l'espace occupé par les fichiers temporaires avec la variable tailleFichiers
            tailleFichiers += os.stat(espaceOccupe).st_size
    # On affiche sur la console l'espace occupé par les fichiers temporaires
    print("Le fichiers temporaires occupent au sein du dossier C:\Windows\Temp:", tailleFichiers, "octets")


def fonctionPrincipale():
    import os
    cheminAcces = 'C:\Windows\Temp'
    fichierTemporaire = ".tmp"
    # On fait redémarrer la fonction plusieurs fois pour pouvoir tout effacer
    for compteur in range(1, 50):

        # On vérifie que le répertoire existe
        if os.path.exists(cheminAcces):

            # On teste le chemin d'accès pour vérifier que c'est un répertoire
            if os.path.isdir(cheminAcces):

                # On navigue dans les sous-dossiers
                for root_folder, folders, files in os.walk(cheminAcces):

                    # On vérifie l'existence d'un fichier avec la variable fichier
                    for file in files:
                        # On recherche le chemin d'accès du fichier
                        cheminFichier = os.path.join(root_folder, file)

                        # On récupère l'extension à partir du fichier
                        extensionFichierTemp = os.path.splitext(cheminFichier)[1]

                    # Comparer l'extension du fichier avec le contenu de la variable
                    if fichierTemporaire == extensionFichierTemp:

                        # Si la comparaison indique que c'est un fichier temporaire
                        # dans la variable, alors on supprime
                        if not os.remove(cheminFichier):

                            # Confirmation de la suppression
                            print("Le fichier temporaire", cheminFichier, " a bien été supprimé")

                        else:
                            # Message si erreur durant la tâche de suppression
                            print("ERREUR! Le fichier temporaire", cheminFichier, " n'a pas pu être supprimé")
                            # Le programme incite à vérifier que l'on est bien administrateur de son poste
                            print(
                                "Veuillez vérifier que vous disposez des droits nécessaires pour exécuter ce programme, puis réessayez")


                    # Si la vérification est fausse, le chemin d'accès ne correspond pas à un répertoire
                    else:
                        print("Le chemin d'accès - ", cheminFichier,
                              " n'est pas un répertoire/dossier ou un fichier temporaire")
            # Si le test échoue, le chemin d'accès n'existe pas
            else:
                print("Le chemin d'accès spécifé - ", cheminFichier, " - n'existe pas")


if choixMode=="reseau":
        print ("Scan du réseau local en cours...")
        print ("Cette opération peut prendre plusieurs minutes")
        time.sleep(3)
        print (". . .")
        time.sleep(3)
        print (". . .")


# Scanner le parc informatique.
# On effectue un ping dans une plage d'adresses allant de 11 à 253.
# On suppose que les serveurs occupent les adresses de 1 à 10.
# On suppose que la passerelle occupe l'adresse terminant par 254.
# (Range d'addresses personnalisable selon les besoins et spécificités du réseau).
        for Ping in range(21,23):
            adresseIP = "192.168.1." + str(Ping)
            reponse = subprocess.run(['Ping', '-n', '3', adresseIP], shell=True)

        # Démarrer une connexion SSH avec Paramiko
        # Invite la saisie de l'adresse IP du poste client distant
        # Ou invite à annuler la connexion
        global IPHote
        IPHote = input("Entrez l'adresse IP du poste sur lequel vous voulez exécuter le script - ou annuler pour quitter")

        if IPHote == "annuler":
                exit()
        else:
                IPHote = input("Entrez l'adresse IP du poste sur lequel vous voulez exécuter le script - ou annuler pour quitter")

        # Ouvrir la fonction Paramiko pour lancer une connexion SSH
        def fonctionSSH ():
                # On commence avec une variable vide pour le nom du poste informatique
                # La valeur sera ajoutée à la variable plus tard.
                NomPoste = None
                # Continuer d'exécuter la fonction pendant que la variable est réelle.
                fonctionSSH = True
                while fonctionSSH:
                        # La fonction va boucler jusqu'à ce que l'on saisisse un nom d'utilisateur
                        nomUtilisateur = ""
                        while nomUtilisateur == "":
                                nomUtilisateur = input("Saisissez le nom d'utilisateur du poste distant, ou annuler pour quitter".format(NomPoste))
                                if nomUtilisateur == "annuler":
                                        exit()
                        # La fonction va boucler jusqu'à ce que l'on saisisse un mot de passe
                        motDePasse = ""
                        while motDePasse == "":
                                motDePasse = input("Saisissez le mot de passe du poste distant, ou annuler pour quitter".format(NomPoste))
                                if motDePasse == "annuler":
                                        exit()
                        # Tentative d'ouverture de connexion SSH
                        try:
                                # Création d'un client SSH
                                ssh = paramiko.SSHClient()
                                # Autoriser la connexion SSH sur un poste distant avec clé publique inconnue
                                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                                # Confirmer la connexion SSH
                                print("Connexion SSH en cours...")
                                # On stocke la commande qui sera exécutée sur le système Windows dans une variable
                                commandeDistante = "cd C:\Windows\Temp && del *.tmp"
                                # Ouvrir la connexion avec le nom d'utilisateur et le mot de passe du poste distant
                                ssh.connect(IPHote, username=nomUtilisateur, password=motDePasse)
                                # On demande une exécution avec Paramiko de la commande stockée dans la variable
                                stdin, stdout, stderr = ssh.exec_command(commandeDistante)
                                print(stdout.read().decode())
                                print("Exécution de la commande distante en cours (via SSH)")
                                
                                fonctionSSH = False
                   # Fermer la connexion SSH avec le poste distant si elle est ouverte
                                if ssh: ssh.close()
        # Afficher les erreurs sur la console en cas de défaut
        # Erreur de fermeture de connexion
                        except paramiko.ssh_exception.NoValidConnectionsError as erreurSSH:
                                print("ERREUR - Connexion fermée! Voici le code erreur rencontré:")
                                print(erreurSSH)

        # Erreur dûe à un défaut d'authentification
                        except paramiko.ssh_exception.AuthenticationException as erreurSSH:
                                print("ERREUR - Défaut d'authentification! Voici le code erreur rencontré:")
                                print(erreurSSH)
                                pass
                        
         # On appelle la fonction SSH pour faire exécuter la partie suivante du programme
        fonctionSSH()
# On demande la fonction principale
obtenirTaille()
fonctionPrincipale()
