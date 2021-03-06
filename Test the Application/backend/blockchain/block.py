import time
from backend.utils.crypto_hash import crypto_hash

# This is how we define a global variable
GENESIS_DATA = {
    "timestamp": 1, 
    "last_hash": "genesis_last_hash", 
    "hash": "genesis_hash", 
    "data": []
}

class Block: 
    """
    Block: a unit of storage
    Store transactions in a blockchain that supports a cryptocurrency
    """
    def __init__(self, timestamp, last_hash, hash, data):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data
    
    def __repr__(self): 
        return (
            'Block('
            f"\nBlockchain - timestamp: {self.timestamp}"
            f"\nBlockchain - last_hash: {self.last_hash}"
            f"\nBlockchain - hash: {self.hash}"
            f"\nBlockchain - data: {self.data} )"
        )
    
    @staticmethod
    def mine_block(last_block, data): 
        """
            Mine a block based on the given last_block and data
            Mine a block meaning: create a new and valid block instant
        """
        timestamp = time.time_ns()
        last_hash = last_block.hash
        hash = crypto_hash(timestamp, last_hash, data)

        return Block(timestamp, last_hash, hash, data)

    @staticmethod
    def genesis(): 
        """
            Generate the genesis block
            Genesis block: the first block in a chain
        """

        # return Block(
        #     timestamp = GENESIS_DATA['timestamp'], 
        #     genesis_last_hash = GENESIS_DATA['genesis_last_hash'], 
        #     genesis_hash = GENESIS_DATA['genesis_hash'], 
        #     data = GENESIS_DATA['data']
        # )
        
        return Block(**GENESIS_DATA)

def main(): 
    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block, "foo")
    print(block)

if __name__ == "__main__": 
    main()