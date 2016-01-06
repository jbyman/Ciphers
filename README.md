# Vigenère/Substitution Cipher Decryptor
This is a Python script used to decrypt Substitution and Vigenère Ciphers. It takes in the name of a file
containing encrypted text and, using frequency analysis, decrypts into English plaintext.

The script should work on Vigenère Ciphers with significantly large key lengths (for small paragraphs of text, should experience little-to-no deviation with key lengths of up to 20). However with small amounts of text and large keys, it is possible to experience some statistical deviation by the nature of frequency analysis.

# Running the Script

### Substitution
In order to run the substitution decryption, you pass the command:

    python cipher_cracker.py MyFile.txt SUBSTITUTION True

Where "MyFile.txt" is the name of the file containing encrypted text, and "True" dictates whether this is the first time running. The substitution mapping will be outputted to the "alphabets.txt" file. This is semi-automatic, so after a base frequency analysis is determined, you should change the value to "False" and switch around the letters in the outputted file.

### Vigenère
In order to run the Vigenère decryption, you pass the command:

    python cipher_cracker.py MyFile.txt VIGENERE 10

Where "MyFile.txt" is the name of the file containing encrypted text, and "10" dictates the length of the key used to encrypt the text.
