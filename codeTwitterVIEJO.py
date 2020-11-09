from selenium import webdriver
import time
import re
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datos
driver = webdriver.Chrome(executable_path=r"chromedriver.exe")

driver = datos.loginDS()
links =list()
linkRoobet = 'https://twitter.com/Roobet'
linkStreamer = 'https://twitter.com/SajuCSGO?s=20'
links.append(linkRoobet)
links.append(linkStreamer)
codigoViejo = ''
mensajeViejo = ''
#input("presione enter: ")

entro= False
codesGuardados=list()
cantidadDeTwits=2
fragmentosDeLinks=list()


for i in range(cantidadDeTwits):
    driver.execute_script(f"window.open('about:blank','{links[i]}');")
    driver.switch_to.window(links[i])
    driver.get(links[i])
    time.sleep(5)
fragmentosDeLinks.append(driver.window_handles[1])
fragmentosDeLinks.append(driver.window_handles[2])
while True:

        for i in range(cantidadDeTwits):
            print(fragmentosDeLinks[i])
            driver.switch_to.window(fragmentosDeLinks[i])
            html = driver.page_source
            soup = bs(html, "html.parser")

        mensajes = soup.findAll(class_="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0")
        #print(mensajes)
        for i in mensajes:
            codeNuevo = i.text
            mensajeNuevo = i.text
            #print(codeNuevo)
            if mensajeNuevo == mensajeViejo: continue
            mensajeViejo=mensajeNuevo
            if codeNuevo == codigoViejo : continue
            codigoViejo = codeNuevo
            try:
                if re.search('se code',codeNuevo) or re.search('.*(sajucsgo[0-9]+[a-z][0-9]+)',codeNuevo):
                    if re.search('.*(sajucsgo[0-9]+[a-z][0-9]+)',codeNuevo):
                        codeNuevo = re.findall('.*(sajucsgo[0-9]+[a-z][0-9]+)',codeNuevo)[0]
                    print('buenas!')
                    entro = True
                    break
                                                                
                else:
                    continue
            except:
                print(1)
                continue


        if entro == False: continue
        if codeNuevo in codesGuardados:continue
        codesGuardados.append(codeNuevo)
        #mandando al otro server:
        discord = driver.window_handles[0]
        driver.execute_script("window.open('about:blank', 'lazabot');")
        driver.switch_to.window("lazabot")
        driver.get('https://discord.com/channels/769427364362584104/769431300057858069')
        wait = WebDriverWait(driver, 60)
        element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'markup-2BOw-j')))
        driver.find_elements_by_class_name("markup-2BOw-j")[-1].send_keys(codeNuevo + Keys.ENTER)
        driver.switch_to.window(discord)  # para que vuelva al server inicial


