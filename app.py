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
    }
]

##### Consultar Todas as Musicas #####

@app.route('/musics', methods=['GET']) #methods esta informando que eus so aceito o metodo GET
def get_musics():
    return jsonify(musics)#Retorna os livros em formato Json

##### Consultar Apenas uma Musica (com o ID) #####

@app.route('/musics/<int:id>', methods=['GET']) #<int:id> - Esta falando que eu espero um numero inteiro que sera nosso id
def get_musics_by_id(id):
    for music in musics: #o laço percorre o dicionario de livros
        if music.get('id') == id: #verifica se o id passado é igual ao id do liivro que o laço esta percorrendo
            return jsonify(music)
        
###### Adicionar nova Musica ######
#

@app.route('/musics', methods=['POST'])
def add_new_music():
    new_music = request.get_json() #request está pegando o novo valor e guardando em "new_music" 
    musics.append(new_music) #Adicona a nova musica no dicionario de musicas
    return jsonify(musics)

###### Editar Musica ######

@app.route('/musics/<int:id>', methods=['PUT'])
def edit_music_by_id(id):
    changes = request.get_json() 
    for indice, music in enumerate(musics):
        if music.get('id') == id: #Verifica o ID 
            musics[indice].update(changes) #Faz a substituição do valor (UPDATE) para o valor da variavel "changes"
            return jsonify(musics[indice]) #Retorna o valor alterado para o usuario
        
###### Deletar Musica ######

@app.route('/musics/<int:id>', methods=['DELETE'])
def delete_music_by_id(id):
    for indice, music in enumerate(musics):
        if music.get('id') == id: #Verifica o ID 
            del musics[indice]
    
    return jsonify(musics) #Retorna 

## Defindo o localhost
app.run(port=500, host='localhost', debug=True)