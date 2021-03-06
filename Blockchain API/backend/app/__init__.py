import os
import random
import requests

from flask import Flask, jsonify
from backend.blockchain.blockchain import Blockchain
from backend.pubsub import PubSub

app = Flask(__name__)
blockchain = Blockchain()
pubsub = PubSub(blockchain)

@app.route("/")
def default():
    return "WELCOME TO THE BLOCKCHAIN"

"""
    Route to get the blockchain's chain

    blockchain.__repr__() returning 
    blockchain.chain in string format

    jsonify can only takes certain data types in python
    such as: numbers, boolean, string, dictionaries (Object)
    and List (array)

    to_json() is the method defined within the class Blockchain
"""
@app.route("/blockchain")
def route_blockchain():
    return jsonify(blockchain.to_json())

@app.route("/blockchain/mine")
def route_blockchain_mine():
    transaction_data = "stubbed_trans_data"

    blockchain.add_block(transaction_data)

    block = blockchain.chain[-1]
    pubsub.broadcast_block(block)

    return jsonify(block.to_json())

ROOT_PORT = 5000
PORT = ROOT_PORT

# This is how to get environment variables
if os.environ.get('PEER') == "True":
    # getting a random port value from 5001 to 6000
    PORT = random.randint(5001, 6000)

    # getting the updated chain when a peer started up
    result = requests.get(f'http://127.0.0.1:{ROOT_PORT}/blockchain')
    result_blockchain = Blockchain.from_json(result.json())

    try:
        blockchain.replace_chain(result_blockchain.chain)
        print('\n -- Successfully synchronized the local chain')
    except Exception as e:
        print(f'\n -- Error Synchronizing: {e}')


app.run(port=PORT)