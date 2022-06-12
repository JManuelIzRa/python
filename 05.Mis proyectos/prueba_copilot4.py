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

  # Function to create a block
def create_block(transactions, proof, previous_hash):
    # Create a block
    block = {
        'index': len(blockchain) + 1,
        'timestamp': time(),
        'transactions': transactions,
        'proof': proof,
        'previous_hash': previous_hash
    }
    # Return the block
    return block
    # End of function

    # Function to get the previous hash
def get_previous_hash(blockchain):
    # Get the last block
    last_block = blockchain[-1]
    # Return the previous hash
    return last_block['hash']
    # End of function

    # Function to get the proof of work
def proof_of_work(previous_hash):
    # Create a variable to store the proof
    proof = 0
    # Loop until the proof is found
    while not valid_proof(previous_hash, proof):
        # Increment the proof
        proof += 1
    # Return the proof
    return proof
    # End of function

    # Function to validate the proof
def valid_proof(previous_hash, proof):
    # Create a string to store the hash
    guess = previous_hash + str(proof)
    # Create a hash
    guess_hash = hashlib.sha256(guess.encode()).hexdigest()
    # Return the result
    return guess_hash[:4] == '0000'
    # End of function

    # Function to create the genesis block
def create_genesis_block():
    # Create the genesis block
    return create_block([], 0, '0')
    # End of function

    # Function to create the blockchain
def create_blockchain():
    # Create the blockchain
    blockchain = [create_genesis_block()]
    # Return the blockchain
    return blockchain
    # End of function

    # Function to get the last block
def get_last_block(blockchain):
    # Get the last block
    last_block = blockchain[-1]
    # Return the last block
    return last_block
    # End of function

    # Function to get the hash of the block
def get_hash(block):
    # Create a string to store the block
    block_string = json.dumps(block, sort_keys=True).encode()
    # Create a hash
    block_hash = hashlib.sha256(block_string).hexdigest()
    # Return the hash
    return block_hash
    # End of function

    # Function to get the proof of work
def get_proof_of_work(blockchain):
    # Get the last block
    last_block = get_last_block(blockchain)
    # Get the previous hash
    previous_hash = get_hash(last_block)
    # Get the proof of work
    proof = proof_of_work(previous_hash)
    # Return the proof of work
    return proof
    # End of function

    # Function to get the transactions

    # Function to get the transactions
def get_transactions(blockchain):
    # Get the last block
    last_block = get_last_block(blockchain)
    # Get the transactions
    transactions = last_block['transactions']
    # Return the transactions
    return transactions
    # End of function

# Main program  
if __name__ == '__main__':
    # Create the blockchain
    blockchain = create_blockchain()
    # Get the proof of work
    proof = get_proof_of_work(blockchain)
    # Create a transaction
    transactions = get_transactions(blockchain)
    # Create a block
    block = create_block(transactions, proof, get_previous_hash(blockchain))
    # Print the block
    print(block)
    # Exit the program
    exit()
    # End of program


    