# Cipher Encryptor/Decryptor
This is a Python script used to decrypt and encrypt Substitution, Caesar, and Vigenère ciphers. It takes in the name of a file
containing encrypted text and, using frequency analysis, decrypts into English plaintext.

The script should work on Vigenère ciphers with significantly large key lengths (for small paragraphs of text, should experience little-to-no deviation with key lengths of up to 20). However with small amounts of text and large keys, it is possible to experience some statistical deviation by the nature of frequency analysis.

##  Running the Script

### Caesar
In order to run the Caesar decryption, you pass the command:
    
```
    python main.py ENCRYPT CAESAR plaintext.txt B
    python main.py DECRYPT CAESAR ciphertext.txt
```

### Vigenère
In order to run the Vigenère decryption, you pass the command:

```
    python main.py ENCRYPT VIGENERE plaintext.txt APPLE
    python main.py DECRYPT VIGENERE ciphertext.txt 5
```


### Substitution
In order to run the substitution decryption, you pass the command:

```
    python main.py ENCRYPT SUBSTITUTION plaintext.txt CBQEGINKLMZPUORSWTFJVHDXYA
    python main.py DECRYPT SUBSTITUTION ciphertext.txt
```
