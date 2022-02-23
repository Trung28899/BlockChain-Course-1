from backend.blockchain.block import Block, GENESIS_DATA
from backend.config import MINE_RATE, SECONDS
import time
from backend.utils.hex_to_binary import hex_to_binary


def test_mine_block(): 
    last_bock = Block.genesis()
    data = "test-data"
    block = Block.mine_block(last_bock, data)

    # Checking if block is a instance of Block class
    assert isinstance(block, Block)
    # Checking to see if the block data is the same as data
    assert block.data == data
    # Checking to see if the last_hash of the new block matched the
    # hash of the previous block
    assert block.last_hash == last_bock.hash
    # Test to see if the hash is valid Proof Of Work
    assert hex_to_binary(block.hash)[0:block.difficulty] == '0' * block.difficulty

def test_genesis(): 
    genesis = Block.genesis()

    # Checking if genesis is a instance of Block class
    assert isinstance(genesis, Block)

    # assert genesis.timestamp == GENESIS_DATA['timestamp']
    # assert genesis.last_hash == GENESIS_DATA['last_hash']
    # assert genesis.hash == GENESIS_DATA['hash']
    # assert genesis.data == GENESIS_DATA['data']

    for key, value in GENESIS_DATA.items():
        # get attribute, same thing as above
        getattr(genesis, key) == value

"""
    Test to make sure that the difficulty for 
    Proof Of Work increased based on MINE_RATE

    The last_block and mined_block are mined very 
    closely, mined_block is basically the last line
    of code. 

    Therefore, the difficulty should be raised by 1
    > Expect difficulty to increase
"""
def test_quickly_mined_block(): 
    last_block = Block.mine_block(Block.genesis(), "foo")
    mined_block = Block.mine_block(last_block, "bar")

    assert mined_block.difficulty == last_block.difficulty + 1

"""
    Test to make sure that the difficulty for 
    Proof Of Work decreased based on MINE_RATE

    Expect difficulty to decrease

    time.sleep() take values in seconds
"""
def test_slowly_mined_block(): 

    last_block = Block.mine_block(Block.genesis(), "foo")

    time.sleep(MINE_RATE / SECONDS)

    mined_block = Block.mine_block(last_block, "bar")

    assert mined_block.difficulty == last_block.difficulty - 1

"""
    Test to make sure that the difficulty for 
    Proof Of Work doesn't go to 0 no matter what
"""
def test_mined_block_difficulty_limits_at_1():
    last_block = Block(
        time.time_ns(), 
        'test_last_hash', 
        'test_hash', 
        'test_data',
        1, 
        0
    )

    time.sleep(MINE_RATE / SECONDS)

    mined_block = Block.mine_block(last_block, "bar")

    assert mined_block.difficulty == 1

