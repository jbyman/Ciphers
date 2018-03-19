
#
# Substitution Cipher
#

from cipher import Cipher
from utils import *

class Substitution(Cipher):

    def _plaintext_to_ciphertext_key_map(self, key):
        """
        Return a map from STANDARD_ALPHABET -> ENCRYPTED_ALPHABET
        """
        
        result = {}

        i = 0
        for letter in key:
            result[STANDARD_ALPHABET[i]] = letter
            i += 1

        return result


    def encrypt(self, plaintext, key):
        """
        Given a piece of plaintext and an alphabet key, return the ciphertext
        """

        if len(key) != 26:
            raise Exception('Invalid Key. Must be 26 letters')
        
        key_map = self._plaintext_to_ciphertext_key_map(key)
        
        ciphertext = ""

        for ch in plaintext:
            if ch == " ":
                ciphertext += " "
                continue

            ciphertext += key_map[ch]

        return ciphertext


    def decrypt(self, ciphertext):
        """
        Given a ciphertext encrypted with a substitution cipher, return
        the plaintext
        """

        plaintext = ""
        

        return plaintext
