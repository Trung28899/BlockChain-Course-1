## START THE BLOCKCHAIN APPLICATION: TABLE OF CONTENT:

1, 4th Commit: Defining Block and Blockchain classes, How to run and import python files

---

## Fundamentals:

- A block contains:
  +, timestamp
  +, last_hash
  +, data
  +, hash

- Mine block (5th Commit):
  +, meaning: create a new and valid block instance

- Genesist block (5th Commit):
  +, First block of the Blockchain

---

## PYTHON FUNDAMENTALS: COMMIT HISTORY:

1, 4th Commit: Defining Block and Blockchain classes, How to run and import python files

    a, Introduction to Blockchain & Crypto currency:
        +, What is Blockchain
        +, Why do we use Blockchain
        +, How does Cryptocurrency uses Blockchain

    => See video 15

    b, How to run python file:
        +, cd to the directory of the file
        +, $ python3 filename.py
        (must use the default __repr__ methods in order
            for the presentation to be readable string)

    c, How to impor python file to other python file:
        +, See blockchain.py file to see how block is imported
        +, When a file is imported, it is fully executed
        +, The __name__ variable show the file name,
            it will show __main__ when it is executed directly with python3

            For example: if you execute:
            $ python3 block.py
            __name__ in python will show __main__
            otherwise it will show block

---

2, 5th Commit: Mining Blocks and the Genesis Block:

    - What is Mining Blocks & Genesis Block:
        +, See in "Fundamentals" above

    - See code in block.py to see how to mine a block and create a genesis block

    - Run the following command to see the result:
        +, $ python3 block.py
