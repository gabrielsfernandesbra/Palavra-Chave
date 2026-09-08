# Gerador de Senhas
### Aplicativo desktop para geração de senhas seguras, desenvolvido em Python utilizando CustomTkinter.
### O programa permite escolher o tamanho da senha e os tipos de caracteres utilizados:

#### Maiúsculas
#### Minúsculas
#### Números
#### Símbolos

As senhas são geradas utilizando o módulo secrets do Python.
___
Requisitos

Python 3.10 ou superior
CustomTkinter
PyInstaller (opcional, apenas para gerar o executável)
___
Instalação

Clone o repositório:
```
git clone https://github.com/gabrielsfernandesbra/Palavra-Chave.git
```
Entre na pasta do projeto:
```
cd Palavra-Chave
```
Crie um ambiente virtual:
```
python -m venv venv
```
Ative o ambiente virtual no Windows:
```
venv\Scripts\activate
```
Instale as dependências:
```
pip install -r requirements.txt
```
Execução

Para iniciar o programa, execute:
```
python app.py
```
Uso

Escolha o tamanho da senha.
Selecione os tipos de caracteres desejados.
Clique em "Gerar senha".
A senha será exibida na tela.
Clique em "Copiar" para copiar a senha.

O programa exige que pelo menos um tipo de caractere seja selecionado.

Quando mais de um tipo é selecionado, o programa garante que cada categoria escolhida apareça pelo menos uma vez na senha.

Geração do executável
___
Para gerar um executável para Windows utilizando PyInstaller:
```
pyinstaller --onefile --windowed --name "GeradorDeSenhas" app.py
```
O executável será criado na pasta:

dist/GeradorDeSenhas.exe

A pasta dist/ não é enviada ao GitHub, pois está incluída no .gitignore.
___
Estrutura do projeto
```
GeradorDeSenhas/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```
___
Segurança

O programa utiliza o módulo secrets para realizar a geração das senhas.

A geração ocorre localmente no computador e o aplicativo não precisa de conexão com a internet para funcionar.

Autor

### Gabriel S Fernandes
___
Aviso

Este projeto é fornecido "como está", sem garantias de qualquer tipo. O uso e a responsabilidade pelas senhas geradas são do usuário.

Copyright (c) 2026 Gabriel S Fernandes

Este projeto é distribuído sob os termos da licença MIT.
