
#
# Caesar Cipher
#

from cipher import Cipher

class Caesar(Cipher):

    def _get_next_letter(self, letter1, letter2):
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

            next_letter = self._get_next_letter(ch, key)
            ciphertext += next_letter

        return ciphertext


    def decrypt(self, ciphertext):
        """
        Returns the decrypted caesar_shift
        @param ciphertext is the encrypted text
        @param spaces is the indices of the spaces in the original text
        @returns the decrypted text
        """

        letter = 'A'
        for i in range(26):
            new_text = reverse_vigenere(ciphertext, letter)
            letter = next_letter(letter)
            with_spaces = insert_spaces_back(new_text, spaces)

            if english_words_percentage(with_spaces) > 0.5:
                return with_spaces
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
