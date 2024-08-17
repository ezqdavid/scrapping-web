from src import Browser
from src.helpers.scrapping import *
from src.helpers.utils import *
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
import subprocess

#45.5.2.246:8084, 190.103.177.131:80, 200.71.237.238:23500, 209.13.186.20:80

load_dotenv()

URL_DEP_ALQUILERES = os.getenv("URL_DEP_ALQUILERES")
URL_DEP_VENTAS = os.getenv("URL_DEP_VENTAS")

segmento = "venta"

numero_alto = 10000
fechas = '020824-090824'#(datetime.today() - timedelta(days=7)).strftime("%d%m%y") + "-" + datetime.today().strftime("%d%m%y")
nombre_archivo = f'links_compilados/links_{segmento}_{fechas}.csv'

browser_dep_alq = Browser()

if segmento == "alq":
    if os.path.exists(nombre_archivo):
        scrape_data(browser_dep_alq, fechas, nombre_archivo)
    else:
        inicio, cant_pags = setear_cantidad_paginas(browser_dep_alq, URL_DEP_ALQUILERES, numero_alto, segmento, fechas)
        print("Cant_pags", inicio, cant_pags)

        leer_y_guardar_pags(URL_DEP_ALQUILERES, browser_dep_alq, cant_pags, segmento, fechas, inicio)

        print("obteniendo links de las páginas")
        listar_links_en_paginas(nombre_archivo, segmento, fechas)
        input("Links Obtenidos") # Para que el usuario pueda ver la cantidad de páginas y decidir si continuar o no


        scrape_data(browser_dep_alq, fechas, nombre_archivo)

        browser_dep_alq.driver.quit()
    
elif segmento == 'venta':
    inicio, cant_pags = setear_cantidad_paginas(browser_dep_alq, URL_DEP_VENTAS, numero_alto, segmento, fechas)
    print("Cant_pags", inicio, cant_pags)

    #leer_y_guardar_pags(URL_DEP_VENTAS, browser_dep_alq, cant_pags, segmento, fechas, inicio)

    print("obteniendo links de las páginas")
    #listar_links_en_paginas(nombre_archivo, segmento, fechas)
    input("Links Obtenidos") # Para que el usuario pueda ver la cantidad de páginas y decidir si continuar o no


    scrape_data(browser_dep_alq, fechas, nombre_archivo)

    browser_dep_alq.driver.quit()