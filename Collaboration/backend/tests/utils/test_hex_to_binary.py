from backend.utils.hex_to_binary import hex_to_binary

"""
    Testing the function that convert hex value to binary value
    This helped to complicate the Proof Of Work Algorithm
    so that the avarage time to create a block is close to the 
    MINE_RATE
"""
def test_hex_to_binary():
    original_number = 789
    # convert integer to hex
    hex_number = hex(original_number)[2:]
    # convert hex to binary
    binary_number = hex_to_binary(hex_number)
    
    # convert binary to int to compare and test
    assert int(binary_number, 2) == original_number