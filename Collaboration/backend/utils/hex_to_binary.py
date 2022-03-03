from backend.utils.crypto_hash import crypto_hash

HEX_TO_BINARY_CONVERSION_TABLE = {
    '0': '0000', 
    '1': '0001', 
    '2': '0010', 
    '3': '0011',     
    '4': '0100', 
    '5': '0101', 
    '6': '0110', 
    '7': '0111', 
    '8': '1000', 
    '9': '1001', 
    'a': '1010', 
    'b': '1011', 
    'c': '1100', 
    'd': '1101', 
    'e': '1110', 
    'f': '1111', 
}

"""
    This function is used in backend/blockchain/block.py
    to complicate the hash. Therefore, we can get the average time 
    to add block closer to the MINE_RATE
"""
def hex_to_binary(hex_string):
    binary_string = ''
    
    for character in hex_string: 
        binary_string += HEX_TO_BINARY_CONVERSION_TABLE[character]

    return binary_string

def main(): 
    number = 451
    """
        hex() is a global function offered by python
        converting number to hexidecimal form

        format will be: 0x000000
        the 0x is the prefix, we dont need it so 
        we take the string from 2nd index to the end
    """
    hex_number = hex(number)[2:]
    print(f'hex_number: {hex_number}')

    binary_number = hex_to_binary(hex_number)
    print(f'binary_number: {binary_number}')

    # int() is a global function offered by python
    # converting back to number to test the function
    original_number = int(binary_number, 2)
    print(f'original_number: {original_number}')

    hext_to_binary_crypto_hash = hex_to_binary(crypto_hash('test-data'))
    print(f'hext_to_binary_crypto_hash: {hext_to_binary_crypto_hash}')


if __name__ == '__main__': 
    main()