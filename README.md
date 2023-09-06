# Consulta de CEP

Este é um programa Python simples que permite ao usuário consultar informações de endereço com base em um CEP usando a API do ViaCEP. Ele usa a biblioteca `requests` para fazer a solicitação à API.

## Como Usar
1. Quando solicitado, insira um CEP válido.

2. O programa fará uma solicitação à API do ViaCEP, recuperará os detalhes do endereço e os exibirá no console.

## Comportamento

- Se o CEP for válido e for encontrado na API do ViaCEP, ele exibirá os detalhes do endereço, incluindo rua, bairro, UF e DDD.

- Se o CEP for inválido, o programa indicará que o CEP é inválido.

- Se o CEP não for encontrado na API do ViaCEP, o programa indicará que o CEP não foi encontrado.

## Requisitos

- Python 3.x
- Biblioteca `requests`
- Utilize `pip install -r requirements.txt` para instalar a versão mais recente da biblioteca
