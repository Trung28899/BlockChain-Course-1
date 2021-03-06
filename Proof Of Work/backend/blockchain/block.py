import time
from backend.utils.crypto_hash import crypto_hash
from backend.utils.hex_to_binary import hex_to_binary
from backend.config import MINE_RATE

# This is how we define a global variable
GENESIS_DATA = {
    "timestamp": 1, 
    "last_hash": "genesis_last_hash", 
    "hash": "genesis_hash", 
    "data": [], 
    "difficulty": 3, 
    'nonce': "genesis_nonce"
}

class Block: 
    """
    Block: a unit of storage
    Store transactions in a blockchain that supports a cryptocurrency
    """
    def __init__(self, timestamp, last_hash, hash, data, difficulty, nonce):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data
        self.difficulty = difficulty
        self.nonce = nonce
    
    def __repr__(self): 
        return (
            'Block('
            f"\nBlockchain - timestamp: {self.timestamp}"
            f"\nBlockchain - last_hash: {self.last_hash}"
            f"\nBlockchain - hash: {self.hash}"
            f"\nBlockchain - data: {self.data}"
            f"\nBlockchain - difficulty: {self.difficulty}"
            f"\nBlockchain - nonce: {self.nonce} )"
        )
    
    @staticmethod
    def mine_block(last_block, data): 
        """
            Mine a block based on the given last_block and data, until a block hash is found that 
            meets the leading 0's proof of work requirement
            Mine a block meaning: create a new and valid block instant
        """
        timestamp = time.time_ns()
        last_hash = last_block.hash
        difficulty = Block.adjust_difficulty(last_block, timestamp)
        nonce = 0
        hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)

        """
            Syntax Explanation: 

            hash[0:difficulty] is the substring of the hash value. 
            For example, if difficulty is 3, the substring will be taken from 
            index 0 to index 3 

            '0' * difficulty is, for example, if difficulty = 3
            '0' * difficulty will be '000'

            so this loop won't stop until there are 3 zeros
            at the begining of the string
        """
        while hex_to_binary(hash)[0:difficulty] != '0' * difficulty: 
            nonce += 1
            timestamp = time.time_ns()
            difficulty = Block.adjust_difficulty(last_block, timestamp)
            hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)

        return Block(timestamp, last_hash, hash, data, difficulty, nonce)

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
    
    @staticmethod
    def adjust_difficulty(last_block, new_timestamp): 
        """
            Calculate the adjusted difficulty according to the MINE_RATE
            Increase the difficulty for quicky mined blocks
            Decrease the difficulty for slowly mined blocks
        """
        if(new_timestamp - last_block.timestamp) < MINE_RATE:
            return last_block.difficulty + 1

        if(last_block.difficulty - 1) > 0:
            return last_block.difficulty - 1
        
        return 1

def main(): 
    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block, "foo")
    print(block)

if __name__ == "__main__": 
    main()