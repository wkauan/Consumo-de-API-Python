import requests

def consulta_cep():
    cep = input('Informe um CEP: ')

    consulta = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    requisicao = consulta.json()

    if requisicao['erro']:
        consulta.status_code = 404
        
        print('O status code é: ', consulta.status_code)

        print('CEP Não encontrado \n')
    elif consulta.status_code == 400:
        print('O status code é: ', consulta.status_code)

        print('CEP Inválido \n')
    elif consulta.status_code == 200:
        print('O status code é: ', consulta.status_code)

        uf = requisicao['uf']
        rua = requisicao['logradouro']
        bairro = requisicao['bairro']
        ddd = requisicao['ddd']

        print('Resultado da busca: \n')

        print('O CEP informado foi: %s.' % cep)

        print('Rua: %s, Bairro: %s, UF: %s, DDD: %s \n' % (rua, bairro, uf, ddd))

consulta_cep()
