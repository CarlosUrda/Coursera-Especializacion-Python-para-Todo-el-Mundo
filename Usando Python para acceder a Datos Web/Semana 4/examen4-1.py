#!/usr/bin/env python
#coding=utf-8

# Examen 1 de la Semana 4 del Curso 3. Obtener los valores de etiquetas span.

__author__      = "Carlos A. Gómez Urda"
__copyright__   = "Copyright 2016"
__credits__     = ["Carlos A. Gómez Urda"]
__license__     = "GPL"
__version__     = "1.0"
__maintainer__  = "Carlos A. Gómez Urda"
__email__       = "carlosurda@yahoo.es"
__status__      = "Producción"
__date__        = "06/02/2016"

import bs4, urllib

while True:
    direccionWeb = raw_input( "Introduce la web: ").strip()
    if not direccionWeb: continue

    try:
        web = urllib.urlopen( direccionWeb)
    except:
        print "La dirección web no es correcta."
        continue

    break   

contenido = web.read()
sopa = bs4.BeautifulSoup( contenido, 'html.parser')

#print sopa

total = 0
cuenta = 0
for etiquetaTR in sopa( 'tr'):
    for etiquetaTD in etiquetaTR.findChildren( "td"):
        etiquetasSpan = etiquetaTD.findChildren( "span", {"class": "comments"})
        for etiquetaSpan in etiquetasSpan:
            cuenta += 1
            total += int( etiquetaSpan.string)

print "Cuenta", cuenta
print "Suma", total


