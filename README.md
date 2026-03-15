# RSA
A Python-based exploration of RSA public-key cryptography and integer factorization. Includes tools to generate large primes, create RSA key pairs, encrypt/decrypt files, and test factorization vulnerabilities using Brute Force and Fermat's method. Created as a high school final project. 

# RSA Encryption & Factorization Explorer

## 🚀 Project Overview
This repository contains my final high school project, focusing on the mechanics of RSA public-key cryptography. It is a hands-on implementation of how RSA encryption works under the hood, accompanied by mathematical factorization algorithms designed to test how these keys can be broken.

## 📁 Features & Modules

### Core Cryptography
* **`makePublicPrivateKeys.py`**: Generates RSA public and private key files using randomly generated large primes.
* **`publicKeyCipher.py`**: Encrypts standard text into block integers and decrypts it back to readable text using the generated key files.

### Mathematical Utilities
* **`primeNum.py`**: Handles prime number logic, including a Sieve of Eratosthenes and the Rabin-Miller primality test for generating secure keys.
* **`cryptomath.py`**: Contains essential mathematical functions, such as finding the Greatest Common Divisor (Euclid's Algorithm) and modular inverses (Extended Euclidean Algorithm).

### Factorization & Cracking Tools
* **`bruteForce.py`**: A brute-force trial division script with a timer to test how long it takes to factorize a given modulus.
* **`fermat.py` & `fermat.sage`**: Implementations of Fermat's factorization method in both Python and SageMath to efficiently find factors of odd positive integers.

## ⚙️ How to Use

1.  **Generate Keys:** Run `makePublicPrivateKeys.py` to create your public (`_pubkey.txt`) and private (`_privkey.txt`) keypair files.
2.  **Encrypt & Decrypt:** Run `publicKeyCipher.py` in the same directory as your key files. You can toggle the `mode` variable inside the script to either `'encrypt'` a message to a file or `'decrypt'` an existing file.
3.  **Test Factorization:** Run `bruteForce.py` or `fermat.py` to time how long it takes your machine to factorize large integers.

## 📚 Acknowledgments
* Core cryptography logic and mathematical utilities are based on the BSD-licensed *Cracking Codes with Python* by Al Sweigart.
* The Python implementation of Fermat's factorization was inspired by GeeksforGeeks.
