import pytest
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

"""
@pytest.fixture helps declare variable that we can re-use
in test method

this is so that we don't have to create the last_block
and block variables again and again for the block validation 
(test_is_valid_block) tests down below
remember to import pytest at the top of the file
"""
@pytest.fixture
def last_block():
    return Block.genesis()

# last_block is declared with @pytest.fixture above
@pytest.fixture
def block(last_block):
    return Block.mine_block(last_block, "test_data")

"""
    Test to see if a block is valid
    if there is no exceptions raised from the is_valid_block
    method > the test will pass

    otherwise, there will be an error
"""
def test_is_valid_block(last_block, block):
    Block.is_valid_block(last_block, block)

def test_is_valid_block_bad_last_hash(last_block, block):
    block.last_hash = "evil_last_hash"

    # this is how pytest expect for an exception to happen so that it will be passed
    with pytest.raises(Exception, match="last_hash must be correct"):
        Block.is_valid_block(last_block, block)

def test_is_valid_block_bad_proof_of_work(last_block, block):
    block.hash = "fff"

    # this is how pytest expect for an exception to happen so that it will be passed
    with pytest.raises(Exception, match="The proof of work requirement was not met"):
        Block.is_valid_block(last_block, block)

def test_is_valid_block_bad_proof_of_work(last_block, block):
    block.hash = "fff"

    # this is how pytest expect for an exception to happen so that it will be passed
    with pytest.raises(Exception, match="The proof of work requirement was not met"):
        Block.is_valid_block(last_block, block)

def test_is_valid_block_jumped_difficulty(last_block, block):
    jumped_difficulty = 10
    block.difficulty = jumped_difficulty
    block.hash = f'{"0" * jumped_difficulty}111abc'

    # this is how pytest expect for an exception to happen so that it will be passed
    with pytest.raises(Exception, match="The block difficulty must only adjust by 1"):
        Block.is_valid_block(last_block, block)

def test_is_valid_block_bad_block_hash(last_block, block):
    block.hash = "000000000000000bbbac"

    # this is how pytest expect for an exception to happen so that it will be passed
    with pytest.raises(Exception, match="The block hash must be correct !"):
        Block.is_valid_block(last_block, block)