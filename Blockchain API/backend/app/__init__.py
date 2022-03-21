from this import d
from flask import Flask, jsonify
from backend.blockchain.blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

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

    return jsonify(blockchain.chain[-1].to_json())

app.run(port=5001)