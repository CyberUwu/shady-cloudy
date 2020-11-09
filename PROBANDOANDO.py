import re
import random
variable = ['malaso','xposed','attoficial']
diccionario = {"malaso": 'malaso', "xposed":'xposed', "att_oficial": 'attoficial', "erivillalva":'erivilla'}
s1 = ['promo code is malaso123a45,malaso178u69,malaso696e52', 'xposed123i45', 'attoficial2220']
textoEnviar = ''
directo = ''
arrayEnviar = list()


def mandarCode(mensaje,streamer, codeViejo):
    textoEnviar = ''
    if re.search(rf'.*({streamer}[0-9]+)',mensaje):
        if re.search(',',mensaje):
            array = re.findall(rf'({streamer}[0-9]+[a-z][0-9]+)', mensaje)
            print(array)
            print('-------------')
            for z in range (len(array)):
                if z == 0: 
                    textoEnviar += array[z]
                else:
                    if z == len(array): 
                        textoEnviar += array[z]
                    textoEnviar += ', ' + array[z]
    else:
        textoEnviar = codeViejo
            
    return(textoEnviar)
    

texto = random.choice(s1)

print(mandarCode(texto,'malaso', 'CODEVIEJOOOOO'))

#if re.search('.*(malaso[0-9]+[a-z][0-9]+)', str(texto)):
#    array = re.findall('(malaso[0-9]+[a-z][0-9]+)',str(texto))
#    for i in array:
#        envio = envio + i + ','
#print (envio)
