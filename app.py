from flask import Flask, jsonify, request

app = Flask(__name__)

musics = [
    {
        'id': 1,
        'name': 'CHIHIRO',
        'singer': 'Billie Eilish'
    },
    {
        'id': 2,
        'name': 'So American',
        'singer': 'Olivia Rodrigo'
    },
    {
        'id': 3,
        'name': 'MALAMENTE',
        'singer': 'Rosalia'
    },
    {
        'id': 4,
        'name': 'Moth To A Flame',
        'singer': 'The Weekend'
    },
    {
        'id': 5,
        'name': 'Kill Bill',
        'singer': 'SZA'
    },
]

### Consultar Todas as Musicas

### Consultar Apenas uma Musica (com o ID)

### Adicionar nova Musica

### Editar Musica 

### Deletar Musica

## Defindo o localhost
app.run(port=500, host='localhost', debug=True)