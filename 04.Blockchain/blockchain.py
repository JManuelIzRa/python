#Importamos todos los modulos necesarios.
import sys

import hashlib
import json

from time import time
from uuid import uuid4

from flask import Flask, jsonify, request

import requests
from urllib.parse import urlparse

#Declaramos la clase
class Blockchain(object):

    difficulty_target = "0000"

    def hash_block(self,block):
        block_encoded = json.dumps(block, sort_keys=True).encode()
        
        return hashlib.sha256(block_encoded).hexdigest()

    def __init__(self):
        #Almacena todos los bloques de la blockchain
        self.chain = []

        #Temporalmente almacena las transacciones para el bloque actual
        self.current_transactions = []

        #Crea el genesis block con un hash especifico que comienza con índice 0
        genesis_hash = self.hash_block("genesis_block")

        self.append_block(
            hash_of_previus_block = genesis_hash,
            nonce = self.proof_of_work(0, genesis_hash, [])
        )

        #hash_block() codifica un bloque en un array de bytes y luego el aplica un hash; 
        #es necesario asegurar que el diccionario está ordenado, de lo contrario puede haber hashes inconsistentes.

    #El nonce es un número arbitrario que solo puede utilizarse una vez.

    #Usamos PoW para encontrar el nonce para el bloque
    def proof_of_work(self, index, hash_of_previus_block, transactions):

        #Lo intentamos con nonce = 0
        nonce = 0

        #Intentamos crear un hash juntando el nonce con el hash del anterior nodo hasta que este sea válido
        while self.valid_proof(index, hash_of_previus_block, transactions, nonce) is False:
            nonce += 1

        return nonce
            
    
    def valid_proof(self, index, hash_of_previus_block, transactions, nonce):

        #Creamos una cadena de caracteres que contenga el hash del nodo anterior y el contenido del bloque incluyendo el nonce
        content = f'{index}{hash_of_previus_block}{transactions}{nonce}'.encode()

        #Creamos el hash usando sha256
        content_hash = hashlib.sha256(content).hexdigest()

        #Comprobamos que el hash se encuentre en la dificultad objetivo
        return content_hash[:len(self.difficulty_target)] == self.difficulty_target


    #Creamos un nuevo bloque y lo añadimos a la blockchain
    def append_block(self, nonce, hash_of_previus_block):

        block = {
            'index': len(self.chain),
            'timestamp':time(),
            'transactions':self.current_transactions,
            'nonce':nonce,
            'hash_of_previus_block':hash_of_previus_block
        }

        #Reseteamos la lista actual de transacciones
        self.current_transactions = []

        #Añadimos el nuevo bloque a la blockchain
        self.chain.append(block)
        return block

    #Añadimos las transacciones
    def add_transaction(self, sender, recipient, amount):
        
        self.current_transactions.append({
            'amount':amount,
            'recipient':recipient,
            'sender':sender,
        })

        return self.last_block['index'] + 1

    
    @property
    def last_block(self):
        #devuelve el último bloque de la blockchain
        return self.chain[-1]


#La clase Blockchain ya está completa, lo siguiente es exponerla como una REST API usando Flask.
app = Flask(__name__)

#generamos una direccion unica para este nodo
node_identifier = str(uuid4()).replace('-','')

#instanciamos la Blockchain
blockchain = Blockchain()

#Obtenemos toda la blockchain
@app.route('/blockchain', methods=['GET'])

def full_chain():
    response = {
        'chain':blockchain.chain,
        'length':len(blockchain.chain),
    }

    return jsonify(response), 200

#Es necesario que creemos una ruta para que los mineros minen los bloques para que puedan ser añadidos a la blockchain
@app.route('/mine', methods = ['GET'])

def mine_block():
    blockchain.add_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1,
    )

    #Obtenemos el hash del ultimo bloque de la blockchain
    last_block_hash = blockchain.hash_block(blockchain.last_block)

    #Usando PoW, obtenemos el nonce para el nuevo bloque que será añadido a la blockchain
    index = len(blockchain.chain)

    nonce = blockchain.proof_of_work(index, last_block_hash, blockchain.current_transactions)

    #Añadimos el nuevo bloque a la blockchain usando el hash del ultimo bloque y el nonce del actual
    block = blockchain.append_block(nonce, last_block_hash)

    response = {
        'message':"Nuevo bloque minado",
        'index':block['index'],
        'hash_of_previus_block':block['hash_of_previus_block'],
        'nonce':block['nonce'],
        'transactions':block['transactions'],
    }

    return jsonify(response),200


#Creamos una nueva ruta para que la API pueda añadir transacciones al bloque actual
@app.route('/transactions/new',methods = ['POST'])

def new_transaction():

    #Obtiene el valor que envia el cliente
    values = request.get_json()

    #Verificamos que los campos obligatorios esten en los datos de POST
    requiered_fields = ['sender','recipient','amount']

    if not all(k in values for k in requiered_fields):
        return ('Faltan campos',400)

    #Si todo es correcto se crea una nueva transaccion
    index = blockchain.add_transaction(
        values['sender'],
        values['recipient'],
        values['amount']
    )

    response = {'mensaje':f'La transaccion sera añadida al bloque {index}'}

    return (jsonify(response), 201)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(sys.argv[1]))