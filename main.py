
#
# Main script to actually run cipher decryption
#

from utils import *
from caesar import Cipher
from substitution import Substitution
from vigenere import Vigenere
from caesar import Caesar

args = get_args()
file_data = get_text_data(args['FILENAME'])
text = file_data

if args['CIPHER'] == 'SUBSTITUTION':
    substitution = Substitution()

    if args['SHOULD_ENCRYPT']:
        key = args['ENCRYPTION_KEY']
        encrypted = substitution.encrypt(text, key)
        print(encrypted)

    elif args['SHOULD_DECRYPT']:
        decrypted = substitution.decrypt(text)
        print(decrypted)

elif args['CIPHER'] == 'VIGENERE':
    vigenere = Vigenere()

    if args['SHOULD_ENCRYPT']:
        key = args['ENCRYPTION_KEY']
        encrypted = vigenere.encrypt(text, key)
        print(encrypted)

    elif args['SHOULD_DECRYPT']:
        decrypted = vigenere.decrypt(text)
        print(decrypted)

elif args['CIPHER'] == 'CAESAR':
    caesar = Caesar()

    if args['SHOULD_ENCRYPT']:
        key = args['ENCRYPTION_KEY']
        encrypted = caesar.encrypt(text, key)
        print(encrypted)

    elif args['SHOULD_DECRYPT']:
        decrypted = caesar.decrypt(text)
        print(decrypted)
else:
   print("PLEASE ENTER A VALID CIPHER TYPE")
