import string
import secrets

CYRILLIC_ALPHABET = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"

class CryptoCore:
    def __init__(self, public_key:str):
        self.public_key = public_key
        self.alphabet = string.ascii_letters + string.digits + string.punctuation + CYRILLIC_ALPHABET

        self._char_to_idx = {char: idx for idx, char in enumerate(self.alphabet)}
        self._secret_key = None

    def _vigenere(self, text: str, key: str, mode: str = 'encrypt') -> str:
            res = ""
            sign = 1 if mode == 'encrypt' else -1
            
            for i, char in enumerate(text):
                if char in self.alphabet:
                    k_char = self._char_to_idx[key[i % len(key)]]
                    res += self.alphabet[
                           (self._char_to_idx[char] + sign * k_char) % len(self.alphabet)
                           ]
                else:
                    res += char
 
            return res

    def get_crypted_secret_key(self, length:int = 20) -> str:
        self._secret_key = ''.join(secrets.choice(self.alphabet) for _ in range(length))
        return self._vigenere(self._secret_key, self.public_key, 'encrypt')

    def load_crypted_secret_key(self, crypted_secret_key: str) -> None:
        self._secret_key = self._vigenere(crypted_secret_key, self.public_key, 'decrypt')

    def encrypt_message(self, message: str) -> str:
        current = self._vigenere(message, self._secret_key, 'encrypt')
        garbage = ''.join(secrets.choice(self.alphabet) for _ in range(97))
        current += garbage
        current = self._vigenere(current, self._secret_key, 'encrypt')
        return self._vigenere(current, self.public_key, 'encrypt')

    def decrypt_message(self, crypted_message: str) -> str:
        current = self._vigenere(crypted_message, self.public_key, 'decrypt')
        current = self._vigenere(current, self._secret_key, 'decrypt')
        
        if len(current) <= 97:
            return ""
            
        current = current[0:-97]
        return self._vigenere(current, self._secret_key, 'decrypt')
