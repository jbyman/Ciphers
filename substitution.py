
#
# Substitution Cipher
#

from cipher import Cipher
from utils import *

class Substitution(Cipher):

    def encrypt(self, plaintext, key):
        pass


    def decrypt(self, ciphertext):
        pass


    def swap(index1, index2, l):
        """
        Given two indices, switch the elements at those two indices
        and return the new list

        @param index1 is the first index
        @param index2 is the second index
        @param l is the list in which you are switching
        @returns the new list with swapped elements
        """

        temp = l[index1]
        l[index1] = l[index2]
        l[index2] = temp

        return l


    def adjust(encrypted_three, standard_alphabet, encrypted_alphabet):
        """
        Switches the most used three-letter word letters with 'T', 'H', and 'E'
        in the standard alphabet to match up with the encrypted. Used in
        substitution cracking.

        @param encrypted_three is the 3-letter word you are replacing with 'the'
        @param standard_alphabet is the standard alpahbet you are rearranging
        @param encrypted_alphabet is the encrypted alphabet you are using for
        indices
        @returns the adjusted list
        """

        index_of_t = encrypted_alphabet.index(encrypted_three[0])
        index_of_h = encrypted_alphabet.index(encrypted_three[1])
        index_of_e = encrypted_alphabet.index(encrypted_three[2])

        l = swap(index_of_t, standard_alphabet.index('T'), standard_alphabet)
        l = swap(index_of_h, standard_alphabet.index('H'), l)
        return swap(index_of_e, standard_alphabet.index('E'), l)


    def replace_letters(string, encrypted, standard):
        """
        Given a string, replace each encrypted letter with its equivalent
        frequency plaintext letter

        @param string is the string in which to replace characters
        @param encrypted is the encrypted letter alphabet
        @param standard is the standard language letter alphabet
        @returns the new decrypted string
        """

        res = ""
        for letter in string:
            if letter not in standard:
                res += letter
            else:
                encrypted_distribution_index = encrypted.index(letter)
                res += standard[encrypted_distribution_index]
        return res

    def get_alphabet_mapping(filename):
        """
        Given a filename, return a 2D list of [alphabet1, alphabet2] representing
        two alphabet list mappings

        @param filename is the filename containing the two alphabets
        @returns the 2D list
        """

        with open(filename) as data:
            res = []
            for line in data.read().splitlines():
                alphabet = []
                for letter in line:
                    alphabet.append(letter)
                res.append(alphabet)
        return res


    def n_letter_words(all_words, n):
        """
        Given a collection of words, return the ones that are
        three letters

        @param all_words is the string containing all words
        @returns a list of three-letter words
        """

        res = []
        all_words = all_words.split(" ")
        print(all_words)
        for word in all_words:
            if len(word) == n:
                res.append(word)
        return res


    def most_used_n_letter_words(n_letter_word_list):
        """
        Given a list of three-letter words,
        returns which is the most commonly used

        @param three_letter_word_list is the word list
        @returns the most common three-letter word
        """

        used_words = []
        word_dict = {}
        for word in n_letter_word_list:
            if word not in used_words:
                word_dict[word] = 0
                used_words.append(word)
            else:
                word_dict[word] += 1
        res = as_list(as_sorted_tuple_list(word_dict))
        return res


    def reverse_vigenere(ciphertext, key):
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
            res.append(letter_from_difference(letter, key[key_index]))
            key_index += 1
            if key_index > len(key) - 1:
                key_index = 0
        res = list_to_string(res)
        return res


    def letter_from_difference(letter1, letter2):
        """
        Returns the letter needed to transform letter1 into letter2
        Example: letter_from_difference('B', 'C') -> 'B' because 'B' = 1,
        and 'B' + 1 = 'C'

        @param letter1 is the first letter
        @param letter2 is the second letter
        @returns the letter needed
        """

        diff = (ord(letter1) - ord(letter2))

        if diff < 0:
            diff = 26 + diff
        elif diff + 65 > 90:
            diff -= 65

        return chr(65 + diff)


    def as_sorted_tuple_list(dic):
        """
        Given a dictionary, sort the key:value pairs into a tuple-list

        @param dic is the dictionary of letter:frequency
        @returns the (key, value) list in descending order based on value
        """

        res = []
        for k, v in dic.items():
            res.append((k, v))
        return list(reversed(sorted(res, key=lambda x: x[1])))


