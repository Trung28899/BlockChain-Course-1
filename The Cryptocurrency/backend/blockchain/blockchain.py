from backend.blockchain.block import Block

class Blockchain: 
    """
    Blockchain: a public ledger of transactions. 
    Implemented as a list of block - data set of transactions
    """

    def __init__(self):
        self.chain = [Block.genesis()]
    
    def add_block(self, data): 
        # this is how to get the last item in a list (array) in python
        last_block = self.chain[-1]
        self.chain.append(Block.mine_block(last_block, data))
    
    def __repr__(self): 
        return f"Blockchain: {self.chain}"

    """
        Validate the incoming chain
        Enforce the following rules of the blockchain
            - The chain must start with the genesis block
            - blocks must be formatted correctly
        
        => the idea is to validate every single the blocks
    """
    @staticmethod
    def is_valid_chain(chain): 
        """
            This if statement works because of the __eq__
            method in block.py

            it shouldn't work because these 2 are different
            instances of a Block so the != or == won't work
        """
        if chain[0] != Block.genesis(): 
            raise Exception('The genesis block must be valid')

        for i in range(1, len(chain)):
            block = chain[i]
            last_block = chain[i - 1]
            Block.is_valid_block(last_block, block)
    
    def to_json(self):
        # serialized_chain = []

        # for block in self.chain:
        #     serialized_chain.append(block.to_json())

        # return serialized_chain
        """
            Serialized the blockchain into a list
            of blocks

            lambda function like the arrow function in JS: 
            (data) => {}

            syntax down below in JS would be: 
            self.chain.map(block => block.to_json())
        """

        return list(map(lambda block: block.to_json(), self.chain))
    
    @staticmethod
    def from_json(chain_json):
        """
            Convert an object into a Blockchain instance (Blockchain Object)
            The result will contain a chain list of Block instances
        """
        blockchain = Blockchain()

        """
            Equivalent of 
            blockchain.chain = chain_json.map(block_json => Block.from_json(block_json))
            in JavaScript
        """
        blockchain.chain = list(map(lambda block_json: Block.from_json(block_json), chain_json))
        return blockchain

    
    def replace_chain(self, chain): 
        """
            Replace the local chain with the incoming one if the following applies: 
                - The incoming chain must be longer than the local one
                - The incoming chain is formatted properly
        """
        if len(chain) <= len(self.chain): 
            raise Exception("Cannot replace. The incoming chain must be longer")

        try: 
            Blockchain.is_valid_chain(chain)
        except Exception as e:
            raise Exception(f'Cannot replace. The incoming is invalid: {e}')
        
        self.chain = chain




def main(): 
    blockchain = Blockchain()
    blockchain.add_block("one")
    blockchain.add_block("two")

    print(blockchain)

    print(f'blockchain.py __name__: {__name__}')

if __name__ == "__main__": 
    main()