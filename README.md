# linuxmao-logiciels.py

# Mais pourquoi ?!

Ce script a été commis pour plusieurs raisons :
* Aider à suivre les mises à jour des logiciels MAO sur Linux afin de les 
  annoncer sur https://linuxmao.org et, accessoirement, de donner à manger à 
  http://librazik.tuxfamily.org
* Me permettre de découvrir le langage python. Etant un un piètre codeur, vos
  contributions ou suggestions sont les bienvenues !

# Installation
* Cloner le repository
* Installer les dépendances python (python3-requests et python3-urllib3)	
* Configurer linuxmao-logiciels.ini avec les identifiants github (le nombre de
  requêtes vers l'API est très limité sans être identifié)

# Utilisation

Montrer les options disponibles :
```
./linuxmao-logiciels.py 
usage: linuxmao-logiciels.py [-h] [--logiciel LOGICIEL] [--stats]
                             [--repo REPO]

optional arguments:
  -h, --help           show this help message and exit
  --logiciel LOGICIEL  chercher si un logiciel est présent dans la DB locale
  --stats              afficher des statistiques sur la DB locale
  --repo REPO          chercher les maj dans les repos en ligne (repo =
                       sourceforge, github, ALL)
```

Chercher si un logiciel est présent dans la DB locale :
```
./linuxmao-logiciels.py --logiciel aud
audiveris - 5.1.0 - https://github.com/Audiveris/audiveris/
Audacity - Audacity-2.3.1 - https://github.com/audacity/audacity/
```

Chercher si des logiciels ont été mis à jour sur sourceforge :
```
./linuxmao-logiciels.py --repo sourceforge
wavesurfer - /wavesurfer/1.8.8p5/wavesurfer-1.8.8p5-linux-x86_64.tgz - https://sourceforge.net/projects/wavesurfer/
---
qtractor - /qtractor/0.9.5/qtractor-0.9.5.tar.gz - https://sourceforge.net/projects/qtractor/
---
[...]

```

Chercher si des logiciels ont été mis à jour sur les repos pris en charge  :
```
./linuxmao-logiciels.py --repo ALL
```

# TODO
* Gérer les exceptions en particulier sur les requêtes http (l'API 
  sourceforge n'est pas toujours super en forme)
* Factoriser certaines fonctions
* Permettre l'ajout de logiciels ou la modification d'une entrée dans la base 
  locale. Actuellement il faut utiliser, par exemple, sqlitebrowser
* Jouer avec le threading afin d'accélérer les choses
* Ajouter d'autres repos comme gitlab ou bitbucket, voir même des sites 
  spécifiques
