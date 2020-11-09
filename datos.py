import time
import re
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
def loginDS():
        linkDiscord = 'https://discord.com/login'
        discord_username = "pereltobias@icloud.com"
        discord_pwd = "rivercampeon04"
        print('Initializing Browser')
        preferences = {'download.prompt_for_download': 'false'}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', preferences)
        options.add_argument("--start-maximized")
        browser = webdriver.Chrome('chromedriver.exe', options=options)
        browser.get(linkDiscord)
        browser.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/input').send_keys(discord_username)
        browser.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input').send_keys(discord_pwd)
        browser.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]').click()
        time.sleep(2)
        return(browser)