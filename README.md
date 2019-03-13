# linuxmao-logiciels.py

# Mais pourquoi ?!
Ce script a été commis pour plusieurs raisons :
* Aider à suivre les mises à jour des logiciels MAO sur Linux afin de les 
  annoncer sur https://linuxmao.org et, accessoirement, de donner à manger à 
  http://librazik.tuxfamily.org
* Me permettre de découvrir le langage python. Etant un un piètre codeur, vos
  contributions ou suggestions sont les bienvenues !

# Principe
* Les versions en cours des logiciels sont stockées dans une base de données
  sqlite
* Les API des différents repos sont interrogées afin de scruter les nouvelles
  mises à jour
* Le script indique qu'une nouvelle version est disponible

# Installation
* Cloner le repository
* Installer les dépendances python (python3-requests et python3-urllib3)	
* Configurer linuxmao-logiciels.ini avec les identifiants github (le nombre de
  requêtes vers l'API est très limité sans être identifié)

# Utilisation

Montrer les options disponibles :
```
./linuxmao-logiciels.py 
usage: linuxmao-logiciels.py [-h] [--cherche CHERCHE] [--stats]
                             [--repo REPO]

optional arguments:
  -h, --help           show this help message and exit
  --cherche CHERCHE    chercher si un logiciel est présent dans la DB locale
  --stats              afficher des statistiques sur la DB locale
  --repo REPO          chercher les maj dans les repos en ligne (repo =
                       sourceforge, github, gitlab, ALL)
```

Chercher si un logiciel est présent dans la base de données locale :
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
* Ajouter d'autres repos comme bitbucket ou savannah, voir même des sites 
  spécifiques
* Poster sur le formulaire de linuxmao.org 
* Mettre à jour des variables version et date sur linuxmao.org
  à jour les versions 
