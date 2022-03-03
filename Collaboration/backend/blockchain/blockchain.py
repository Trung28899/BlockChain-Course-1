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

def main(): 
    blockchain = Blockchain()
    blockchain.add_block("one")
    blockchain.add_block("two")

    print(blockchain)

    print(f'blockchain.py __name__: {__name__}')

if __name__ == "__main__": 
    main()