mpd-py-serv
===========

A web server to control MPD server installed localy.

Using :
* Python 3.x
* Bottle.py Framework <http://bottlepy.org/docs/dev/>
* Dojo Toolkit <http://dojotoolkit.org/>
* httpheader.py 

Copyright © 2013 Marc Sibert <marc at sibert dot fr>

This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See the COPYING.WTFYW file for more details.

Install
-------

    ~ $ sudo aptitude update
    ~ $ sudo aptitude install mpd

Importer les sources (au besoin, définir les variables `http_proxy` et `https_proxy`)
    ~ $ git clone https://github.com/Marcussacapuces91/mpd-py-serv CybeRadio

Ajouter le framework bootle.py
    ~ $ cd CybeRadio
    ~/CybeRadio $ wget https://github.com/defnull/bottle/raw/master/bottle.py

Télécharger l'API Dojo
    ~/CybeRadio $ cd static
    ~/CybeRadio/static $ git clone https://github.com/dojo/dojo
    ~/CybeRadio/static $ git clone https://github.com/dojo/dijit

Si nécessaire :
    ~/CybeRadio/static $ git clone https://github.com/dojo/dojox
    
    
  
