from core import CryptoCore
from storage import EnvKeyStorage
from ui import CryptoInterface

PUBLIC_KEY = "'=9=pR}+78'KCuy+SBT#Q4,]!x46,6B*]f6,%`WYxE^@&8g!Fv"

def decrypt(message):

    core.load_crypted_secret_key( storage.get_crypted_key() )

    return core.decrypt_message(message)

core = CryptoCore(PUBLIC_KEY)
storage = EnvKeyStorage()

win = CryptoInterface("Decrypt",decrypt)
