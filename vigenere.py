
#
# Vigenere Cipher
#

from cipher import Cipher
from utils import *

class Vigenere(Cipher):

    def encrypt(self, plaintext, key):
        """
        Given plaintext and an encryption key,
        return the encrypted text using the Vigenere cipher
        """

        pass


    def decrypt(self, ciphertext, key_length):
        """
        Given a piece of ciphertext encrypted using a Vigenere cipher,
        with a key of a specified length, return the plaintext
        """

        #
        # Does the text have spaces in it?
        #

        spaces = index_of_spaces(file_data)
        ciphertext_without_spaces = file_data.replace(" ", "")

        standard_distribution = get_frequency_dict(get_text_data('dictionary.txt'))

        key = self.find_key_from_frequencies(ciphertext=ciphertext_without_spaces,
                                        standard=standard_distribution,
                                        key_length=key_length)

        decryption = insert_spaces_back(reverse_vigenere(ciphertext_without_spaces, key),
                                    spaces)

        return decryption


    def get_index_lists(self, key_length, text_length):
        """
        Given a key length and a text length, give back a list of lists
        for indices up to the text length

        @param key_length is the length of the key in the vigenere cipher
        @param text_length is the limit for the text
        @returns a dictionary of integer lists as above
        """

        res = {}

        for i in range(key_length):
            res[i] = []

        for i in range(key_length):
            for g in range(text_length / key_length):
                res[i].append(i + g * key_length)
        return res


    def find_key_from_frequencies(self, ciphertext, standard, key_length):
        """
        Finds the most likely key used to turn the ciphertext into English
        text

        @param ciphertext is the full ciphertext
        @param standard is the standard distribution of letters with frequencies
        @param key_length is the length of the key
        @returns the most likely key
        """

        key_letter_texts = texts_by_period(ciphertext, key_length)

        key = ""
        for key_letter in key_letter_texts:
            key += find_letter_by_chi_squared(key_letter, standard, key_length)

        return key


    def find_letter_by_chi_squared(self, word, standard, key_length):
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
            caesar_shift = reverse_vigenere(word, letter)
            res[letter] = chi_squared(caesar_shift, standard, key_length)
            letter = next_letter(letter)

        min_chi = max(res.values())
        best_letter = ''
        for k, v in res.iteritems():
            if v < min_chi:
                best_letter = k
                min_chi = v
        return best_letter


    def chi_squared(self, text, standard, key_length):
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

    def texts_by_period(self, ciphertext, key_length):
        """
        Returns a list of strings of characters
        separated by key_length

        @param ciphertext is the full text
        @param key_length is the length of the key
        @returns a list of texts based on the key and the text
        """

        res = []

        indices = get_index_lists(key_length, len(ciphertext)).values()

        for index_list in indices:
            l = []
            for index in index_list:
                l.append(ciphertext[index])
            res.append(list_to_string(l))
        return res


