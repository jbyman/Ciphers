
#
# Main script to actually run cipher decryption
#

from utils import *
from caesar import Cipher
from substitution import Substitution
from vigenere import Vigenere

args = get_args()
file_data = get_text_data(args['CIPHERTEXT_FILE'])

spaces = index_of_spaces(file_data)
without = file_data.replace(" ", "")

encrypted_distribution = get_frequency_dict(file_data)

enc = as_list(as_sorted_tuple_list(encrypted_distribution))

missing = missing_letters(as_list(encrypted_distribution))
encrypted_alphabet = enc + missing

if args['CIPHER'] == 'SUBSTITUTION':
    substitution = Substitution()

    if args['SHOULD_ENCRYPT']:
        key = sys.argv[3]
        encrypted = substitution.encrypt(plaintext, key)
        print(encrypted)

    elif args['SHOULD_DECRYPT']:
        decrypted = substitution.decrypt(ciphertext)
        print(decrypted)

elif args['CIPHER'] == 'VIGENERE':
    vigenere = Vigenere()

    if args['SHOULD_ENCRYPT']:
        key = sys.argv[3]
        encrypted = vigenere.encrypt(plaintext, key)
        print(encrypted)

    elif args['SHOULD_DECRYPT']:
        decrypted = vigenere.decrypt(ciphertext)
        print(decrypted)

elif args['CIPHER'] == 'CAESAR':
    caesar = Caesar()

    if args['SHOULD_ENCRYPT']:
        key = sys.argv[3]
        encrypted = caesar.encrypt(plaintext, key)
        print(encrypted)

    elif args['SHOULD_DECRYPT']:
        decrypted = caesar.decrypt(ciphertext)
        print(decrypted)
else:
   print("PLEASE ENTER A VALID CIPHER TYPE")
