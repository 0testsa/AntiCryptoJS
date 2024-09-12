import os
import subprocess

# Define the path to the cipher script
cipher_script = "C:\\Users\\Fakeuser\\Desktop\\AntiCryptoJs\\AntiCryptoJS.py"

# Define the path to the test data file
test_data_file = "C:\\Users\\Fakeuser\\Desktop\\AntiCryptoJs\\Testing\\TestData.txt"

# Define test cases
test_cases = [
    {
        "description": "Encrypt using AES with direct input",
        "command": f'python {cipher_script} --alg AES --key testtestte@12345 --iv testtestte@12345 --enc "This is a test message For AES"'
    },
    {
        "description": "Decrypt using AES with direct input",
        "command": f'python {cipher_script} --alg AES --key testtestte@12345 --iv testtestte@12345 --dec "HhCNedWqoD5BaYvt1TWy9+idFr/rYw54qr6Q52rjdHvy76u2Y3iMQI/rwfRHNMHR"'
    },
    {
        "description": "Encrypt using DES with direct input",
        "command": f'python {cipher_script} --alg DES --key DESKey@8 --iv DESKey@8 --enc "This is a test message for DES"'
    },
    {
        "description": "Decrypt using DES with direct input",
        "command": f'python {cipher_script} --alg DES --key DESKey@8 --iv DESKey@8 --dec "3s57apTjTAMm9A6QEmSXdDZ3ODA/s8fCe3P7IYTd4Hwtxm8UPqDexw=="'
    },
    {
        "description": "Encrypt using AES with file input",
        "command": f'python {cipher_script} --alg AES --key testtestte@12345 --iv testtestte@12345 --enc {test_data_file}'
    },
    {
        "description": "Decrypt using AES with file input",
        "command": f'python {cipher_script} --alg AES --key testtestte@12345 --iv testtestte@12345 --dec {test_data_file}'
    }
]

# Run test cases
for test in test_cases:
    print(f"Running test: {test['description']}")
    process = subprocess.Popen(test['command'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print(stdout.decode())
    if stderr:
        print(f"Error: {stderr.decode()}")
    print("-" * 50)
