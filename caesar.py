
#
# Caesar Cipher
#

from cipher import Cipher
from utils import add_letters, subtract_letters, english_words_percentage

class Caesar(Cipher):

    def encrypt(self, plaintext: str, key: str) -> str:
        """
        Given an encryption letter and a piece of plaintext,
        return the ciphertext using the Caesar cipher
        """

        if len(key) != 1:
            raise Exception('Invalid Key. Must be of length 1')

        ciphertext = ""

        for ch in plaintext:
            if ch == " ":
                ciphertext += " "
                continue

            next_letter = add_letters(ch, key)
            ciphertext += next_letter

        return ciphertext

    def _decryption_attempt(self, ciphertext: str, letter: str) -> str:
        """
        Go backwards
        """
        
        plaintext = ""
        for c in ciphertext:
            if c == " ":
                plaintext += " "
                continue

            next_letter = subtract_letters(c, letter)
            plaintext += next_letter

        return plaintext


    def decrypt(self, ciphertext: str) -> str:
        """
        Returns the decrypted caesar_shift
        @param ciphertext is the encrypted text
        @param spaces is the indices of the spaces in the original text
        @returns the decrypted text
        """

        letter = 'A'
        for i in range(26):
            attempt = self._decryption_attempt(ciphertext, letter)
            letter = chr(ord(letter) + 1)

            if english_words_percentage(attempt) > 0.5:
                return attempt
        
        return "UNABLE TO DECRYPT"
