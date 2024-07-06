import time
import pyautogui
import pyperclip
import numpy as np
num = 120
time.sleep(1)
# Espera unos segundos para que puedas cambiar a la ventana de Chrome y el Bloc de Notas

pyautogui.keyDown('alt')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.keyUp('alt')

# Pestaña 1 en Chrome
pyautogui.hotkey('ctrl', '1')  # Cambiar a la pestaña 1
pyautogui.hotkey('ctrl', 'a')  # Seleccionar todo el contenido
pyautogui.hotkey('ctrl', 'c')  # Copiar al portapapeles

# Bloc de Notas
pyautogui.keyDown('alt')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.keyUp('alt')
pyautogui.hotkey('ctrl', 'v')  # Pegar el contenido

#for x in range(num):
# 2 y 102 dps
for x in np.arange(2,num):
    c = str(x)
    pyautogui.hotkey('alt', 'tab')  # Cambiar a la ventana de Bloc de Notas
    pyautogui.hotkey('ctrl','tab')  # Cambiar a la pestaña 1
    pyautogui.hotkey('ctrl', 'a')  # Seleccionar todo el contenido
    pyautogui.hotkey('ctrl', 'c')  # Copiar al portapapeles
    time.sleep(3)
    pyautogui.hotkey('alt', 'tab')  # Cambiar a la ventana de Bloc de Notas
    pyautogui.hotkey('ctrl', 't')  # Pegar el contenido
    pyautogui.hotkey('ctrl', 'v')  # Pegar el contenido
    time.sleep(3)    
    pyautogui.hotkey('ctrl', 'g')  # Pegar el contenido
    time.sleep(2)    
    pyautogui.write(c)  # Pegar el contenido
    pyautogui.hotkey('enter')  # Pegar el contenido
    pyautogui.hotkey('ctrl', 'w')  # Pegar el contenido