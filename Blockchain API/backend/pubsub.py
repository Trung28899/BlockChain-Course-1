import time
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-660a6c3e-a9f2-11ec-a8cf-c6bc4dd2ac2a'
pnconfig.publish_key = 'pub-c-815d2a7a-942b-4a1a-a804-bfe1862f6b01'
# For pubnub==6.1.0 and above, will need to set up pnconfig.uuid

TEST_CHANNEL = "TEST_CHANNEL"

class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f'\n-- Channel: {message_object.channel}')
        print(f'\n-- Message: {message_object.message}')

class PubSub():
    """
        Handles the publish/subscribe layer of the application
        Provides communication between the nodes of the blockchain network
    """
    def __init__(self):
        self.pubnub = PubNub(pnconfig)
        # Subscribing to a channel
        self.pubnub.subscribe().channels([TEST_CHANNEL]).execute()
        self.pubnub.add_listener(Listener())
    
    """
        Publish the message object to the channel
    """
    def publish(self, channel, message): 
        self.pubnub.publish().channel(channel).message(message).sync()



def main():
    pubsub = PubSub()
    time.sleep(1)

    pubsub.publish(TEST_CHANNEL, {'foo': 'bar'})

if __name__ == "__main__": 
    main()