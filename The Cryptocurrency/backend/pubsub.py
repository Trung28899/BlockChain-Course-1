from tarfile import BLOCKSIZE
import time
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback
from backend.blockchain.block import Block


pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-660a6c3e-a9f2-11ec-a8cf-c6bc4dd2ac2a'
pnconfig.publish_key = 'pub-c-815d2a7a-942b-4a1a-a804-bfe1862f6b01'
# For pubnub==6.1.0 and above, will need to set up pnconfig.uuid

CHANNELS = {
    "TEST": "TEST", 
    "BLOCK": 'BLOCK'
}

class Listener(SubscribeCallback):
    def __init__(self, blockchain):
        self.blockchain = blockchain


    def message(self, pubnub, message_object):
        print(f'\n-- Channel: {message_object.channel}')
        print(f'\n-- Message: {message_object.message}')

        if message_object.channel == CHANNELS['BLOCK']: 
            # converting json to a block presentation
            # see backend/blockchain/block.py
            block = Block.from_json(message_object.message)
            
            # this is how to get a complete array without referencing
            # its address. This is like the slice() function in JavaScript
            potential_chain = self.blockchain.chain[0:len(self.blockchain.chain)]
            potential_chain.append(block)

            try: 
                # this will validate the entire chain before replacing it
                # See /blockchain/blockchain.py
                self.blockchain.replace_chain(potential_chain)
                print(f'\n -- Successfully replaced the local chain')
            except Exception as e: 
                print(f'\n -- Did not replace chain: {e}')

class PubSub():
    """
        Handles the publish/subscribe layer of the application
        Provides communication between the nodes of the blockchain network
    """
    def __init__(self, blockchain):
        self.pubnub = PubNub(pnconfig)
        # Subscribing to a channel
        self.pubnub.subscribe().channels(CHANNELS.values()).execute()
        self.pubnub.add_listener(Listener(blockchain))
    
    """
        Publish the message object to the channel
    """
    def publish(self, channel, message): 
        self.pubnub.publish().channel(channel).message(message).sync()
    
    """
        Broadcast a block object to all nodes
    """
    def broadcast_block(self, block):
        # .to_json() is a method in the class Block, 
        # see file /backend/blockchain/block.py to see it
        self.publish(CHANNELS['BLOCK'], block.to_json())

def main():
    pubsub = PubSub()
    time.sleep(1)

    pubsub.publish(CHANNELS['TEST'], {'foo': 'bar'})

if __name__ == "__main__": 
    main()