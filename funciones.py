import re
def recibirCode(mensaje,prefijo, codeViejo):
    textoEnviar = ''
    if re.search(rf'.*({prefijo}[0-9]+)',mensaje):
        if re.search(',',mensaje):
            array = re.findall(rf'({prefijo}[0-9]+[a-z][0-9]+)', mensaje)
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
            try:    
                code = re.findall(rf'.*({prefijo}[0-9]+[a-z][0-9]+)',mensaje)
                textoEnviar = code[0]
            except:
                code = re.findall(rf'.*({prefijo}[0-9]+)',mensaje)
                textoEnviar = code[0]
    else:
        textoEnviar = codeViejo
            
    return(textoEnviar)