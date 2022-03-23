import time
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-660a6c3e-a9f2-11ec-a8cf-c6bc4dd2ac2a'
pnconfig.publish_key = 'pub-c-815d2a7a-942b-4a1a-a804-bfe1862f6b01'
# For pubnub==6.1.0 and above, will need to set up pnconfig.uuid

pubnub = PubNub(pnconfig)

TEST_CHANNEL = "TEST_CHANNEL"

# Subscribing to a channel
pubnub.subscribe().channels([TEST_CHANNEL]).execute()

class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f'\n-- Incoming message_object: {message_object}')


pubnub.add_listener(Listener())

def main():
    time.sleep(1)
    # Publishing to a channel
    pubnub.publish().channel(TEST_CHANNEL).message({"foo": "bar"}).sync()
    # print("Hi")

if __name__ == "__main__": 
    main()