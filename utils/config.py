from configparser import RawConfigParser


# load_config loads data from our config files
def load_config(path: str, section, option):
    config = RawConfigParser()
    config.read(path)
    return config.get(section, option)
