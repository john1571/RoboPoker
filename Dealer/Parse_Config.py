import os


config_file = os.getcwd() + "\\Dealer\\config.ini"

def parse(key):
    if not os.path.exists(config_file):
        return False
    with open(config_file, "r") as config:
        line = config.readline()
        while line:
            key_length = len(key)
            if len(line) < key_length:
                line = config.readline()
                continue
            if line[:key_length] == key:
                values = line.split("=")
                value = values[1]
                value = value.replace("\n", "")
                return value
            line = config.readline()
        return ""
