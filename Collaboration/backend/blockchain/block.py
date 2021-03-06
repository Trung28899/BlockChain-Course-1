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

    """
        run this command to understand __dict__

        $ python3
        >> foo = Block.genesis()
        >> print(foo.__dict__)
    """
    def __eq__(self, other): 
        return self.__dict__ == other.__dict__
    
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
    
    @staticmethod
    def is_valid_block(last_block, block): 
        """
            Validate a block by enforcing the following rules: 
                - The block must have the proper last_hash reference
                - The block must meet the proof of work requirement
                - The difficulty must only adjust by 1
                - The block hash must be a valid combination of the block fields
        """
        if block.last_hash != last_block.hash:
            raise Exception("The block last_hash must be correct")

        if hex_to_binary(block.hash)[0:block.difficulty] != '0' * block.difficulty: 
            raise Exception("The proof of work requirement was not met")
        
        if abs(last_block.difficulty - block.difficulty) > 1:
            raise Exception("The block difficulty must only adjust by 1")
        
        reconstructed_hash = crypto_hash(block.timestamp, block.last_hash, block.data, block.difficulty, block.nonce)

        if block.hash != reconstructed_hash: 
            raise Exception("The block hash must be correct !")

def main(): 
    genesis_block = Block.genesis()
    bad_block = Block.mine_block(genesis_block, "foo")
    bad_block.last_hash = 'evil_data'

    try: 
        Block.is_valid_block(genesis_block, bad_block)
    except Exception as e: 
        print(f'is_valid_block: {e}')

if __name__ == "__main__": 
    main()