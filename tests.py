import re
#mensaje = 'promo code is agusbob896^20x, agusbob80p56%0, agusbob91U$568, agusbobdepo9056Y#5'
#mensaje = 'agusbobdepo9056 la concha de tu madre29, agusbob trola de mierda, agusbobcomepitos'
mensaje = 'promo code is:agusbob896^20x'
prefijo = 'agusbob'
codeViejo = 'COMEME LAS 2 CONCHAS'

def recibirCode(mensaje,prefijo, codeViejo):
    textoEnviar = ''
    if re.search(rf'.*({prefijo}[0-9][0-9]+)',mensaje):
        if re.search(',',mensaje):
            array = re.findall(rf'({prefijo}[0-9][0-9]+.*)', mensaje)
            print(array)
            print('-------------')
            for z in range (len(array)):
                array[z] = array[z].strip(',')
                if z == 0: 
                    textoEnviar += array[z]
                else:
                    if z == len(array): 
                        textoEnviar += array[z]
                    textoEnviar += ', ' + array[z]
        else:
            array = re.findall(rf'({prefijo}[0-9][0-9]+.*)', mensaje)
            print(array)
            textoEnviar = array[0]
        # else:
        #     try:    
        #         code = re.findall(rf'.*({prefijo}[0-9]+[a-z][0-9]+)',mensaje)
        #         textoEnviar = code[0]
        #     except:
        #         code = re.findall(rf'.*({prefijo}[0-9]+)',mensaje)
        #         textoEnviar = code[0]
    else:
        textoEnviar = codeViejo
            
    return(textoEnviar)

print(recibirCode(mensaje,prefijo,codeViejo))