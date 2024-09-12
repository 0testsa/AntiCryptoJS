import argparse
import base64
from Crypto.Cipher import AES, DES
from Crypto.Util.Padding import pad, unpad
import sys
import os

# Define a dictionary mapping algorithms to their respective block sizes
ALGORITHMS = {
    'AES': {
        'cipher': AES,
        'default_block_size': AES.block_size
    },
    'DES': {
        'cipher': DES,
        'default_block_size': DES.block_size
    }
}

def encrypt(algorithm, key, iv, data, block_size):
    """
    Encrypt data using the specified algorithm, key, iv, and block size.
    """
    try:
        cipher = ALGORITHMS[algorithm]['cipher'].new(key, ALGORITHMS[algorithm]['cipher'].MODE_CBC, iv)
        encrypted_data = cipher.encrypt(pad(data.encode(), block_size))
        return base64.b64encode(encrypted_data).decode('utf-8')
    except Exception as e:
        raise ValueError(f"Encryption failed: {e}")

def decrypt(algorithm, key, iv, data, block_size):
    """
    Decrypt data using the specified algorithm, key, iv, and block size.
    """
    try:
        encrypted_data = base64.b64decode(data)
        cipher = ALGORITHMS[algorithm]['cipher'].new(key, ALGORITHMS[algorithm]['cipher'].MODE_CBC, iv)
        decrypted_data = unpad(cipher.decrypt(encrypted_data), block_size)
        return decrypted_data.decode('utf-8')
    except ValueError as e:
        raise ValueError(f"Decryption failed: {e}")
    except Exception as e:
        raise ValueError(f"An error occurred during decryption: {e}")

def main():
    parser = argparse.ArgumentParser(description="Encrypt or decrypt data using various algorithms.",
                                     epilog="""Examples:
  Encrypt using AES:
    python AntiCryptoJS.py --alg AES --key your_key_here --iv your_iv_here --enc "your data to encrypt"
  Encrypt using AES with a specified block size:
    python AntiCryptoJS.py --alg AES --key your_key_here --iv your_iv_here --block_size 16 --enc "your data to encrypt"
  Decrypt using AES:
    python AntiCryptoJS.py --alg AES --key your_key_here --iv your_iv_here --dec "your encrypted data"
  Encrypt using DES:
    python AntiCryptoJS.py --alg DES --key your_key_here --iv your_iv_here --enc "your data to encrypt"
  Encrypt using DES with a specified block size:
    python AntiCryptoJS.py --alg DES --key your_key_here --iv your_iv_here --block_size 8 --enc "your data to encrypt"
  Decrypt using DES:
    python AntiCryptoJS.py --alg DES --key your_key_here --iv your_iv_here --dec "your encrypted data"
""")
    parser.add_argument('--alg', required=True, choices=ALGORITHMS.keys(), help='Algorithm to use (AES or DES)')
    parser.add_argument('--key', required=True, help='Encryption key')
    parser.add_argument('--iv', required=True, help='Initialization vector')
    parser.add_argument('--block_size', type=int, help='Block size for padding (default is algorithm-specific)')
    parser.add_argument('--enc', action='store_true', help='Encrypt the data')
    parser.add_argument('--dec', action='store_true', help='Decrypt the data')
    parser.add_argument('data', help='The data to encrypt or decrypt or path to a file containing the data')

    args = parser.parse_args()

    try:
        key = args.key.encode()
        iv = args.iv.encode()
    except Exception as e:
        print(f"Error encoding key or iv: {e}")
        sys.exit(1)
    
    algorithm = args.alg
    default_block_size = ALGORITHMS[algorithm]['default_block_size']
    block_size = args.block_size if args.block_size else default_block_size

    # Validate key length
    if algorithm == 'AES' and len(key) not in {16, 24, 32}:
        print("AES key must be 16, 24, or 32 bytes long")
        sys.exit(1)
    elif algorithm == 'DES' and len(key) != 8:
        print("DES key must be 8 bytes long")
        sys.exit(1)

    # Validate IV length
    if len(iv) != default_block_size:
        print(f"{algorithm} IV must be {default_block_size} bytes long")
        sys.exit(1)

    # Ensure block size is a multiple of the algorithm's default block size
    if block_size % default_block_size != 0:
        print(f"Block size must be a multiple of {default_block_size} bytes for {algorithm}")
        sys.exit(1)

    # Ensure only one operation (encrypt or decrypt) is specified
    if args.enc and args.dec:
        print("Cannot encrypt and decrypt at the same time")
        sys.exit(1)

    # Read data from file if it's a valid file path, otherwise use direct input
    data = ""
    if os.path.isfile(args.data):
        try:
            with open(args.data, 'r') as f:
                data = f.read().strip()
        except Exception as e:
            print(f"Error reading file: {e}")
            sys.exit(1)
    else:
        data = args.data

    # Perform encryption or decryption
    try:
        if args.enc:
            result = encrypt(algorithm, key, iv, data, block_size)
            print(f"Encrypted data:\n\n{result}")
        elif args.dec:
            result = decrypt(algorithm, key, iv, data, block_size)
            print(f"Decrypted data:\n\n{result}")
        else:
            print("Must specify either --enc or --dec")
            sys.exit(1)
    except ValueError as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()
