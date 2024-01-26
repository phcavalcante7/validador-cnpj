from validator import Validator # Importando a classe 
import json

v = Validator()
cnpj = str(input("Digite o CNPJ que deseja consultar:\n"))
result = v.validate(12, cnpj)   # consulta CNPJ G
result2 = v.validate(6, cnpj)   # consulta CNPJ D

if result != "None":  
    with open('data/cnpj-g.json', 'w', encoding='utf-8') as file:  # Escrevendo o JSON em um arquivo na pasta data
        json.dump(result, file, ensure_ascii=False, indent=4)      # Modelando o arquivo pra ficar mais legivel 

if result2 != "None":
    with open('data/cnpj-d.json', 'w', encoding='utf-8') as file:
        json.dump(result2, file, ensure_ascii=False, indent=4)
