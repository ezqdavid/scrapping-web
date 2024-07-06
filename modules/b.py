import time
import pyautogui
import pyperclip
import numpy as np
num = 120
dir = 'view-source:https://www.zonaprop.com.ar/departamentos-alquiler-capital-federal-publicado-hace-menos-de-1-semana-pagina-'
#dir = 'view-source:https://www.zonaprop.com.ar/departamentos-venta-capital-federal-publicado-hace-menos-de-1-semana-pagina-'
#dir = 'view-source:https://www.zonaprop.com.ar/oficinas-comerciales-locales-comerciales-alquiler-capital-federal-publicado-hace-menos-de-1-mes-pagina-'
#dir = 'view-source:https://www.zonaprop.com.ar/inmueble-comercial-alquiler-capital-federal-publicado-hace-menos-de-1-mes-pagina-'
#dir = 'view-source:https://www.zonaprop.com.ar/casas-departamentos-ph-venta-capital-federal-desde-2-hasta-3-ambientes-mas-45-m2-menos-80000-dolar-pagina-'
dir2 = '.html'
pyautogui.hotkey('alt', 'tab')  # Cambiar a la ventana de Bloc de Notas
for x in np.arange(1,num):
    c = str(dir + str(x) + dir2)
    #time.sleep(1)
    # Número aleatorio entre 0 y 3 segundos
    random_sleep = np.random.uniform(1, 3)
    time.sleep(random_sleep)
    pyautogui.hotkey('ctrl', 't')  # Pegar el contenido
    pyautogui.write(c)  # Pegar el contenido
    pyautogui.press('enter')  # Presionar la tecla Enter al final