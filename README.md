# DES in Python

This project implements the Data Encryption Standard in Python using built in operations, lists, strings, and integers. It encrypts and decrypts one 64 bit block with a 64 bit key. The implementation uses the DES tables directly and does not use a cryptography package.

## Run the program

Python 3 is the only requirement. Run the program from this folder:

```text
python3 des.py
```

Enter a key and plaintext as 16 hexadecimal digits each. Lowercase hexadecimal letters are accepted. The program prints the plaintext, ciphertext, and decrypted plaintext as 16 hexadecimal digits.

For the example key `133457799BBCDFF1` and plaintext `0123456789ABCDEF`, the ciphertext is `85E813540F0AB405`. Decryption recovers `0123456789ABCDEF`.

## Explore the notebook

[DES_walkthrough.ipynb](DES_walkthrough.ipynb) shows the conversion functions, key schedule, round function, encryption, and decryption in separate code cells. Its Markdown cells explain each step, and its final cell displays results for three key and plaintext combinations. Run the notebook cells from top to bottom in Colab or Jupyter.

## Run the tests

```text
python3 -m unittest discover -s tests -v
```

The tests check expected ciphertexts, decryption, lowercase input, invalid input, and command line output. The additional expected ciphertexts come from [BoringSSL's DES test cases](https://boringssl.googlesource.com/boringssl/%2B/97e8ba8d1dc4b43f560694e11a0df302041f9969/crypto/cipher/test/cipher_test.txt).

DES is studied here as an implementation exercise. Its 56 bit effective key is too small for protecting current data.
