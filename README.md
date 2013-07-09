mpd-py-serv
===========

A web server to control MPD server installed localy.

Copyright © 2013 Marc Sibert <marc at sibert dot fr>

This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See the COPYING.WTFYW file for more details.

Dependences
-----------

* Python 3.x

Install
-------

    ~ $ sudo aptitude update
    ~ $ sudo aptitude install mpd

Aller dans le répertoire qui va bien, par exemple :

    ~ $ cd /usr/local/bin

et importer les sources (au besoin, définir les variables `http_proxy` et `https_proxy`)

    ~ $ git clone https://github.com/Marcussacapuces91/mpd-py-serv radio

Créer un lien logique entre le répertoire init.d et le script de lancement du serveur Radio

    ~ $ sudo ln -s /usr/local/bin/radio/etc/init.d/radio /etc/init.d/radio
    
Au besoin, ajouter des variables (comme la définition du proxy) dans le fichier :

    /etc/default/radio
    
Vérifier le fonctionnement du service avec :

    ~ $ sudo service radio start
    ~ $ sudo service radio status
    
Activer le serveur au démarrage :

    ~ $ sudo update-rc.d radio defaults

