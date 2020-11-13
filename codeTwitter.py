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

import creacionBot

sistema = platform.system()

if sistema == 'Windows':
    driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
else:
    chromeOptions = Options()
    chromeOptions.headless = True
    driver = webdriver.Chrome(executable_path="./chromedriver",
    options=chromeOptions)
    
entro = False
codesGuardados=list()
codigoViejo = ''
mensajeViejo = ''
driver.get('https://twitter.com/Roobet')
delay = time.time() + 15

while True:
    html = driver.page_source
    soup = bs(html, "html.parser")
    # print(soup)
    if time.time() >= delay:
        delay = time.time() + 15
        driver.refresh()
    mensajes = soup.findAll(class_="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0")
    #print(mensajes)
    #    print(1)
    print('Esta funcionando pa!!')
    for i in mensajes:
        codeNuevo = i.text
        mensajeNuevo = i.text
        #print(codeNuevo)
        if mensajeNuevo == mensajeViejo: continue
        mensajeViejo=mensajeNuevo
        if codeNuevo == codigoViejo : continue
        codigoViejo = codeNuevo
        try:
            if re.search('se code',codeNuevo):
                print('buenas!')
                entro = True
                break
            else:
                continue
        except:
            print(1)
            continue


    if entro == False: continue
    if codeNuevo in codesGuardados: continue
    codesGuardados.append(codeNuevo)
    #mandando al otro server:
    creacionBot.mandarMensaje(codeNuevo,'CyberBot')