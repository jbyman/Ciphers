
#
# Generic Cipher abstract class
#

from abc import ABC, ABCMeta, abstractmethod
from utils import *

class Cipher(ABC):
    __metaclass__ = ABCMeta

    def __init_(self):
        # first_time_running = sys.argv[3]  # To write to the alphabets.txt file

        # words = n_letter_words(file_data, 3)
        # most = most_used_n_letter_words(words)
        # standard_alphabet = adjust(most, standard_alphabet, encrypted_alphabet)

        # if first_time_running == 'True':
            # alphabet_file = open("alphabets.txt", 'w+')
            # alphabet_file.write(list_to_string(encrypted_alphabet) + "\n")
            # alphabet_file.write(list_to_string(standard_alphabet) + "\n")
            # alphabet_file.close()

        # alphabets = get_alphabet_mapping("alphabets.txt")

        # replaced = replace_letters(string=file_data,
                                   # encrypted=alphabets[0],
                                   # standard=alphabets[1])
        # threshold = english_words_percentage(replaced)
        # print(replaced)
        # print(threshold)

        pass

    @abstractmethod
    def encrypt(self, plaintext, key): pass

    @abstractmethod
    def decrypt(self, ciphertext): pass

