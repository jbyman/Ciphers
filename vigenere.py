
#
# Vigenere Cipher
#

from cipher import Cipher
from typing import List
from utils import index_of_spaces, get_text_data, get_frequency_dict, subtract_letters, list_to_string, next_letter

class Vigenere(Cipher):

    def _get_next_letter(self, letter1: str, letter2: str) -> str:
        """
        Helper function to add two letters together
        """

        increment = ord(letter2) % 65
        ascii_value = ord(letter1) + increment

        if ascii_value > 90:
            ascii_value = ascii_value - 90

        if ascii_value < 65:
            ascii_value += 65

        return chr(ascii_value)


    def encrypt(self, plaintext: str, key: List[str]) -> str:
        """
        Given plaintext and an encryption key,
        return the encrypted text using the Vigenere cipher
        """

        key_index = 0
        
        ciphertext = ""

        for ch in plaintext:
            if ch == " ":
                ciphertext += " "
                continue

            encryption_letter = key[key_index % len(key)]
            
            new_character = self._get_next_letter(ch, encryption_letter)
            ciphertext += new_character
            key_index += 1

        return ciphertext


    def decrypt(self, ciphertext: str, key_length: int) -> str:
        """
        Given a piece of ciphertext encrypted using a Vigenere cipher,
        with a key of a specified length, return the plaintext
        """

        #
        # Does the text have spaces in it?
        #

        spaces = index_of_spaces(ciphertext)
        ciphertext_without_spaces = ciphertext.replace(" ", "")

        standard_distribution = get_frequency_dict(get_text_data('data/dictionary.txt'))

        key = self.find_key_from_frequencies(ciphertext=ciphertext_without_spaces,
                                        standard=standard_distribution,
                                        key_length=key_length)

        decryption = self.insert_spaces_back(self.reverse_vigenere(ciphertext_without_spaces, key),
                                    spaces)

        return decryption


    def reverse_vigenere(self, ciphertext: str, key: List[str]) -> str:
        """
        Opposite of a Vigenere cipher. Goes backwards instead of forwards
        @param ciphertext is the encrypted text
        @key is the key from which to move backwards
        @returns the attempted plaintext
        """

        res = []
        key_index = 0
        for letter in ciphertext:
            if letter == ' ':
                continue
            res.append(subtract_letters(letter, key[key_index]))
            key_index += 1
            if key_index > len(key) - 1:
                key_index = 0
        res = list_to_string(res)
        return res


    def get_index_lists(self, key_length: int, text_length: int) -> dict:
        """
        Given a key length and a text length, give back a list of lists
        for indices up to the text length

        @param key_length is the length of the key in the vigenere cipher
        @param text_length is the limit for the text
        @returns a dictionary of integer lists as above
        """

        res = {}

        key_length = int(key_length)
        for i in range(key_length):
            res[i] = []

        num_keys = int(text_length / key_length)
        for i in range(key_length):
            for g in range(num_keys):
                res[i].append(i + g * key_length)
        return res


    def find_key_from_frequencies(self, ciphertext: str, standard: List[str], key_length: int) -> str:
        """
        Finds the most likely key used to turn the ciphertext into English
        text

        @param ciphertext is the full ciphertext
        @param standard is the standard distribution of letters with frequencies
        @param key_length is the length of the key
        @returns the most likely key
        """

        key_letter_texts = self.texts_by_period(ciphertext, key_length)

        key = ""
        for key_letter in key_letter_texts:
            key += self.find_letter_by_chi_squared(key_letter, standard, key_length)

        return key


    def find_letter_by_chi_squared(self, word: str, standard: List[str], key_length: int) -> str:
        """
        Given a word, returns the letter that, when used in a
        Caesar shift on the text, gives the lowest Chi-Squared value,
        meaning the one that makes the letters most like the standard
        distribution

        @param word is the word you are shifting
        @param standard is the standard distribution of letters
        @param key_length is the length of the key
        @returns the most likely needed letter for that word
        to shift the text to have an English-like distribution
        """

        res = {}
        letter = 'A'

        for i in range(26):
            caesar_shift = self.reverse_vigenere(word, letter)
            res[letter] = self.chi_squared(caesar_shift, standard, key_length)
            letter = next_letter(letter)

        min_chi = max(res.values())
        best_letter = ''
        for k, v in res.items():
            if v < min_chi:
                best_letter = k
                min_chi = v
        return best_letter


    def chi_squared(self, text: str, standard: List[str], key_length: int) -> float:
        """
        Finds the Chi-Squared value of the text
        based on the standard distribution of letters

        @param text is the text you are analyzing
        @standard is the dictionary of letter : frequency
        @key_length is the length of the key
        @returns a Chi-Squared value representing how close the text
        is to the standard distribution
        """

        text_length = len(text)

        chi_squared_sum = 0.0
        for i in range(len(text)):
            letter = text[i]
            count_of_letter = float(text.count(letter))

            expected_count_of_letter = standard[letter] * text_length
            val = count_of_letter - expected_count_of_letter
            val *= val
            val /= expected_count_of_letter
            chi_squared_sum += val

        return chi_squared_sum


    def texts_by_period(self, ciphertext: str, key_length: int) -> List[str]:
        """
        Returns a list of strings of characters
        separated by key_length

        @param ciphertext is the full text
        @param key_length is the length of the key
        @returns a list of texts based on the key and the text
        """

        res = []

        indices = self.get_index_lists(key_length, len(ciphertext)).values()

        for index_list in indices:
            l = []
            for index in index_list:
                l.append(ciphertext[index])
            res.append(list_to_string(l))
        return res


    def insert_spaces_back(self, text: str, indices: List[int]) -> List[str]:
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

