from configparser import ConfigParser

def get_token(section:str=None,token_name:str='token'):
    config = ConfigParser()
    config.read('config.ini')
    return config[section][token_name]