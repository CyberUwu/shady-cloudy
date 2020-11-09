import requests
modoPrueba = False
if modoPrueba == True:
    URL_WEBHOOK = 'https://discordapp.com/api/webhooks/773555505859395585/XvgMUeEC-XRxIJ7y6Zp1QuVmqYKuJ18G99GAcc0POkFwozUDjqC670jCUspEI5rg1X0W'
else:
    URL_WEBHOOK = ' https://discord.com/api/webhooks/771892959150342176/iihI2sqKW4edhEJNpWewxvgaKXnAUTtdm4o9szDM1MYQGVIiGSUbjip1wtW9Elc2DpOE'

def mandarMensaje(mensaje, nombreBot):
    return requests.post(URL_WEBHOOK, json={
        "content" : mensaje,
        "username" : nombreBot,
        "avatar_url" :'https://i.imgur.com/IiRdnR0.jpg'
    }).text





