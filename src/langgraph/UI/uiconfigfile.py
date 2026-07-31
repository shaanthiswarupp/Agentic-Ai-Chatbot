from configparser import ConfigParser

class config:
    def __init__(self, configfile = "src/langgraph/UI/uiconfigfile.ini"):
        self.config = ConfigParser()
        self.config.read(configfile)
        