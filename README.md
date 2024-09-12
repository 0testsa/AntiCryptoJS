# AntiCryptoJS Script

This project contains a script for encrypting and decrypting data using AES and DES algorithms that generaly used by crypto-js library. It also includes a test script to validate the functionality of the AntiCryptoJS script. The main goal of this script is to help the Penetration Tester to deal with encrypted client-side data in their assement.

## Requirements

Install the required dependencies using:

```bash
pip install -r requirements.txt
```

## Usage

### Help

Run the script with the `-h` or `--help` flag to see the help message:

```bash
python AntiCryptoJS.py -h
```

The help message displays the following information:

```
usage: AntiCryptoJS.py [-h] --alg {AES,DES} --key KEY --iv IV [--block_size BLOCK_SIZE] [--enc] [--dec] data

Encrypt or decrypt data using various algorithms.

positional arguments:
  data                  The data to encrypt or decrypt or path to a file containing the data

options:
  -h, --help            show this help message and exit
  --alg {AES,DES}       Algorithm to use (AES or DES)
  --key KEY             Encryption key
  --iv IV               Initialization vector
  --block_size BLOCK_SIZE
                        Block size for padding (default is algorithm-specific)
  --enc                 Encrypt the data
  --dec                 Decrypt the data

Examples:
  Encrypt using AES:
    python AntiCryptoJS.py --alg AES --key testtestte@12345 --iv testtestte@12345 --enc "your data to encrypt"
  Encrypt using AES with a specified block size:
    python AntiCryptoJS.py --alg AES --key testtestte@12345 --iv testtestte@12345 --block_size 16 --enc "your data to encrypt"
  Decrypt using AES:
    python AntiCryptoJS.py --alg AES --key testtestte@12345 --iv testtestte@12345 --dec "your encrypted data"
  Encrypt using DES:
    python AntiCryptoJS.py --alg DES --key DESKey@8 --iv DESKey@8 --enc "your data to encrypt"
  Encrypt using DES with a specified block size:
    python AntiCryptoJS.py --alg DES --key DESKey@8 --iv DESKey@8 --block_size 8 --enc "your data to encrypt"
  Decrypt using DES:
    python AntiCryptoJS.py --alg DES --key DESKey@8 --iv DESKey@8 --dec "your encrypted data"
```
### Encrypting Data

Encrypt data using AES with direct input:

```bash
python AntiCryptoJS.py --alg AES --key testtestte@12345 --iv testtestte@12345 --enc "your data to encrypt"
```

Encrypt data using AES with a specified block size:

```bash
python AntiCryptoJS.py --alg AES --key testtestte@12345 --iv testtestte@12345 --block_size 16 --enc "your data to encrypt"
```

Encrypt data using AES with file input:

```bash
python AntiCryptoJS.py --alg AES --key testtestte@12345 --iv testtestte@12345 --enc "path_to_your_file"
```

Encrypt data using DES with direct input:

```bash
python AntiCryptoJS.py --alg DES --key DESKey@8 --iv DESKey@8 --enc "your data to encrypt"
```

### Decrypting Data

Decrypt data using AES with direct input:

```bash
python AntiCryptoJS.py --alg AES --key testtestte@12345 --iv testtestte@12345 --dec "your encrypted data"
```

Decrypt data using AES with file input:

```bash
python AntiCryptoJS.py --alg AES --key testtestte@12345 --iv testtestte@12345 --dec "path_to_your_file"
```

Decrypt data using DES with direct input:

```bash
python AntiCryptoJS.py --alg DES --key DESKey@8 --iv DESKey@8 --dec "your encrypted data"
```

## Running Tests

To run the provided test cases, use the `AntiCryptoJS_testing.py` script. This script will test various encryption and decryption scenarios for both AES and DES algorithms using different keys and initialization vectors.

### Test Cases

1. **Encrypt using AES with direct input**: This test case uses AES with the key and IV "testtestte@12345" to encrypt a test message.
2. **Decrypt using AES with direct input**: This test case uses AES with the key and IV "testtestte@12345" to decrypt a provided encrypted message.
3. **Encrypt using DES with direct input**: This test case uses DES with a different key and IV to encrypt a test message.
4. **Decrypt using DES with direct input**: This test case uses DES with a different key and IV to decrypt a placeholder encrypted message.
5. **Encrypt using AES with file input**: This test case uses AES with the key and IV "testtestte@12345" to encrypt data read from a file.
6. **Decrypt using AES with file input**: This test case uses AES with the key and IV "testtestte@12345" to decrypt data read from a file.

To run the tests:

```bash
python AntiCryptoJS_testing.py
```

This will execute all the test cases and print the results to the console.


## Notes

- Ensure that the key and IV lengths are appropriate for the chosen algorithm (AES: 16, 24, or 32 bytes for the key and 16 bytes for the IV; DES: 8 bytes for the key and IV).
- The provided test cases assume specific keys and IVs; adjust these as necessary for your use case.
- The test data file `/Path/to/data/file` should contain valid data for encryption/decryption tests.

If you encounter any issues or have any questions, please feel free to reach out.
