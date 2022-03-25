## BLOCKCHAIN API: TABLE OF CONTENT:

1. 18th Commit: Setup the Flask API (Video 50)

---

## FUNDAMENTALS:

- Building blockchain API with routes to receive
  (much like routes in Express.js)

- Python is also a non-blocking language. Meaning when there is an asychronous
  task running, the code will continue to be execute synchronously to the next line and
  doesn't block the execution to wait for the async task to be completed

- PubNub:
  https://www.pubnub.com/
  > account: google email (trung28899@gmail.com)

---

## COMMANDS:

`$ source blockchain-env/bin/activate`

> go to testing environment

`$ cd "Blockchain API"`

`$ pip3 freeze`

> see all the dependencies

`$ pip3 install flask`

`$ python3 -m backend.app`

`$ python3 -m backend.pubsub`

---

## COMMIT HISTORY:

1. 18th Commit: Setup the Flask API (Video 50)

   - Set up RESTful API for our app (much like routes in Express.js)

   - See code:
     +, ./backend/app/init.py

   - Command:

`$ python3 -m backend.app`

---

2.  19th Commit: Setup the get blockchain route and the mine block route
    (Video 51 - 53)

    - Set up the route to get the blockchain and the route to mine block

    - NOTES:
      +, Type: `$ python3 -m backend.app` in the terminal, then
      +, go to localhost:5000/blockchain to get the blockchain.chain
      +, Go to localhost:5000/blockchain/mine to mine a new block then go back to
      the /blockchain route to see the result

      +, Right now the blockchain system is not able for multiple nodes to collaborate
      +, Next commit will implement that

    - NOTES for code:
      +, Needed to convert data to JSON format for the HTTP request so have to format the data
      correctly:

      > See file: block.py and blockchain.py, method: to_json()

      > See file /server/app/init.py: jsonify()

---

3. 20th Commit: Setup PubNub (Video 55 - 56):

   - See how pubnub is setup in /backend/pubsub.py

   - 20th Commit Part 2 is a more organized code in the same file.
     Code is organized into a PubSub class

   - COMMANDS:
     `$ pip3 install pubnub`
     `$ python3 -m backend.pubsub`
     `$ python3 -m backend.app`

---

4. 21st Commit: Setup Peer Instances (video 57):

   - Setting up peer instances so that we have multiple nodes in the network

   - See code in:
     +, backend/app/init.py > see how the port is setup
     +, backend/pubsub.py

   - Open 3 different terminals:

     +, 1st terminal, run: `$ python3 -m backend.app`

     +, 2nd terminal, run: `$ export PEER=True && python3 -m backend.app`

     > This is how to run a peer instance

     +, 3rd terminl, run: `$ python3 -m backend.pubsub`

     => Then see how to print is broadcast in the 3 different terminals

   - OTHER COMMAND: `$ cd "Blockchain API"`

---

5. 22nd Commit: Broadcast to all peers when a new block is added (Video 58)

   - See how a peer broadcast a message to add a new block to all peers in network

   - See Code:
     +, backend/pubsub.py > look for broadcast_block()
     +, backend/app/init.py > see route_blockchain_mine()

   - In order to see how it works, open 3 different temrinals, cd to the correct folder. STEPS TO TEST OUTPUT:
     +, 1st terminal, run: `$ python3 -m backend.app`

     +, 2nd terminal, run a peer instance: `$ export PEER=True && python3 -m backend.app`

     +, 3rd terminal, run a peer instance: `$ export PEER=True && python3 -m backend.app`

     +, Go to browser, go to http://127.0.0.1:5000/blockchain/mine

     => This will mine a new block and broadcast it for the peer of the 1st terminal
     => See the output for all terminals to see how a new block is broadcast

   - OTHER COMMAND: `$ cd "Blockchain API"`

---

6. 23rd Commit: Add a block locally after receiving a broadcast message (Vid 59)

   - After a peer received a broadcasted messsage to add a block, it will
     need to add the block locally. We will implement the code in this commit

   - See Code:

     +, backend/pubsub.py > look for class Listener and message()
     to see how message to add block is being handled

     +, backend/app/init.py

     > see route_blockchain_mine()

     > see pubsub = PubSub(blockchain)

     +, backend/blockchain/block.py: see method from_json()

   - Perform the exact steps for the 22nd Commit (STEPS TO TEST OUTPUT):

     +, Will see the peers will have the block successfully added

     +, The primary node will have an error of did not replace chain

   => This is because the primary node already have the updated chain locally
   => It published to add a new block but it also subscribe to this channel
   => Will try to add new block like other peers but the block was already there, so it will be rejected

   - A new problem:

     +, After adding the 1st block, a new peer join the network won't
     have the updated version. It will only have the chain with the
     genesis block (see backend/app/init.py)

     +, Therefore, when we add another block, the new peer won't
     be able to add that block. To see this issue:

     > open a 4th terminal, run the same command: `$ export PEER=True && python3 -m backend.app`

     > hit the route to mine a new block: http://127.0.0.1:5000/blockchain/mine

     > the other 2 peers will be able to add this new block. The 4th peer won't be able to

   => We will need to synchronize when a new peer join the network
   => Will do it in next commit
