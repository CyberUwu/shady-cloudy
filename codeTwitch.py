import time
import re
import platform
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver




sistema = platform.system()

if sistema == 'Windows':
    driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
else:
    chromeOptions = Options()
    chromeOptions.headless = True
    driver = webdriver.Chrome(executable_path="./chromedriver",
    options=chromeOptions)
    
    
import funciones
import apiTwitch
import creacionBot

linkBase = 'https://www.twitch.tv/popout/'
linkExtra ='/chat?popout='

diccionarioStreamer = apiTwitch.diccionarioStreamer

cantidadCanales = len(diccionarioStreamer)
inactivos = list()
streamersActivos = list()

mensajeViejo = ''

codesNuevos = list()
codesNuevos = range(cantidadCanales)
codesViejos = list()
codesViejos = range(cantidadCanales)


#funcionesCodes =  ['code0', 'code1', 'code2', 'code3', 'code4', 'code5', 'code6', 'code7', 'code8', 'code9', 'code10', 'code11', 'code12', 'code13', 'code14', 'code15', 'code16', 'code17', 'code18', 'code19', 'code20', 'code21', 'code22', 'code23', 'code24', 'code25', 'code26', 'code27', 'code28', 'code29', 'code30', 'code31', 'code32', 'code33', 'code34', 'code35', 'code36', 'code37', 'code38', 'code39', 'code40', 'code41', 'code42', 'code43', 'code44', 'code45', 'code46', 'code47', 'code48', 'code49', 'code50', 'code51', 'code52', 'code53', 'code54', 'code55', 'code56', 'code57', 'code58', 'code59', 'code60', 'code61', 'code62','code63']
delay = time.time() + 60*15
contador = 0
glosario=list()
codigoEnviado=''

while True:
    try:
        if time.time() >=delay or contador == 0:
            streamersActivos.clear()
            if contador != 0: 
                driver.quit()
            contador+=1
            delay = time.time() + 60 * 15
            #interacion = 0
            
            if sistema == 'Windows':
                driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
            else:
                chromeOptions = Options()
                chromeOptions.headless = True
                driver = webdriver.Chrome(executable_path="./chromedriver",
                options=chromeOptions)
            
            print('yendo api twitch')
            inactivos = apiTwitch.api()
            print(inactivos)
            print(inactivos.count('activo'))

            for i in range(len(inactivos)):
                if inactivos[i] == 'activo':
                    print(diccionarioStreamer[i][0])
                    streamersActivos.append(diccionarioStreamer[i][0])

            for i in range(cantidadCanales):
                if (inactivos[i] == 'inactivo'): continue
                driver.execute_script(f"window.open('about:blank','{diccionarioStreamer[i][0]}');")
                driver.switch_to.window(diccionarioStreamer[i][0])
                driver.get(linkBase + str(diccionarioStreamer[i][0]) + linkExtra)
        else:
            for i in range(cantidadCanales):
                if(inactivos[i] == 'inactivo'): continue
                try:
                    driver.switch_to.window(diccionarioStreamer[i][0])
                    html = driver.page_source
                    soup = bs(html, "html.parser")
                    mensajes = soup.findAll(class_='text-fragment')
                    texto = mensajes[-1].text
                    #print(texto)
                except:
                    #print(1000000000000)
                    continue
                if (mensajeViejo == mensajes): continue
                mensajeViejo = mensajes
                #streamer = getattr(funciones, funcionesCodes[i])  # get attributte
                codesNuevos = funciones.recibirCode(texto, diccionarioStreamer[i][1],codesViejos[i])
                if codesNuevos is glosario:continue
                
                #glosario.append(codesNuevos)
                #print(glosario)
                if type(codesNuevos) == int: continue
                print('hay code muchachos!')
                try:
                    if codigoEnviado==codesNuevos: continue
                    codigoEnviado=codesNuevos
                    creacionBot.mandarMensaje(codesNuevos,'CyberBot')
                except:
                    print(1)
    except:
        continue
