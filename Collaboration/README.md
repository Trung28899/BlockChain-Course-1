## CHAIN VALIDATION & REPLACEMENT: TABLE OF CONTENT:

1. 15th Commit: Validating Blocks
2. 16th Commit: Validating Chain
3. 17th Commit: Chain Replacement

---

## FUNDAMENTALS:

- See Handbook to understand the concept of Chain Validation & Replacement

- In this section, we're preparing the Block and Blockchain classes to be
  able for collaboration

---

## COMMANDS:

`$ cd Collaboration`
`$ python3 -m backend.blockchain.block`
`$ python3 -m pytest backend/tests`
`$ python3 -m backend.scripts.average_block_rate`

---

## COMMIT HISTORY:

1. 15th Commit: Validating Blocks

   - Method to validate a block based on the previous block

   - See code:
     +, ./backend/blockchain/block.py > method: is_valid_block()
     +, ./backend/tests/blockchain/block.py

   - See how to raise exceptions and catch it with try and except

2. 16th Commit: Validating Chain

   - Method to validate the whole chain

   - See code:
     +, ./backend/blockchain/blockchain.py > method: is_valid_chain()
     +, ./backend/tests/blockchain/blockchain.py

3. 17th Commit: Chain Replacement

   - Method to validate replace the whole chain of the blockchain

   - See code:
     +, ./backend/blockchain/replace_chain.py > method: is_valid_chain()
     +, ./backend/tests/blockchain/blockchain.py
