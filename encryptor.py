from core import CryptoCore
from storage import EnvKeyStorage
from ui import CryptoInterface

PUBLIC_KEY = "'=9=pR}+78'KCuy+SBT#Q4,]!x46,6B*]f6,%`WYxE^@&8g!Fv"

def encrypt(message):
   
    crypted_key = storage.get_crypted_key()
    if not crypted_key:
        storage.save_crypted_key(core.get_crypted_secret_key())
    else:
        core.load_crypted_secret_key(crypted_key)
        
    return core.encrypt_message(message)



core = CryptoCore(PUBLIC_KEY)
storage = EnvKeyStorage()

win = CryptoInterface("Encrypt",encrypt)
