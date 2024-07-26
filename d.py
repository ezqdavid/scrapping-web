from urllib.request import Request, urlopen, re	
import requests
from bs4 import BeautifulSoup 
import time
import numpy as np
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
links=['https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-2-3-ambientes-jardin-parrilla-53633270.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-villa-urquiza.-departamento-dos-ambientes-a-estrenar.-53622505.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-amoblado-a-estrenar-en-san-telmo-53629433.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-mirabilia-palermo-exclusivo-semipiso-4-ambientes-53629382.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-quantum-bellini-4-amb-c-dep-y-2-cocheras-piso-alto-53629337.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-en-venta-en-caballito-capital-federal-53622759.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-espectacular-departamento-en-caballito-de-3-ambientes-53628900.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-venta-departamento-2-dos-ambientes-villa-pueyrredon-53643422.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-venta-monoambiente-sarandi-200-balvanera-53648571.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-quantum-bellini-3-amb-con-cochera-piso-alto-con-53629336.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-depto.-venta.-3amb.-dependencia.-balcon.-baulera.-san-53649042.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-monoambiente-en-venta-en-belgrano-53653079.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-hermoso-3-ambientes-en-emprendimiento-de-categoria-en-53629264.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-semipiso-3-ambientes-frente-balcon-abasto-53649123.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-a-estrenar-53629454.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-en-venta-en-balvanera-capital-federal-53610517.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-zabal-urquiza-departamento-3-ambientes-al-frente-con-53629387.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-en-flores-2-ambientes-con-patio-y-53629349.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-hermoso-4amb-con-dependencia-y-cochera-en-almagro-53629439.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-dragones-1819.-piso-4-ambientes.-balcon-aterrazado-y-53647615.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-hermoso-departamento-en-caballito-4-ambientes-semipiso-53628901.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-3-amb-con-cochera-en-construccion-en-villa-crespo-53629340.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-2-ambientes-premium-amenities-de-53638530.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-espectacular-departamento-2-ambientes-en-fresias-53628904.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-2-ambientes-en-construccion-en-barracas-53629378.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-dragones-1819.-triplex-6-ambientes.-terraza-con-53647382.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-3-ambientes-con-balcon-aterrazado-y-53638134.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-en-villa-crespo-53629440.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-evoque-olazabal-venta-1amb-con-balcon-frances-y-53635815.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-4-ambientes-dependencia-floresta-53611088.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-monoambiente-almagro-norte-divisible-53607774.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-evoque-belgrano-triplex-4-ambientes-con-terraza-en-53629334.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-hermoso-monoambiente-con-balcon-terraza-y-vista-53629322.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-monoambiente.-venta.-saavedra.-estrenar.-cochera-53629549.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-hermoso-departamento-en-caballito-2-ambientes-premium-53628898.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-venta-de-departamento-de-3-ambientes-con-dependencia-53620487.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-3-ambientes-con-balcon-palermo-53653425.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-venta-departamento-2-amb.-con-balcon.-en-obra-a-53652548.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-dragones-1819.-duplex-5-ambientes.-terraza-con-piscina-53647391.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-4-ambientes-con-dependencia-de-servicio-53629464.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-en-venta-en-almagro-capital-federal-53635932.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-apto-credito-monoambiente-en-l-luminoso-nunez-53636592.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-2-ambientes-en-venta-amoblado-en-palermo-53608738.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-3-ambientes-en-construccion-en-barracas-53629311.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-venta-departamento-de-dos-ambientes-con-balcon-y-53653898.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-en-venta-en-palermo-capital-federal-53627198.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-hermoso-monoambiente-divisible-en-las-torres-de-53629263.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-2-ambientes-en-construccion-en-palermo-soho-53629304.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-en-venta-en-balvanera-capital-federal-53608165.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-monserrat-3-ambientes-dormitorio-suite-2-banos-cocina-53639638.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-en-las-canitas-3amb-patio-53629432.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-4-ambientes-con-dependencia-en-piso-alto-53629373.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-human-abasto-towers-3-ambientes-con-grandes-vistas-y-53629359.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-human-abasto-towers-2-ambientes-con-grandes-vistas-y-53629391.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-human-abasto-towers-3-ambientes-con-grandes-vistas-y-53629310.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-en-las-canitas-3amb-escritorio-piscina-53629444.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-monoambiente-en-la-torre-mas-importante-53629449.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-human-abasto-towers-2-ambientes-con-grandes-vistas-y-53629341.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-de-2-amb-en-pozo-en-palermo-53629338.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-en-edificio-en-palermo-soho-53629367.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-human-abasto-towers-3-ambientes-con-grandes-vistas-y-53629300.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-zabal-urquiza-departamento-2-ambientes-al-frente-con-53629441.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-de-4amb-en-pozo-en-palermo-53629434.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-2-ambientes-en-la-torre-de-almagro-53629372.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-de-4amb-en-pozo-en-palermo-53629417.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-human-abasto-towers-3-ambientes-con-grandes-vistas-y-53629351.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-a-estrenar-de-2amb-en-duplex-53629421.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-hermoso-departamento-de-2-ambientes-en-caballito-53629352.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-human-abasto-towers-2-ambientes-con-grandes-vistas-y-53629344.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-espectacular-departamento-de-4-ambientes-amenities-53629285.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-human-abasto-towers-2-ambientes-con-grandes-vistas-y-53629422.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-1-ambiente-con-balcon-y-vista-abierta-a-53629423.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-en-palermo-soho-53629308.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-2-ambientes-en-la-torre-mas-importante-de-53629277.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-human-abasto-towers-2-ambientes-con-grandes-vistas-y-53629462.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-de-2-amb-en-pozo-en-palermo-53629457.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-human-abasto-towers-2-ambientes-con-grandes-vistas-y-53629425.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-de-2amb-en-la-torre-mas-importante-de-53629280.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-4-ambientes-en-almagro-amenities-de-53629325.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-de-3-ambientes-en-villa-del-parque-53629427.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-de-2-amb-en-pozo-en-palermo-53629426.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-zabal-urquiza-departamento-2-ambientes-al-contra-53629386.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-venta.-semipiso-4-amb-c-dep-cochera-y-baulera.-53611174.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-venta-departamento-2-dos-ambientes-villa-pueyrredon-53643653.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-av-pueyrredon-800-duplex-piso-alto-53647271.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-en-pozo-53619321.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-3-ambientes-en-colegiales-53618165.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-venta-monoambinete-totalmente-refaccionado-en-canitas-53610723.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-en-san-cristobal-53638596.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento-en-san-nicolas-53610623.html','https://www.zonaprop.com.ar/propiedades/clasificado/veclapin-departamento.-venta.-monoambiente.-cochera.-saavedra.-53633440.html']
n=5000
fechas='100524-170524'
nombre='venta_' + fechas + '_objetos_2.csv'
nombre_aux='venta_' + fechas + '_objetos_aux_2.csv'
hdr = {'User-Agent': 'Mozilla/5.0'}			
for x in np.arange(0,n):
	site=links[x]
	n=x+1
	options = webdriver.chrome.options.Options()
	#options.add_argument("--headless")
	options.add_argument("--disable-gpu")
	options.add_experimental_option('excludeSwitches', ['enable-logging'])
	capabilities = DesiredCapabilities.CHROME.copy()
	capabilities['acceptSslCerts'] = True 
	capabilities['acceptInsecureCerts'] = True
	driver = webdriver.Chrome(options=options)
	driver.get(site)
	print("hola0")
	try:
		des = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "longDescription")))
	except:
		continue
	print("hola")
	source = driver.page_source
	bsObj1= BeautifulSoup(source,'html.parser')			
	global obj1			
	obj1=['Datos vacio']			
	for dat1 in bsObj1.findAll('ul', class_='section-icon-features'):			
		obj1=re.sub(r'\n\s*\n', r'\n\n', dat1.get_text().strip(), flags=re.M)		
	global obj2			
	obj2=['Desc vacio']			
	for dat2 in bsObj1.findAll('div', id='longDescription'):			
		obj2=re.sub(r'\n\s*\n', r'\n\n', dat2.get_text().strip(), flags=re.M)		
	global obj3			
	obj3=['Titulo vacio']
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
	global obj4			
	obj4=['Dir vacio']			
	for dat4 in bsObj1.findAll('div', class_='section-location-property'):			
		obj4=re.sub(r'\n\s*\n', r'\n\n', dat4.get_text().strip(), flags=re.M)		
	global obj5			
	obj5=['Cod anun']			
	for item0 in bsObj1.find_all(id='reactPublisherCodes', recursive=True): obj5.append(item0.get_text())			
	obj5 = [i1.replace('\n',' ') for i1 in obj5]		
	global obj6			
	obj6=['Precios vacio']			
	for dat6 in bsObj1.findAll('div', class_='price-value'):			
		obj6=re.sub(r'\n\s*\n', r'\n\n', dat6.get_text().strip(), flags=re.M)		
	global obj7			
	obj7=['Inmob vacio']			
	for dat7 in bsObj1.find('section', id='reactPublisherData'):			
		obj7=re.sub(r'\n\s*\n', r'\n\n', str(dat7), flags=re.M)		
	global obj8			
	obj8=['Premium vacio']			
	for dat8 in bsObj1.findAll('span', class_='publisher-premium-tag'):			
		obj8=re.sub(r'\n\s*\n', r'\n\n', dat8.get_text().strip(), flags=re.M)		
	global obj9			
	obj9=['Pubhace vacio']			
	for dat9 in bsObj1.findAll('div', class_='view-users-container'):
		obj9=re.sub(r'\n\s*\n', r'\n\n', dat9.get_text().strip(), flags=re.M)		
	global obj10			
	obj10=['Lat Long vacio']			
	dat10=bsObj1.find(id='static-map')			
	try:
		obj10=dat10.attrs['src']
	except AttributeError:
		continue
	global obj11			
	obj11=['Bajo precio vacio']			
	for dat11 in bsObj1.findAll('div', class_='block-discount block-row'):			
		obj11=re.sub(r'\n\s*\n', r'\n\n', dat11.get_text().strip(), flags=re.M)		
	global obj12			
	obj12=['Finalizado vacio']			
	for dat12 in bsObj1.findAll('div', class_='multimedia-offline-title'):			
		obj12=re.sub(r'\n\s*\n', r'\n\n', dat12.get_text().strip(), flags=re.M)		
	lista1=[]			
	for item1 in bsObj1.find_all('div', id='reactGeneralFeatures', recursive=True): lista1.append(item1.get_text())			
	lista1 = [i1.replace('\n',' ') for i1 in lista1]		
	global obj13			
	obj13=['Expensas vacio']			
	for dat13 in bsObj1.findAll('div', class_='price-extra'):			
		obj13=re.sub(r'\n\s*\n', r'\n\n', dat13.get_text().strip(), flags=re.M)	
	print('Aviso:', x, 'link:', site)
	print("post aviso 1")
	try:
		driver.close()
	except:
		continue
	print("post aviso 2")
	with open(nombre, 'a', newline='') as csvFile:			
		csvWriter = csv.writer(csvFile)		
		try:		
			csvWriter.writerow([site, obj1, obj2, lista1, obj3, obj4, obj5, [obj6], obj7, obj8, obj9, obj10, obj11, obj12, obj13])	
		except (NameError, TypeError, UnicodeEncodeError):		
			try:	
				csvFile2 = open (nombre_aux,'a', encoding='utf-8')
				csvWriter2 = csv.writer(csvFile2)
				csvWriter2.writerow([site, obj1, obj2, lista1, obj3, obj4, obj5, [obj6], obj7, obj8, obj9, obj10, obj11, obj12, obj13])
				csvFile2.close()
			except:
				continue
csvFile.close()