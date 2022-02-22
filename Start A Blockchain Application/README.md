## START THE BLOCKCHAIN APPLICATION: TABLE OF CONTENT:

1, 4th Commit: Defining Block and Blockchain classes, How to run and import python files

---

## FUNDAMENTALS:

- A block contains:
  +, timestamp
  +, last_hash
  +, data
  +, hash

- Mine block (5th Commit):
  +, meaning: create a new and valid block instance

- Genesist block (5th Commit):
  +, First block of the Blockchain

- Static Method (6th Commit):
  +, Much like class method, are methods that are bounds to a class rather than its object
  +, They do not require a class instance creation. They are not dependent on
  the state of the object

- Block hash (7th Commit):
  +, Generated from the timestamp, given data and the last_hash

- SHA-256 (7th Commit):
  +, S: Secure, H: Hash, A: Algorithm
  +, 256 represent the size of 256 bit for the hash value

  +, Benefit of SHA-256:

  -> Produces an unique value for unique input
  -> A one-way function: you can only encrypt, you cannot decrypt it

- Other Terms for cryptography (7th Commit):
  +, ENCODING: The process of converting data into an alternate representation

  +, CHARACTER ENCODING: Most often in programming, Character Encoding is used.
  This means that string will be converted to a lower data type like a set of bytes

  +, UTF-8 ENCODING: a method of encoding that convert each character in a string
  to 8 bits byte (contains 0 and 1)

  +, DECODING: The process of converting encoded data back to its original format

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
        +, `$ python3 filename.py`
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
        +, `$ python3 block.py`

---

3, 6th Commit: Static method in python and Refactor code

    - Update static methods in block.py
    - Refactor code in blockchain.py

    => still the same code as 5th commit but just
        refactor for better code presentation

---

4, 7th Commit: Lambda Functions in Python, Hashing Algorithm Completed

    - Lambda function in python:
      +, See crypto_hash.py first comment

    - Completed Hashing algorithm:
      +, See crypto_hash.py

    - Basic terms and fundamentals:
      +, Block hash
      +, SHA-256
      +, UTF-8
      +, Encoding, Decoding
