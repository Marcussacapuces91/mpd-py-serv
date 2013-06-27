#!/usr/bin/python3
# -*- coding: utf-8 -*-

## 
# @author Marc Sibert
# Copyright (c) 2012

from bottle import                                                             \
    Bottle, run, static_file, request, response, redirect, HTTPError, get,     \
    post, abort

################################################################################
## Instance mpd pour l'api rest mpd
import socket

mpd = Bottle()

mpd.__PATH = '/var/run/mpd/socket'
mpd.__sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
mpd.__sock.connect(mpd.__PATH)

def read_reponse(sock = mpd.__sock):
    b = sock.gettimeout()
    sock.settimeout(10)
    chunk = sock.recv(4096).decode('utf-8')
    sock.settimeout(b)
    if chunk == '':
        raise RuntimeError('Socket connection broken')
    l = chunk.split('\n')
#    if l[-2][:2] != 'OK':
#        raise RuntimeError('Error Response')
    return l[:-1]

def write_command(value, sock = mpd.__sock):
    try:
        sock.sendall(value.encode('utf-8') + b'\n')
    except socket.error as err:
        print(err)
        if err.errno == 32:     # broken pipe (reinit socket)
            sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        else:
            raise err

# Initialisation !
if (read_reponse() != ['OK MPD 0.16.0']):
    raise RuntimeError('Waiting for MPD protocol number 0.16.0')

@mpd.get('/currentsong')
def get_current_song():
    write_command('currentsong')
    reponse = read_reponse()
    if reponse[-1] != 'OK':
        raise RuntimeError(reponse[0])
    r = {}
    for ligne in reponse[:-1]:
        l = ligne.split(':')
        r[l[0]] = l[1].strip()
    return r

@mpd.get('/status')
def get_status():
    write_command('status')
    reponse = read_reponse()
    if reponse[-1] != 'OK':
        raise RuntimeError(reponse[0])
    r = {}
    for ligne in reponse[:-1]:
        l = ligne.split(':')
        if len(l) == 2:
            r[l[0]] = l[1].strip()
        else:
            r[l[0]] = l[1:]
    return r
    
@mpd.put('/status/<var:re:(repeat|random|single)>')
def put_status(var):
    data = request.body.readline().decode('utf-8')
    write_command(var + ' ' + data)
    reponse = read_reponse()    
    if reponse[-1] == 'OK':
        response.status = '202 Accepted'
        return
    raise RuntimeError(reponse[0])
    
@mpd.post('/play')
def post_play():
    data = request.body.readline().decode('utf-8')
    if not data:
        write_command('playid')
    else:
        write_command('playid ' + data)
    reponse = read_reponse()
    if reponse == ['OK']:
        response.status = '202 Accepted'
        return    
    raise HTTPError(412, """
{reponse[0]}

Usage:
    http://<servname>/<service path>/play + body = songId""")

@mpd.post('/pause')
def post_pause():
    data = request.body.readline().decode('utf-8')
    if not data:
        write_command('pause')        # None : toggle
    elif data == '0':
        write_command('pause 0')    # 0 : playing
    else:
        write_command('pause 1')    # 1 : pause
    reponse = read_reponse()
    if reponse[-1] == 'OK':
        response.status = '202 Accepted'
        return    
    raise RuntimeError(reponse[0])

@mpd.post('/stop')
def post_stop():
    write_command('stop')
    reponse = read_reponse()
    if reponse[-1] != 'OK':
        raise RuntimeError(reponse[0])

@mpd.post('/next')
def post_next():
    write_command('next')
    reponse = read_reponse()
    if reponse[-1] != 'OK':
        raise RuntimeError(reponse[0])

@mpd.post('/previous')
def post_previous():
    write_command('previous')
    reponse = read_reponse()
    if reponse[-1] != 'OK':
        raise RuntimeError(reponse[0])

@mpd.get('/urlhandlers')
def get_urlhandlers():
    write_command('urlhandlers')
    reponse = read_reponse()
    if reponse[-1] != 'OK':
        raise RuntimeError(reponse[0])
    r = []
    for ligne in reponse[:-1]:
        l = ligne.split(':')    # handler : xxx
        r.append(l[1].strip())
    return {'handlers': r}

@mpd.put('/volume')
def put_volume():
    data = request.body.readline()
    if data:
        write_command('setvol ' + data.decode('utf-8'))
        reponse = read_reponse();
        if reponse == ['OK']:
            response.status = "202 Accepted"
            return
    raise HTTPError(412, """
{reponse[0]}

Usage:
    http://<servname>/<service path>/volume + body <volume>
    volume: in [0..100]""")

@mpd.post('/play/stream')
def play_stream():
    data = request.body.readline().decode('utf-8')
    if data:
        write_command('clear')
        reponse = read_reponse()
        if reponse != ['OK']:
            raise RuntimeError(reponse[0])
        write_command('add ' + data)
        reponse = read_reponse()
        if reponse == ['OK']:
            write_command('play')
            reponse = read_reponse();
            if reponse != ['OK']:
                raise RuntimeError(reponse[0])
            response.status = "202 Accepted"
            return
        rep = reponse[0]
    else:
        rep = "No data!"        

    handlers = get_urlhandlers()['handlers']
    raise HTTPError(412, """
{rep}

Usage:
    http://<servname>/<service path>/play/stream + body = <url>
    url:    shoud be a valid URL for MPD server (http, etc.) 
        encoded following <a href='http://tools.ietf.org/html/rfc3986'>RFC 3986</a>
        url protocols: {handlers}""")
    return None

################################################################################
## Service central faisant appel au site central
from urllib.request import urlopen, getproxies

central = Bottle()

central.__URL = 'http://radio.sibert.fr'

@central.get('/<filename:path>')
def get_radios(filename):
    f = urlopen(central.__URL + '/' + filename)
    return f.read()


################################################################################
## Instance principale de l'application
from httpheader import acceptable_language

app = Bottle()

app.mount('/mpd', mpd)
app.mount('/central', central)

## Renvoie la demande par défaut vers le fichier index.htm d'un répertoire 
#  localisé.
@app.route('/')
def index():
    return static_file('index.htm', root='static/')
#    langs = request.get_header('Accept-Language')
#    lang = acceptable_language(langs, ['en','fr'], 'en')
#    redirect(str(lang)+'/index.htm')

## Retourne le fichier demandé dans le répertoire.
# 
@app.route('/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static/')

## Route de test.
#
@app.route('/hello')
def hello():
    return "Hello world !"

## Lancement du serveur en écoute sur toutes les adresses & port 80.
#
if __name__ == '__main__':
#    run(app, host='0.0.0.0', port=8080, debug=True, reloader=True)
    run(app, host='0.0.0.0', port=80)
