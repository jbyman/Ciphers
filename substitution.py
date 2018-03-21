
#
# Substitution Cipher
#

from cipher import Cipher
from utils import STANDARD_ALPHABET, STANDARD_ALPHABET_FREQUENCIES
from random import randint

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

    def _ciphertext_to_plaintext_key_map(self, key):
        """
        Return a map from ENCRYPTED_ALPHABET -> STANDARD_ALPHABET
        """

        result = {}

        i = 0
        for letter in key:
            result[key[i]] = STANDARD_ALPHABET[i]
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


    def _text_score(self, text):
        """
        Use log frequency analysis to analyze how close to plaintext
        a piece of text is
        """

        score = 0.0

        return score


    def _adjust_letters_in_key(self, key, letter1, letter2):
        """
        Swap two letters in a key and return the new adjusted key
        """

        new_key = []

        for key_letter in key:
            if key_letter == letter1:
                new_key.append(letter2)
            elif key_letter == letter2:
                new_key.append(letter1)
            else:
                new_key.append(key_letter)

        return new_key


    def _decryption_attempt(self, ciphertext, key):
        """
        Given a key and a piece of ciphertext, return the attempted
        plaintext
        """

        attempt = ""

        decryption_dict =self._ciphertext_to_plaintext_key_map(key)

        for letter in ciphertext:
            attempt += decryption_dict[letter]

        return attempt


    def decrypt(self, ciphertext):
        """
        Given a ciphertext encrypted with a substitution cipher, return
        the plaintext
        """

        plaintext = ""

        key = STANDARD_ALPHABET_FREQUENCIES

        decrypted = False
        best_score = 0.0
        while not decrypted:

            #
            # Attempt to decrypt with our current key
            #

            attempt = self._decryption_attempt(ciphertext, key)

            #
            # Calculate a score for this key
            #

            score = self._text_score(attempt)

            #
            # Is this score good enough?
            #

            if score > 0.5:
                plaintext = attempt
                key = key
                decrypted = True
                break

            #
            # See if this score is the best so far
            #

            if score > best_score:
                best_score = score

            #
            # As part of the hill-climbing algorithm, have a certain amount of randomness
            #

            if randint(0, 10) == 1:

                #
                # Generate new key
                #

                rand1 = randint(0, 25)
                rand2 = randint(0, 25)

                key = self._adjust_letters_in_key(key, key[rand1], key[rand2])

            else:

                #
                # Calculate a key based on a smart decision...
                #

                key = key
    
        return plaintext
