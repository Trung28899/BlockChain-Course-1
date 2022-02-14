import time

def mine_block(last_block, data): 
    """
        Mine a block based on the given last_block and data
        Mine a block meaning: create a new and valid block instant
    """
    timestamp = time.time_ns()
    last_hash = last_block.hash
    hash = f'{timestamp}-{last_hash}'

    return Block(timestamp, last_hash, hash, data)

def genesis(): 
    """
        Generate the genesis block
        Genesis block: the first block in a chain
    """

    return Block(1, 'genesis_last_hash', 'genesis_hash', [])

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

def main(): 
    genesis_block = genesis()
    block = mine_block(genesis_block, "foo")
    print(block)

if __name__ == "__main__": 
    main()