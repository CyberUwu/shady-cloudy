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
driver.get('https://web.telegram.org')
input('presione enter: ')
driver.get('https://web.telegram.org/#/im?p=@roobetcom')
codigoViejo = ''
mensajeViejo = ''
input("presione enter: ")
while True:

    try:

        html = driver.page_source
        soup = bs(html, "html.parser")
        #print(soup)
        mensajes = soup.findAll(class_="im_message_text")
        codeNuevo = mensajes[-1].text
        mensajeNuevo = mensajes[-1].text
        if mensajeNuevo == mensajeViejo: continue
        print(mensajeNuevo)
        mensajeViejo=mensajeNuevo
        if codeNuevo == codigoViejo : continue
        if not re.search('code',str(codeNuevo)):
            print('No es code')
            continue
        codeNuevo = re.findall('.ode: ([a-z]+[0-9]+[a-z][0-9]+).',codeNuevo)
        print(codeNuevo)
        codigoViejo = codeNuevo
    except:
        continue

    #mandando al otro server:

    discord = driver.window_handles[0]
    driver.execute_script("window.open('about:blank', 'lazabot');")
    driver.switch_to.window("lazabot")
    driver.get('https://discord.com/channels/769427364362584104/769431300057858069')
    wait = WebDriverWait(driver, 60)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'markup-2BOw-j')))
    driver.find_elements_by_class_name("markup-2BOw-j")[-1].send_keys(codeNuevo[0] + Keys.ENTER)
    driver.switch_to.window(discord)  # para que vuelva al server inicial
    try:
        discord = driver.window_handles[0]
        driver.execute_script("window.open('about:blank', 'lazabot');")
        driver.switch_to.window("lazabot")
        driver.get('https://discord.com/channels/769427364362584104/769431300057858069')
        wait = WebDriverWait(driver, 60)
        element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'markup-2BOw-j')))
        driver.find_elements_by_class_name("markup-2BOw-j")[-1].send_keys(codeNuevo[-1] + Keys.ENTER)
        driver.switch_to.window(discord)  # para que vuelva al server inicial
    except:
        pass


