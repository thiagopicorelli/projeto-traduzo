# Traduzo

Aplicação feita no curso da Trybe do backend de Tradução, utilizando a API do Google Tradutor e feito em **Python**, utilizando o framework **Flask**. Ele utiliza um banco de dados pronto do **MongoDB** para salvar a lista de linguagens, e um frontend já pronto que foi editado e conectado com o backend produzido. Os testes também foram feitos pela Trybe.

## Arquivos trabalhados
[translate_controller.py](https://github.com/thiagopicorelli/projeto-traduzo/blob/main/src/controllers/translate_controller.py)
[language_model.py](https://github.com/thiagopicorelli/projeto-traduzo/blob/main/src/models/language_model.py)
[index.html](https://github.com/thiagopicorelli/projeto-traduzo/blob/main/src/views/templates/index.html)

## Setup
Utiliza Python 3.10.12 e docker-compose.

`python3 -m venv .venv && source .venv/bin/activate` para criar o ambiente virtual do projeto.

`python3 -m pip install -r dev-requirements.txt` para instalar.

`docker compose up translate` para iniciar o docker do banco de dados e do projeto.

`docker compose exec -it translate pytest` para iniciar os testes do projeto.

`localhost:8000` é a rota padrão.

## Linguagens e Frameworks
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
