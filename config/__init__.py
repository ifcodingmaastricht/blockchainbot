import yaml

def load():
    return yaml.safe_load(open("./config.yml"))
