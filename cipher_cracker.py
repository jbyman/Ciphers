import sys
import string


def get_text_data(filename):
    """
    Given a filename, return the contents of the file

    @param filename is the name of the text file
    @returns the file in string form
    """

    with open(filename, 'rb') as data:
        res = data.read()
    return res.upper()


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


def get_frequency_dict(string):
    """
    Iterate over the ciphertext and determine the frequency of each letter

    @param string is the ciphertext
    @returns a dictionary of letter:frequency
    """

    used_letters = []
    letter_dict = {}
    total_num_words = 0.0
    for letter in string:
        if letter == " " or letter == '\n':
            continue
        total_num_words += 1
        if letter not in used_letters:
            letter_dict[letter] = 1
            used_letters.append(letter)
        else:
            letter_dict[letter] += 1

    for i in letter_dict.keys():
        letter_dict[i] /= total_num_words
    for elem in missing_letters(as_list(letter_dict)):
        letter_dict[elem] = 0
    return letter_dict


def n_letter_words(all_words, n):
    """
    Given a collection of words, return the ones that are
    three letters

    @param all_words is the string containing all words
    @returns a list of three-letter words
    """

    res = []
    all_words = all_words.split(" ")
    for word in all_words:
        if len(word) == n:
            res.append(word)
    return res


def as_sorted_tuple_list(dic):
    """
    Given a dictionary, sort the key:value pairs into a tuple-list

    @param dic is the dictionary of letter:frequency
    @returns the (key, value) list in descending order based on value
    """

    res = []
    for k, v in dic.iteritems():
        res.append((k, v))
    return list(reversed(sorted(res, key=lambda x: x[1])))


def as_list(tup_list):
    """
    Turns a tuple-list into a list of the first element of the tuple

    @param tup_list is the tuple-list you are converting
    @returns the created list
    """

    res = []
    for elem in tup_list:
        res.append(elem[0])
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


def list_to_string(l):
    """
    Converts a string list in to a string

    @param l is the string list
    @returns a concatentation of each element in the list
    """

    res = ""
    for elem in l:
        res += elem
    return res


def string_to_list(str):
    """
    Converts a string to a string list, line separated

    @param str is the string you are converting
    @returns the list
    """

    res = []
    for elem in str.split(" "):
        res.append(elem)
    return res


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


def english_words_percentage(string):
    """
    Given a string, returns the percentage of words that are English words

    @param string is the string you are analysing for proportions
    @param all_english_words is the list of all valid english words
    @returns a float from 0 to 1 representing the percentage
    """

    all_english_words = get_text_data("dictionary.txt")

    total_num_words = len(string.split(" "))
    num_english_words = 0.0
    all_english_words = all_english_words.split("\n")
    all_english_words = set(all_english_words)

    for word in string.split(" "):
        if word in all_english_words:
            num_english_words += 1
    return num_english_words / total_num_words


def missing_letters(alphabet):
    """
    Given a list, return the missing letters of the alphabet

    @param alphabet is the list of letters you are comparing to the alphabet
    @returns a list of missing letters
    """

    res = []
    for letter in list(string.ascii_uppercase):
        if letter not in alphabet:
            res += letter
    return res


def index_of_spaces(text):
    """
    Given text, return all space indices

    @param text is the string to analyze
    @returns a list of integers representing the indices
    """

    res = []
    for i in range(0, len(text)):
        if text[i] == ' ':
            res.append(i)
    return res


def insert_spaces_back(text, indices):
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


def get_index_lists(key_length, text_length):
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


def decrypt_caesar(ciphertext, spaces):
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


def texts_by_period(ciphertext, key_length):
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


def chi_squared(text, standard, key_length):
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


def find_letter_by_chi_squared(word, standard, key_length):
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


def find_key_from_frequencies(ciphertext, standard, key_length):
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


def next_letter(letter):
    """
    Helper function to get the next letter
    after a letter.

    Example: next_letter('A') -> B,

    @param letter is the letter you are starting with
    @returns letter + 1 in the alphabet
    """

    res = ''

    if ord(letter) < 65:
        res = 'Z'
    elif ord(letter) >= 90:
        res = 'A'
    else:
        res = chr(ord(letter) + 1)

    return res


# # # # # # # # # # # # # # # # # # # # # # ACTUAL SCRIPT BELOW

file_data = get_text_data(sys.argv[1])
spaces = index_of_spaces(file_data)
without = file_data.replace(" ", "")

encrypted_distribution = get_frequency_dict(file_data)

enc = as_list(as_sorted_tuple_list(encrypted_distribution))

missing = missing_letters(as_list(encrypted_distribution))
encrypted_alphabet = enc + missing

standard_alphabet = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L'
                     'C', 'U', 'M', 'F', 'P', 'G', 'W', 'Y', 'B', 'V', 'K',
                     'X', 'J', 'Q', 'Z']

if sys.argv[2].upper() == 'SUBSTITUTION':
    first_time_running = sys.argv[3]  # To write to the alphabets.txt file

    most = most_used_n_letter_words(n_letter_words(file_data, 3))[0]
    standard_alphabet = adjust(most, standard_alphabet, encrypted_alphabet)

    if first_time_running == 'True':
        alphabet_file = open("alphabets.txt", 'w+')
        alphabet_file.write(list_to_string(encrypted_alphabet) + "\n")
        alphabet_file.write(list_to_string(standard_alphabet) + "\n")
        alphabet_file.close()

    alphabets = get_alphabet_mapping("alphabets.txt")

    replaced = replace_letters(string=file_data,
                               encrypted=alphabets[0],
                               standard=alphabets[1])
    threshold = english_words_percentage(replaced)
    print replaced
    print threshold
elif sys.argv[2].upper() == 'VIGENERE':
    standard_distribution = get_frequency_dict(get_text_data('dictionary.txt'))

    key_length = int(sys.argv[3])

    key = find_key_from_frequencies(ciphertext=without,
                                    standard=standard_distribution,
                                    key_length=key_length)

    decryption = insert_spaces_back(reverse_vigenere(without, key),
                                    spaces)

    print "WITH KEY: " + key
    print decryption
elif sys.argv[2].upper() == 'CAESAR':
    print decrypt_caesar(without, spaces)
else:
    print "PLEASE ENTER A VALID CIPHER TYPE"
