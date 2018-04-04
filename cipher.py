
#
# Generic Cipher abstract class
#

from abc import ABC, ABCMeta, abstractmethod
from typing import List

class Cipher(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def encrypt(self, plaintext: str, key: List[str]) -> str: pass

    @abstractmethod
    def decrypt(self, ciphertext: str) -> str: pass

