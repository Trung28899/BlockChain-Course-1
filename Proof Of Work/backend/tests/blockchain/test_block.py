from backend.blockchain.block import Block, GENESIS_DATA

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
    assert block.hash[0:block.difficulty] == '0' * block.difficulty

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