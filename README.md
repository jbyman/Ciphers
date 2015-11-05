# Vigenère/Substitution Cipher Decryptor
This is a Python script used to decrypt Substitution and Vigenère Ciphers. It takes in the name of a file
containing encrypted text and, using frequency analysis, decrypts into English plaintext.

# Running the Script

### Substitution
In order to run the substitution decryption, you pass the command:

    python cipher_cracker.py MyFile.txt SUBSTITUTION True

Where `MyFile.txt' is the name of the file containing encrypted text, and "True" dictates whether this is the first time running. The substitution mapping will be outputted to the "alphabets.txt" file.

### Vigenère
In order to run the Vigenère decryption, you pass the command:

    python cipher_cracker.py MyFile.txt VIGENERE 10

Where `MyFile.txt' is the name of the file containing encrypted text, and "10" dictates the length of the key used to encrypt the text.
