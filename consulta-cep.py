import requests
import json


print("\n"+17*"="+"CONSULTA CEP"+17*"=")
    
cep = input("\nDigite o cep: ")
local = "https://viacep.com.br/ws/{}/json/".format(cep)
obj_url = requests.get(local, headers={"chave-api-dados": "8c2190bf68ad4f00a4bcbf60df1fe44f"})
ce = obj_url.json()
print("CEP: %s"%ce['cep'])
print("Logradouro: %s"%ce["logradouro"])
print ("Complemento: %s"%ce['complemento'])
print("Bairro: "+ce['bairro'])
print ("Município: "+ce['localidade'])
print('uf: '+ce['uf'])
print('Ibge: '+ce['ibge'])
print ("Gia: "+ce["gia"])
print("ddd: "+ce["ddd"])