# ImgMorph

Projeto simples de conversor de tipos de imagem com backend em Flask e frontend em HTML, CSS e JavaScript.

---

## Como rodar

### Backend

1. Navegue até a pasta `backend`:

```bash
cd backend
````

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Rode o servidor Flask:

```bash
flask run
```

O backend estará disponível em `http://localhost:5000`.

---

### Frontend

Você pode abrir o arquivo `frontend/index.html` diretamente no navegador ou rodar um servidor local para evitar problemas de CORS.

Para rodar um servidor simples usando Python, execute:

```bash
cd frontend
python -m http.server 8000
```

Depois, abra no navegador:

```
http://localhost:8000
```

---

## Estrutura do projeto

```
ImgMorph/
├── backend/
│   ├── app.py
│   ├── requirements.txt
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── .gitignore
├── README.md
└── launch.json
```

---

## Funcionalidades

* Upload de imagens nos formatos PNG, JPG, JPEG, GIF e BMP.
* Conversão da imagem para outro formato escolhido pelo usuário.
* Download da imagem convertida.

---

## Dependências principais

* Flask
* Pillow
* Flask-CORS (para permitir requisições do frontend)