# Program to make a blockchain
    # Import the necessary modules
from asyncio.base_futures import _format_callbacks
import hashlib
import json
from time import time
from uuid import uuid4
from urllib.parse import urlparse
from numpy import append
import requests

from flask import Flask, jsonify, request

class Blockchain:
    
    # Function to create the blockchain
    def __init__(self):       
        self.current_transactions = []      # List of current transactions
        self.chain = []                      # List of all blocks
        self.nodes = set()                   # List of all nodes
        # Create the genesis block
        self.new_block(previous_hash='1', proof=100)
    
    # Function to create a new block
    def new_block(self, proof, previous_hash=None):
        # Create a new block
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        # Reset the current list of transactions
        self.current_transactions = []
        # Append the block to the chain
        self.chain.append(block)
        # Return the new block
        return block
    
    # Function to create a new transaction
    def new_transaction(self, sender, recipient, amount):
        # Add the transaction to the list of transactions
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        # Return the index of the block that will hold this transaction
        return self.last_block['index'] + 1
    
    # Function to hash a block
    @staticmethod
    def hash(block):
        # Dictionary to be hashed
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    # Function to get the last block
    @property
    def last_block(self):
        return self.chain[-1]
    
    # Function to proof of work
    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof
    
    # Function to check if the proof is valid
    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
    
    # Function to register a node
    def register_node(self, address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)
    
    # Function to resolve conflicts
    def resolve_conflicts(self):
        neighbours = self.nodes
        new_chain = None
        # Get the length of the chain
        max_length = len(self.chain)
        # Loop through all the nodes
        for node in neighbours:
            # Make a request for the chain
            response = requests.get(f'http://{node}/chain')
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']
                # Check if the length is longer and the chain is valid
                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain
        # Replace the chain if there is a new valid chain
        if new_chain:
            self.chain = new_chain
            return True
        return False
    
    # Function to check if the chain is valid
    @staticmethod
    def valid_chain(chain):
        last_block = chain[0]
        current_index = 1
        while current_index < len(chain):
            block = chain[current_index]
            # Check if the hash of the block is correct
            if block['previous_hash'] != Blockchain.hash(last_block):
                return False
            # Check if the proof of work is correct
            if not Blockchain.valid_proof(last_block['proof'], block['proof']):
                return False
            last_block = block
            current_index += 1
        return True
    
    # Function to get the nodes
    @staticmethod
    def get_nodes():
        return list(Blockchain.nodes)
    
    # Function to get the last proof
    @staticmethod
    def get_last_proof():
        return Blockchain.last_block['proof']
    
    # Function to get the last hash
    @staticmethod
    def get_last_hash():
        return Blockchain.last_block['previous_hash']
    
    # Function to get the last block
    @staticmethod
    def get_last_block():
        return Blockchain.last_block
    
    # Function to get the current transactions
    @staticmethod
    def get_current_transactions():
        return Blockchain.current_transactions
    
    # Function to get the chain
    @staticmethod
    def get_chain():
        return Blockchain.chain
    
    # Function to get the length of the chain
    @staticmethod
    def get_length():
        return len(Blockchain.chain)
    
    # Function to create a new blockchain
    def create_blockchain():
        # Create a new blockchain
        blockchain = Blockchain()
        # Return the blockchain
        return blockchain

    # Create a new node
    def create_node(address):
        # Create a new node
        parsed_url = urlparse(address)
        return parsed_url.netloc
        # End of function

    # Function to add a node
    def add_node(self, address):
        # Create a new node
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)
        # End of function

    # Function to remove a node
    def remove_node(self, address):
        # Create a new node
        parsed_url = urlparse(address)
        self.nodes.remove(parsed_url.netloc)
        # End of function
    
# Main program
if __name__ == '__main__':
    # Create a new blockchain
    blockchain = Blockchain.create_blockchain()
    # Create a new node
    node = Blockchain.create_node('http://
    # Add the node to the blockchain
    blockchain.add_node(node)
    # Print the chain
    print(blockchain.get_chain())
    # Print the length of the chain
    print(blockchain.get_length())
    # Print the last block
    print(blockchain.get_last_block())
    # Print the last proof
    print(blockchain.get_last_proof())
    # Print the last hash
    print(blockchain.get_last_hash())
    # Print the current transactions
    print(
        blockchain.get_current_transactions()
    )
    # Print the nodes
    print(blockchain.get_nodes())
    # Print the length of the nodes
    print(len(blockchain.get_nodes()))

    # Create a new transaction
    blockchain.new_transaction(
        sender="0",
        recipient="1",
        amount=1,
    )
    
    # Print the last block
    print(blockchain.get_last_block())
    # Print the current transactions
    print(blockchain.get_current_transactions())

    # Create a new block
    blockchain.new_block()
    # Print the last block
    print(blockchain.get_last_block())
    # Print the current transactions
    print(blockchain.get_current_transactions())



app = Flask(__name__)

    node_identifier = str(uuid4()).replace('-', '')
    # Create a blockchain
    blockchain = Blockchain.create_blockchain()

    @app.route('/blockchain', methods=['GET'])
    def get_blockchain():
        response = {
            'length': blockchain.get_length(),
            'chain': blockchain.get_chain(),
            'last_block': blockchain.get_last_block(),
        }   
        return jsonify(response), 200

    @app.route('/mine', methods=['GET'])
    def mine():
        # Run the proof of work algorithm to get the last proof
        last_proof = blockchain.get_last_proof()
        # Run the proof of work algorithm to get the proof
        proof = blockchain.proof_of_work(last_proof)
        # Get the last hash
        last_hash = blockchain.get_last_hash()
        # Create a new transaction
        blockchain.new_transaction(
            sender="0",
            recipient=node_identifier,
            amount=1,
        )

    @app.route('/transactions/new', methods=['POST'])
    def new_transaction():
        values = request.get_json()
        # Check that the required fields are in the POST'ed data
        required = ['sender', 'recipient', 'amount']
        if not all(k in values for k in required):
            return 'Missing values', 400
        # Create a new transaction
        index = blockchain.new_transaction(
            values['sender'],
            values['recipient'],
            values['amount'],
        )
        response = {'message': f'Transaction will be added to Block {index}'}
        return jsonify(response), 201

    @app.route('/chain', methods=['GET'])
    def full_chain():
        response = {
            'chain': blockchain.get_chain(),
            'length': len(blockchain.get_chain()),
        }
        return jsonify(response), 200

    @app.route('/nodes/register', methods=['POST'])
    def register_nodes():
        values = request.get_json()
        nodes = values.get('nodes')
        if nodes is None:
            return "Error: Please supply a valid list of nodes", 400
        for node in nodes:
            blockchain.add_node(node)
        response = {
            'message': 'New nodes have been added',
            'total_nodes': list(blockchain.get_nodes()),
        }
        return jsonify(response), 201
    
    @app.route('/nodes/resolve', methods=['GET'])
    def consensus():
        replaced = blockchain.resolve_conflicts()
        if replaced:
            response = {
                'message': 'Our chain was replaced',
                'new_chain': blockchain.get_chain(),
            }
        else:
            response = {
                'message': 'Our chain is authoritative',
                'chain': blockchain.get_chain(),
            }
        return jsonify(response), 200
    
    @app.route('/nodes/get', methods=['GET'])
    def get_nodes():
        nodes = list(blockchain.get_nodes())
        response = {
            'message': 'List of nodes',
            'total_nodes': nodes,
        }
        return jsonify(response), 200

    @app.route('/nodes/get/<node_identifier>', methods=['GET'])
    def get_node(node_identifier):
        node = blockchain.get_node(node_identifier)
        if node is None:
            return "Error: Node not found", 400
        response = {
            'message': 'Node found',
            'node': node,
        }
        return jsonify(response), 200
    
    @app.route('/nodes/get/<node_identifier>/transactions', methods=['GET'])
    def get_node_transactions(node_identifier):
        transactions = blockchain.get_node_transactions(node_identifier)
        if transactions is None:
            return "Error: Node not found", 400
        response = {
            'message': 'Node found
            'transactions': transactions,
        }
        return jsonify(response), 200
    
    @app.route('/nodes/get/<node_identifier>/blocks', methods=['GET'])
    def get_node_blocks(node_identifier):
        blocks = blockchain.get_node_blocks(node_identifier)
        if blocks is None:
            return "Error: Node not found", 400
        response = {
            'message': 'Node found
            'blocks': blocks,
        }
        return jsonify(response), 200
    
    @app.route('/nodes/get/<node_identifier>/length', methods=['GET'])
    def get_node_length(node_identifier):
        length = blockchain.get_node_length(node_identifier)
        if length is None:
            return "Error: Node not found", 400
        response = {
            'message': 'Node found
            'length': length,
        }
        return jsonify(response), 200
    
    @app.route('/nodes/get/<node_identifier>/last_block', methods=['GET'])
    def get_node_last_block(node_identifier):
        last_block = blockchain.get_node_last_block(node_identifier)
        if last_block is None:
            return "Error: Node not found", 400
        response = {
            'message': 'Node found
            'last_block': last_block,
        }
        return jsonify(response), 200

    @app.route('/nodes/get/<node_identifier>/last_hash', methods=['GET'])
    def get_node_last_hash(node_identifier):
        last_hash = blockchain.get_node_last_hash(node_identifier)
        if last_hash is None:
            return "Error: Node not found", 400
        response = {
            'message': 'Node found
            'last_hash': last_hash,
        }
        return jsonify(response), 200

    @app.route('/nodes/get/<node_identifier>/last_proof', methods=['GET'])
    def get_node_last_proof(node_identifier):
        last_proof = blockchain.get_node_last_proof(node_identifier)
        if last_proof is None:
            return "Error: Node not found", 400
        response = {
            'message': 'Node found
            'last_proof': last_proof,
        }
        return jsonify(response), 200

    @app.route('/nodes/get/<node_identifier>/last_time', methods=['GET'])
    def get_node_last_time(node_identifier):
        last_time = blockchain.get_node_last_time(node_identifier)
        if last_time is None:
            return "Error: Node not found", 400
        response = {
            'message': 'Node found
            'last_time': last_time,
        }
        return jsonify(response), 200
    
    @app.route('/nodes/get/<node_identifier>/last_hash_time', methods=['GET'])
    def get_node_last_hash_time(node_identifier):
        last_hash_time = blockchain.get_node_last_hash_time(node_identifier)
        if last_hash_time is None:
            return "Error: Node not found", 400
        response = {
            'message': 'Node found
            'last_hash_time': last_hash_time,
        }
        return jsonify(response), 200

    @app.route('/nodes/get/<node_identifier>/last_hash_proof', methods=['GET'])
    def get_node_last_hash_proof(node_identifier):
        last_hash_proof = blockchain.get_node_last_hash_proof(node_identifier)
        if last_hash_proof is None:
            return "Error: Node not found", 400
        response = {
            'message': 'Node found
            'last_hash_proof': last_hash_proof,
        }
        return jsonify(response), 200
    
    @app.route('/nodes/get/<node_identifier>/last_hash_time_proof', methods=['GET'])
    def get_node_last_hash_time_proof(node_identifier):
        last_hash_time_proof = blockchain.get_node_last_hash_time_proof(node_identifier)
        if last_hash_time_proof is None:
            return "Error: Node not found", 400
        response = {
            'message': 'Node found
            'last_hash_time_proof': last_hash_time_proof,
        }
        return jsonify(response), 200

    @app.route('/nodes/sync', methods=['GET'])
    def sync_nodes():
        
        blockchain.sync_nodes()
        response = {
            'message': 'Nodes synced',
        }
        return jsonify(response), 200