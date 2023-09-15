# Consulta de CEP

Este é um programa Python que permite ao usuário consultar informações de endereço com base em um CEP usando a API do ViaCEP. Usando a biblioteca `requests` para fazer a solicitação à API.

## Requisitos

- Instale o Python 3.x em `https://www.python.org/downloads/`
- Utilize `git clone https://github.com/wkauan/Consumo-de-API-Python.git` para baixar o repositório
- Utilize `pip install -r requirements.txt` para instalar a versão mais recente da biblioteca `requests`

## Como Usar

- Use o comando `python main.py` para iniciar.
    1. Quando solicitado, insira um CEP válido.

    2. O programa fará uma solicitação à API do ViaCEP, recuperará os detalhes do endereço e os exibirá no console.

## Comportamento

- Se o CEP for válido e for encontrado na API do ViaCEP, ele exibirá os detalhes do endereço, incluindo rua, bairro, cidade, UF e DDD.

- Se o CEP for inválido, o programa indicará que o CEP é inválido.

- Se o CEP não for encontrado na API do ViaCEP, o programa indicará que o CEP não foi encontrado.
