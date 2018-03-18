
#
# Main script to actually run cipher decryption
#

from utils import *
from caesar import Cipher
from substitution import Substitution
from vigenere import Vigenere

args = get_args()
file_data = get_text_data(args['FILENAME'])

if args['CIPHER'] == 'SUBSTITUTION':
    substitution = Substitution()

    if args['SHOULD_ENCRYPT']:
        key = args['ENCRYPTION_KEY']
        encrypted = substitution.encrypt(plaintext, key)
        print(encrypted)

    elif args['SHOULD_DECRYPT']:
        decrypted = substitution.decrypt(ciphertext)
        print(decrypted)

elif args['CIPHER'] == 'VIGENERE':
    vigenere = Vigenere()

    if args['SHOULD_ENCRYPT']:
        key = args['ENCRYPTION_KEY']
        encrypted = vigenere.encrypt(plaintext, key)
        print(encrypted)

    elif args['SHOULD_DECRYPT']:
        decrypted = vigenere.decrypt(ciphertext)
        print(decrypted)

elif args['CIPHER'] == 'CAESAR':
    caesar = Caesar()

    if args['SHOULD_ENCRYPT']:
        key = args['ENCRYPTION_KEY']
        encrypted = caesar.encrypt(plaintext, key)
        print(encrypted)

    elif args['SHOULD_DECRYPT']:
        decrypted = caesar.decrypt(ciphertext)
        print(decrypted)
else:
   print("PLEASE ENTER A VALID CIPHER TYPE")
