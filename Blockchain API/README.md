## BLOCKCHAIN API: TABLE OF CONTENT:

1. 18th Commit: Setup the Flask API (Video 50)

---

## FUNDAMENTALS:

- Building blockchain API with routes to receive
  (much like routes in Express.js)

---

## COMMANDS:

`$ cd Collaboration`
`$ python3 -m backend.blockchain.block`
`$ python3 -m pytest backend/tests`
`$ python3 -m backend.scripts.average_block_rate`

`$ cd "Blockchain API"`

`$ pip3 freeze`

> see all the dependencies

`$ pip3 install flask`

`$ python3 -m backend.app`

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

    - NOTES for code:
      +, Needed to convert data to JSON format for the HTTP request so have to format the data
      correctly:

      > See file: block.py and blockchain.py, method: to_json()

      > See file /server/app/init.py: jsonify()
