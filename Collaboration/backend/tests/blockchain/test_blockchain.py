from backend.blockchain.blockchain import Blockchain
from backend.blockchain.block import GENESIS_DATA
import pytest

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

"""
@pytest.fixture helps declare variable that we can re-use
in test method

this is so that we don't have to create a blockchain
variables again and again for the blockchain validation 
(test_is_valid_chain) tests down below
remember to import pytest at the top of the file
"""
@pytest.fixture
def blockchain_three_blocks():
    blockchain = Blockchain()

    for i in range(3):
        blockchain.add_block(i)
    return blockchain

"""
    Test to see if a blockchain is valid
    if there is no exceptions raised from the is_valid_chain
    method > the test will pass

    otherwise, there will be an error
"""
def test_is_valid_chain(blockchain_three_blocks):
    Blockchain.is_valid_chain(blockchain_three_blocks.chain)

def test_is_valid_chain_bad_genesis(blockchain_three_blocks):
    blockchain_three_blocks.chain[0].hash = "evil_hash"

    with pytest.raises(Exception, match="genesis block must be valid"):
        Blockchain.is_valid_chain(blockchain_three_blocks.chain)