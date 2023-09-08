import requests

def consulta_cep():
    cep = input('Informe um CEP: ')

    cep = cep.replace("-", "").replace(".", "").replace(" ", "")

    consulta = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

    if consulta.status_code == 200:
        requisicao = consulta.json()
        if 'erro' in requisicao:
            consulta.status_code = 404
            print('O status code é: ', consulta.status_code)

            print('CEP Não encontrado \n')
        else: 
            print('O status code é: ', consulta.status_code)

            uf = requisicao['uf']
            endereco = requisicao['logradouro']
            bairro = requisicao['bairro']
            ddd = requisicao['ddd']
            cidade = requisicao['localidade']

            print('Resultado da busca: \n')

            print('O CEP informado foi: %s.' % requisicao['cep'])

            print('Endereço: %s, %s, %s - %s DDD: %s \n' % (endereco, bairro, cidade, uf, ddd))
    elif consulta.status_code == 400:
        print('O status code é: ', consulta.status_code)

        print('CEP Inválido \n')

consulta_cep()
