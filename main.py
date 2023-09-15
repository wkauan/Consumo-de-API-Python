import requests


def consulta_cep():
    cep = input('Informe um CEP: ')

    cep = cep.replace("-", "").replace(".", "").replace(" ", "")

    consulta = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

    return consulta
    

def tratamento_erro(consulta):
    if consulta.status_code == 200:
        requisicao = consulta.json()
        if 'erro' in requisicao:
            consulta.status_code = 404
            menssagem = 'CEP não encontrado \n'
        else:
            menssagem = 'Resultado da busca: \n'

            menssagem = f'O CEP informado foi: {requisicao["cep"]}.'

            menssagem = f'Endereço: {requisicao["logradouro"]}, {requisicao["bairro"]}, {requisicao["localidade"]} - {requisicao["uf"]} DDD: {requisicao["ddd"]} \n'
    else:
        menssagem = 'CEP Inválido \n'

    print('O status code é: ', consulta.status_code)
    print(menssagem)

tratamento_erro(consulta_cep())
