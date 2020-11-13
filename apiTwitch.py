import time
import re
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import requests
import json

diccionarioStreamer = [("inframe15", "inframe"),("agusbob", "agusbob"),("bgiulietti", "belula"),("bibaboy", "bibaboy"),("theblackjackgm", "thegm"),("bstrdd", "bstrdd"),("jizakude", "jizakude"),("candexnegri", "candenegri"),("capiow", "capiowo"),
                       ("caronigro", "caronigro"),("Carreraaa", "carreraaa"),("Cawelag", "cawelag"),("coloradaxx", "coloradaxx"),("elpibecs1", "elpibecs"),("erivillalva", "erivilla"),("Facubanzas", "facubanzas"),("Forg1", "forg"),
                       ("Francobertello74", "franco"),("frankkaster", "frankkaster"),("ggnia", "ggnia"),("Godeto", "godeto"),("hastad", "hastad"),("land1nf", "land1n"),("FossyGFX", "foss"),("deercheerup", "deercheerup"),("iberru", "iberru"),
                       ("immortal", "immortal"),("heyitsjoe", "joe"),("IvoXxX", "ivox"),("knut", "knut"),("lajefaok", "lajefa"),("lepajee", "lepajee"),("lucascristalino", "lukaslulo"),("luckraok", "luckra"),("luquitarodriguez", "luquitarodrigue"),
                       ("malaso", "Malaso"),("markitonavaja", "markiton"),("notdoom13", "doom"),("momoladinastia", "momo"),("Nanocs1", "nanocs"),("negrogatuxx", "negrogatux"),("ninhafps", "ninhafps"),("oAdanarg", "oadanarg"),("robergalati", "robertogalati"),
                       ("rojankhzxr", "rojankhzxr"),("yuyumartinez", "yuyumartinez"),("sajucasino", "sajucsgo"),("seleneitor", "seleneitor"),("Sionaron", "sionaron"),("submerzed", "submerzed"),("thebestiaoficial", "bestia"),("themasterrodrigo", "drigo"),
                       ("tuli_acosta", "tuliacosta"),("vgorefs", "vgorefs"),("vovo", "vovo"),("vroep", "vroep"),("xandfps", "xandfps"),("xposed", "xposed"),("RiiSki", "riiski"),("Sr_ThuliuM", "thulium"),("nosoynano", "nosoynano"),("frostezor", "frostezor"),
                       ("sksfps1", "sksfps"),("snugtoes", "snugtoes"),("jjuandamoli", "jjuandamoli"),("yungshapez", "shapez"),("Pulmonary0", "pulmonary"),("jasonr", "jasonr"),("att_oficial", "attoficial"),("cyberfocus", "cyberok"),("CABRA_SAFADO", "cabrasafadoxd"),
                       ("m0e_tv", "moe"),("atgoose", "goose"),("apoka", "apoka"),("carlosdleon", "carlosdleon"),("bldcs", "bld"),("juanpolo7l", "juanpolo"),("lucaslauriente10", "lucaslauriente"),("duxontv", "duxontv"),("rnakano", "nak"),("fedaaaa", "fedaaaa"),("kiuzinho", "kiuzinho"),
]


def api():

    headers = {
        "client-id": "ztiu0ovky0u70jxdj6qm6yq3gfv2kj",
        "Authorization": "Bearer lozf40azik5h579m2sepvp1t0y3mcp",
    }
    inactivos = list()
    for nombre in diccionarioStreamer:
        params = (("query", nombre[0]),)

        response = requests.get(
            "https://api.twitch.tv/helix/search/channels",
            headers=headers,
            params=params,
        )
        rjson = response.json()
        # print(rjson['data'][0]['game_id'],rjson['data'][0]['is_live'])

        if (
            rjson["data"][0]["game_id"] == "498566"
            or rjson["data"][0]["game_id"] == "29452"
            or rjson["data"][0]["game_id"] == "509658"
        ) and rjson["data"][0]["is_live"] == True:
            inactivos.append("activo")
        else:
            inactivos.append("inactivo")
    return inactivos


"""
lista=api()
print(lista)
"""
