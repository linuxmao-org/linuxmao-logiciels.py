# linuxmao-logiciels.py

# Mais pourquoi ?!

Ce script a été "codé" pour plusieurs raisons :
* aider à suivre les mises à jour des logiciels MAO sur Linux afin de les 
  annoncer sur https://linuxmao.org et de donner à manger à 
  http://librazik.tuxfamily.org :)
* me permettre de découvrir le langage python. Etant un un piètre codeur, vos
  contributions ou suggestions sont les bienvenues :)

# Installation
* cloner le repository
* Installer les dépendances python (python3-requests et python3-urllib3)	
* configurer linuxmao-logiciels.ini avec les identifiants github (le nombre de
  requêtes vers l'API est très limité sans être identifié)

# Utilisation

Montrer les options disponibles :
```
./linuxmao-logiciels.py 
usage: linuxmao-logiciels.py [-h] [--logiciel LOGICIEL] [--repo REPO]

optional arguments:
  -h, --help           show this help message and exit
  --logiciel LOGICIEL  chercher si une logiciel est présent dans la base de
                       données locale
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