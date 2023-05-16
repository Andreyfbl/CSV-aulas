import json

lista = {
    'frutas': {'abacate':6.99,
               'uva': 7.99,
               'kiwi': 13.99},
    'data': '2023-05-20'
}

with open('arquivon.json', 'w') as arquivo:
    json.dump(lista, arquivo)
    meu_json = json.dumps(lista)

    print(meu_json)


