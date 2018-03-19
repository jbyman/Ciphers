
#
# Caesar Cipher
#

from cipher import Cipher
from utils import *

class Caesar(Cipher):

    def encrypt(self, plaintext, key):
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

    def _decryption_attempt(self, ciphertext, letter):
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


    def decrypt(self, ciphertext):
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


    def insert_spaces_back(self, text, indices):
        """
        Given text and a list of indices, insert spaces at those indices
        Example: insert_spaces_back("HELLOWORLD", [0, 4])

        @param text is the text you are inserting spaces into
        @param indices is the integer list of indices of spaces
        @returns the formatted string with spaces
        """

        string_to_list = []

        for char in text:
            string_to_list.append(char)
        for index in indices:
            string_to_list.insert(index, " ")

        list_to_string = ""

        for elem in string_to_list:
            list_to_string += elem

        return list_to_string
