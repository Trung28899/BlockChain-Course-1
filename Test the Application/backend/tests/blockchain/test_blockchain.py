from backend.blockchain.blockchain import Blockchain
from backend.blockchain.block import GENESIS_DATA

def test_blockchain_instances():
    blockchain = Blockchain()

    # Test to see if the genesis block is valid
    assert blockchain.chain[0].hash == GENESIS_DATA['hash']

def test_add_block():
    blockchain = Blockchain()
    data = 'test-data'
    blockchain.add_block(data)

    # Added a block and check to see if the last block is added correctly
    assert blockchain.chain[-1].data == data