
#
# Substitution Cipher
#

from cipher import Cipher
from itertools import combinations
from utils import STANDARD_ALPHABET, STANDARD_ALPHABET_FREQUENCIES
from heapq import nlargest
from math import log10
from typing import List, Tuple
import random

class Substitution(Cipher):

    def __init__(self):
        """
        Load n-gram statistics into memory
        """

        self.trigrams = {}

        for line in open('data/trigrams.txt'):
            trigram, count = line.split("\t")
            self.trigrams[trigram] = int(count)

        self.__convert_counts_to_log_scores()


    def _plaintext_to_ciphertext_key_map(self, key: List[str]) -> dict:
        """
        Return a map from STANDARD_ALPHABET -> ENCRYPTED_ALPHABET
        """
        
        result = {}

        i = 0
        for letter in key:
            result[STANDARD_ALPHABET[i]] = letter
            i += 1

        return result


    def _ciphertext_to_plaintext_key_map(self, key: List[str]) -> dict:
        """
        Return a map from ENCRYPTED_ALPHABET -> STANDARD_ALPHABET
        """

        result = {}

        i = 0
        for letter in key:
            result[key[i]] = STANDARD_ALPHABET[i]
            i += 1

        return result


    def encrypt(self, plaintext: str, key: List[str]) -> str:
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


    def __convert_counts_to_log_scores(self) -> None:
        """
        Use log probability to adjust bigram scores from counts to probabilities
        """

        self.trigram_scores = {}

        total = sum(count for _, count in self.trigrams.items())

        for trigram in self.trigrams:
            self.trigram_scores[trigram] = log10(float(self.trigrams[trigram] / total))


    def _text_score_trigrams(self, text: str) -> float:
        """
        Use log frequency analysis to analyze how close to plaintext
        a piece of text is. The better the score, the greater the number.
        Note the scores will typically be negative numbers, so the closer
        to 0 is better

        """

        score = 0.0

        for i in range(len(text) - 2):
            ciphertext_trigram = (text[i] + text[i + 1] + text[i + 2]).lower()

            #
            # Check if the bigram we have here is in list of plaintext trigrams
            #
            
            if ciphertext_trigram in self.trigrams.keys():


                #
                # Great! It is, let's add the corresponding plaintext score
                #

                score += self.trigram_scores[ciphertext_trigram]
            else:
                
                #
                # If it's not, just add a small value
                #

                score += 0.01

        return score


    def _adjust_letters_in_key(self, key: str, letter1: str, letter2: str) -> List[str]:
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


    def _decryption_attempt(self, ciphertext: str, key: list) -> str:
        """
        Given a key and a piece of ciphertext, return the attempted
        plaintext
        """

        attempt = ""

        allowed_punctuation = [' ', '.', ',', ';', "'"]
        decryption_dict =self._ciphertext_to_plaintext_key_map(key)

        for letter in ciphertext:
            if letter in allowed_punctuation:
                attempt += letter
                continue

            attempt += decryption_dict[letter]

        return attempt


    def _get_neighboring_keys(self, key: str, text: str, best_score: float) -> List[Tuple[float, List[str], str]]:
        """
        Return all possible swaps to make for this key that would yield better results
        """

        swaps = list(combinations(range(len(STANDARD_ALPHABET)), 2))
        res = []

        for i, j in swaps:
            new_key = self._adjust_letters_in_key(key, STANDARD_ALPHABET[i], STANDARD_ALPHABET[j])
            attempt = self._decryption_attempt(text, new_key)
            score = self._text_score_trigrams(attempt)

            if score > best_score:
                res.append((score, new_key, attempt))

        return res


    def decrypt(self, ciphertext: str) -> str:
        """
        Given a ciphertext encrypted with a substitution cipher, return
        the plaintext
        """

        plaintext = ""
        best_attempt = ""

        best_key = STANDARD_ALPHABET_FREQUENCIES
        best_score = -99e99

        #
        # To avoid local maxima, get the best result out of 50 iterations
        #

        attempts = 0
        choices = self._get_neighboring_keys(best_key, ciphertext, best_score)
        while(attempts < 20):
            try:

                #
                # Generate neighboring keys
                #
                
                choices = self._get_neighboring_keys(best_key, ciphertext, best_score)

                #
                # Randomly select one in 10 of the keys that would lead to an improved score
                #

                choice = random.choice(nlargest(10, choices))
                score, new_key, attempt = choice
                choices = self._get_neighboring_keys(new_key, ciphertext, score)
                
                #
                # Update variables
                #

                best_key = new_key
                best_attempt = attempt
                best_score = score
            except IndexError:

                #
                # If, given the list of better scores, we cannot find any that is better, we have reached our best attempt
                #
                
                plaintext = best_attempt
                attempts += 1

        return plaintext
