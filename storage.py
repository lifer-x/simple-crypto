import dotenv

class EnvKeyStorage:
    def __init__(self,env_path=".env"):
        self.env_path = env_path

    def get_crypted_key(self) -> str:
        return dotenv.dotenv_values(self.env_path).get("KEY", None)
    
    def save_crypted_key(self,crypted_key:str) -> None:
        dotenv.set_key(dotenv_path=self.env_path,key_to_set="KEY",value_to_set=crypted_key)
