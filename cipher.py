
#
# Generic Cipher abstract class
#

from abc import ABC, ABCMeta, abstractmethod
from utils import *

class Cipher(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def encrypt(self, plaintext, key): pass

    @abstractmethod
    def decrypt(self, ciphertext): pass

