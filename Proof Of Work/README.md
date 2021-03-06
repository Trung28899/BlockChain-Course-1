## PROOF OF WORK: TABLE OF CONTENT:

1. 11st Commit: Difficulty and nonce value
2. 12nd Commit: Implementing Dynamic Difficulty based on Fixed Mine Rate
3. 13rd Commit: Average Work Script
4. 14th Commit: Hex To Binary Conversion

---

## FUNDAMENTALS:

- See Handbook to understand the concept of Proof of Work

---

## COMMANDS:

`$ cd "Proof Of Work"`
`$ python3 -m backend.blockchain.block`
`$ python3 -m pytest backend/tests`
`$ python3 -m backend.scripts.average_block_rate`

---

## COMMIT HISTORY:

1.  11st Commit: Difficulty and nonce value

        - This commit helps to understand the basic of
            Difficulty and nonce value to create a hash that is
            satisfy Proof Of Work

        - See file: backend/blockchain/block.py
            +, See function: mine_block()
            +, See def main()

        - See file: backend/tests/blockchain/test_block.py:
            +, test_mine_block()
            +, Command: `$ python3 -m pytest backend/tests`

        - Run this command:

    `$ cd "Proof Of Work"`
    `$ python3 -m backend.blockchain.block`

> See the output of the hash, difficulty and nonce

2.  12nd Commit: Implementing Dynamic Difficulty based on Fixed Mine Rate

        - This commit show how to difficulty can be changed based on Fixed Mine Rate:
            +, Basically, the system compare the timestamp of the last block creation to
                the new block that is created
            +, If differences in timestamp larger than the Mine Rate > difficulty will
                be decreased
            +, If differences in timestamp lower than the Mine Rate > difficulty will
                be increased


        - Implementation:
            +, backend/blockchain/block.py: See:

                > adjust_difficulty(last_block, new_timestamp)

                > mine_block(last_block, data)

            +, Run this command to see output:

    `$ python3 -m backend.blockchain.block`

        - Test:
            +, See how to test this dynamic difficulty system:
            +, See files: backend/tests/blockchain/test_block.py:

                test_quickly_mined_block()
                test_slowly_mined_block()
                test_mined_block_difficulty_limits_at_1()

            +, Run this command to see output:

    `$ python3 -m pytest backend/tests`

3.  13rd Commit: Average Work Script

        - This Commit is to see how does the Proof Of Work System work by
            running a script that create 100 blocks and print out:

            +, Difficulty
            +, Time to mine new block
            +, Average time to add blocks

        - See code in: backend/scripts/average_block_rate.py
            +, Run command:

    `$ python3 -m backend.scripts.average_block_rate`

        - Note that the average time to add block won't be close to 4s
        but the block are adjusting to have the MINE_RATE of 4s.

        Average time to add block will be about 2.8s
        Next commit we will optimized to have the average time
        to add block closer to the mine rate which is 4s

4.  14th Commit: Hex To Binary Conversion

        - In this commit we implement a hex to binary conversion function:
            +, This helps complicate the algorithm so that the average time
            to add block closer to the mine rate which is 4s

        - See files:
            +, backend/utils/hex_to_binary.py
            +, backend/tests/utils/test_hex_to_binary.py for testing
            +, backend/blockchain/block.py: See how hex_to_binary() is used
            +, Run command down below to see result:

    `$ python3 -m backend.scripts.average_block_rate`
    `$ python3 -m pytest backend/tests`
