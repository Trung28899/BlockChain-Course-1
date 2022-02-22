import hashlib
import json

"""

stringified_args = map(lambda data: json.dumps(data), args)

IS THE SAME AS:  

def stringify(data): 
    return json.dumps(data)

stringified_args = map(stringify, args)

"""


def crypto_hash(*args): 
    """
        Return a sha-256 hash of the given arguments
        you can put 1, 2, 3 or as many arguments as you want to create 
        a hash for this function

        Has to:
            +, Make data a string before encoding it 
                => this is because if data is not a string (a number, boolean, array, etc.), 
                    it won't be encoded
            +, encode the data before hashing it
    """
    stringified_args = sorted(map(lambda data: json.dumps(data), args))
    
    # print(f'stringified_args: {stringified_args}')
    joined_data = ''.join(stringified_args)

    ## remove the sort function in stringified_args => output will be different
    # print(f'joined_data: {joined_data}')
    
    encodedData = joined_data.encode('utf-8')
    return hashlib.sha256(encodedData).hexdigest()

def main(): 
    print(f"\ncrypto_hash('one', 2, [3]): {crypto_hash('one', 2, [3])}")
    print(f"\ncrypto_hash(2, 'one', [3]): {crypto_hash(2, 'one', [3])}")

if __name__ == '__main__': 
    main()