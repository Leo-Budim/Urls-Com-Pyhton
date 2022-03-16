url = 'https://bytebank.com/cambio?moedadestino=dolar&moedaorigem=real'
#url = ""

#sanitização da URL
url = url.strip()
#ou url = url.replace(" ","")

#validação da URL


indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametro = url[indice_interrogacao+1:]

paramentro_busca = 'moedadestino'
indice_paramentro = url.find(paramentro_busca)
indice_valor = indice_paramentro + len(paramentro_busca) + 1
indice_e_comercial = url.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url[indice_valor:]
else:
    valor = url[indice_valor:indice_e_comercial]

print(url)
print(url_base)
print(url_parametro)
print(valor)