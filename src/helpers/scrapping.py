import glob
from bs4 import BeautifulSoup
import re
import pandas as pd
from .utils import normalizar_string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def leer_y_guardar_pags(URL, driver, numero_actual_pags, segmento, fechas, inicio):
    """
    This function reads and saves web pages.

    Args:
        URL (str): The base URL of the web pages.
        driver: The web driver object.
        numero_actual_pags (int): The number of pages to read and save.

    Returns:
        None
    """
    if os.path.exists(f"paginas/{segmento}_{fechas}") == False:
        os.makedirs(f"paginas/{segmento}_{fechas}")
    for x in range(inicio, int(numero_actual_pags)+1):
        driver.get(str(URL) + str(x) + ".html")
        with open(f"paginas/{segmento}_{fechas}/"+ str(x) + ".txt", "w", encoding='utf-8') as f:
            f.write(driver.page_source)
        f.close()

def setear_cantidad_paginas(self, url, numero_alto, segmento, fechas):
    """
    Sets the number of pages based on the given URL and high number.

    Args:
        url (str): The base URL.
        numero_alto (int): The high number.

    Returns:
        str: The modified URL without the base URL and file extension.
    """
    existe_directorio = os.path.exists(f"paginas/{segmento}_{fechas}")
    self.get(str(url) + str(numero_alto) + ".html")
    cantidad_total = self.driver.current_url.replace(url[12:], "").replace(".html", "")

    if existe_directorio:
        cantidad_ejecutado = glob.glob(f"paginas/{segmento}_{fechas}/*.txt")
        return  len(cantidad_ejecutado), int(cantidad_total)
    else:
        return 1, int(cantidad_total)
    

def listar_links_en_paginas(nombre_archivo_alq, segmento, fechas):
    """
    Extracts links from HTML files in the 'paginas' directory and saves them to a CSV file.

    Args:
        nombre_archivo_alq (str): The name of the CSV file to save the extracted links.

    Returns:
        None
    """
    files = glob.glob(f"paginas/{segmento}_{fechas}/*.txt")
    df = pd.DataFrame(columns=['n', 'href'])
    for n, f in enumerate(files):
        with open(f, encoding='utf-8') as csv_file:
            bsObj = BeautifulSoup(csv_file, 'html.parser')
            for link in bsObj.findAll('a', attrs={'href': re.compile(r'^/propiedades/clasificado/[A-Za-z0-9\.\_\-+]+\.(html)(?!\#map)')}):
                newPage = link.attrs['href']
                df.loc[len(df.index)] = [n+1, newPage]

    print("Sin eliminar duplicados", df.shape[0])
    df.drop_duplicates(subset=['href'], inplace=True)
    print("Eliminando duplicados", df.shape[0])
    df['href'] = 'https://www.zonaprop.com.ar' + df['href']
    df.to_csv(nombre_archivo_alq, index=False)



def scrape_data(driver, fechas, nombre_archivo_alq):
    """
    Scrapes data from a list of links using a web driver.

    Args:
        driver: The web driver object.
        fechas: The date string used in the file name.

    Returns:
        None
    """
    df_links = pd.read_csv(nombre_archivo_alq, usecols=['href'])
    nombre = f'alq_{fechas}_objetos.csv'
    data = []  # List to store extracted data as dictionaries

    links = df_links['href'].tolist()
    if os.path.exists(nombre):
        df_previo = pd.read_csv(nombre, sep=";")
        #skip the links that are already in the file
        links = [x for x in links if x not in df_previo['site'].tolist()]
    links = links[500:]
    print(len(links))
    for i, site in enumerate(links):  # Iterate through the links
        driver.get(str(site))
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "longDescription")))
        except:
            pass

        bsObj1 = BeautifulSoup(driver.page_source, 'html.parser')

        obj1='Datos vacio'		
        for dat1 in bsObj1.findAll('ul', class_='section-icon-features'):			
            obj1=re.sub(r'\n\s*\n', r'\n\n', dat1.get_text().strip(), flags=re.M)		
        obj2='Desc vacio'	
        for dat2 in bsObj1.findAll('div', id='longDescription'):			
            obj2=re.sub(r'\n\s*\n', r'\n\n', dat2.get_text().strip(), flags=re.M)		
        obj3='Titulo vacio'
        try:
            title_element = bsObj1.find('h1', class_='title-property')
            if title_element:
            # If the element is found, iterate over it
                for dat3 in title_element:
                    obj3 = re.sub(r'\n\s*\n', r'\n\n', dat3, flags=re.M)
                    break
        except:
            title_element = bsObj1.find('h1', class_='title-property')
            if title_element:
        # If the element is found, iterate over it
                for dat3 in title_element:
                    obj3 = re.sub(r'\n\s*\n', r'\n\n', dat3, flags=re.M)
                    break
        obj4='Dir vacio'		
        for dat4 in bsObj1.findAll('div', class_='section-location-property'):			
            obj4=re.sub(r'\n\s*\n', r'\n\n', dat4.get_text().strip(), flags=re.M)		
        obj5=['Cod anun']			
        for item0 in bsObj1.find_all(id='reactPublisherCodes', recursive=True): obj5.append(item0.get_text())			
        obj5 = [i1.replace('\n',' ') for i1 in obj5]		
        obj6='Precios vacio'		
        for dat6 in bsObj1.findAll('div', class_='price-value'):			
            obj6=re.sub(r'\n\s*\n', r'\n\n', dat6.get_text().strip(), flags=re.M)		
        obj7='Inmob vacio'	
        for dat7 in bsObj1.find('section', id='reactPublisherData'):			
            obj7=re.sub(r'\n\s*\n', r'\n\n', str(dat7), flags=re.M)		
        obj8='Premium vacio'		
        for dat8 in bsObj1.findAll('span', class_='publisher-premium-tag'):			
            obj8=re.sub(r'\n\s*\n', r'\n\n', dat8.get_text().strip(), flags=re.M)		
        obj9='Pubhace vacio'		
        for dat9 in bsObj1.findAll('div', class_='view-users-container'):
            obj9=re.sub(r'\n\s*\n', r'\n\n', dat9.get_text().strip(), flags=re.M)		
        obj10='Lat Long vacio'	
        dat10=bsObj1.find(id='static-map')			
        try:
            obj10=dat10.attrs['src']
        except AttributeError:
            continue
        obj11='Bajo precio vacio'		
        for dat11 in bsObj1.findAll('div', class_='block-discount block-row'):			
            obj11=re.sub(r'\n\s*\n', r'\n\n', dat11.get_text().strip(), flags=re.M)		
        obj12='Finalizado vacio'		
        for dat12 in bsObj1.findAll('div', class_='multimedia-offline-title'):			
            obj12=re.sub(r'\n\s*\n', r'\n\n', dat12.get_text().strip(), flags=re.M)		
        lista1=[]			
        for item1 in bsObj1.find_all('div', id='reactGeneralFeatures', recursive=True): lista1.append(item1.get_text())			
        lista1 = [i1.replace('\n',' ') for i1 in lista1]		
        obj13='Expensas vacio'	
        for dat13 in bsObj1.findAll('div', class_='price-extra'):			
            obj13=re.sub(r'\n\s*\n', r'\n\n', dat13.get_text().strip(), flags=re.M)	

        print('Aviso:', i, 'link:', site)

        data = []
        data.append({
            'site': site.strip(),
            'obj1': normalizar_string(obj1),
            'obj2': normalizar_string(obj2),
            'lista1':  str(lista1).replace("[", "").replace("]", ""),
            'obj3': normalizar_string(obj3),
            'obj4': normalizar_string(obj4),
            'obj5': str(obj5).replace("[", "").replace("]", ""), #lista
            'obj6': normalizar_string(obj6),
            'obj7': normalizar_string(obj7),
            'obj8': normalizar_string(obj8), 
            'obj9': normalizar_string(obj9),
            'Lat Long': normalizar_string(obj10),
            'Bajo precio': normalizar_string(obj11), 
            'Finalizado': normalizar_string(obj12), 
            'Expensas': normalizar_string(obj13),
        })
        #save dinamicaly
        if os.path.exists(nombre):
            df_previo = pd.read_csv(nombre, sep=";")
            df = pd.DataFrame(data)
            df_previo = pd.concat([df_previo, df], ignore_index=True)
            df_previo.to_csv(nombre,na_rep=' ', index=False, sep=";", encoding="UTF-8")
        else:
            df = pd.DataFrame(data)
            df.to_csv(nombre,na_rep=' ', index=False, sep=";", encoding="UTF-8")
