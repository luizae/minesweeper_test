## Robozin.py

Este é um automato escrito em **python**, utilizando **selenium**, para jogar um [campo minado](https://github.com/imakecodes/minesweeper-frontend).

Assumindo que você está utilizando **Ubuntu**:


> Necessário instalar **Selenium**

Com o [virtualenv](https://docs.python.org/pt-br/3/library/venv.html) instalado, execute no terminal 

`pip install -r requirements.txt`

> Necessário instalar **chromedriver**

Driver do navegador **chrome** necessário para executar a automação

Escolha uma dessas [versões](https://chromedriver.chromium.org/downloads), descompacte e mova o binário para
`/usr/bin/chromedriver`

---

## Para rodar a automação

Basta digitar `python robozin.py` e veja a mágica acontecer!

---

## Caso queira mudar os parâmetros

> Mudar quantidade de colunas

`set_rows.send_keys(x)`

> Mudar quantidade de linhas

`set_cols.send_keys(x)`

> Mudar quantidade de bombas

`set_mines.send_keys(x)`




