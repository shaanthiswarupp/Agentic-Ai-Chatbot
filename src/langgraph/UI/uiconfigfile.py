from configparser import ConfigParser

class config:

    def __init__(self, configfile = "./src/langgraph/UI/uiconfigfile.ini"):

        self.config = ConfigParser()
        self.config.read(configfile)



    def get_page_title(self):
        return self.config.get("DEFAULT", "PAGE_TITLE")

    def get_llms_options(self):
        return self.config.get("DEFAULT", "LLMS_OPTIONS").split(", ")

    def get_groq_models_options(self):
        return self.config.get("DEFAULT", "GROQ_MODELS_OPTIONS").split(", ")

    def get_usecases_options(self):
        return self.config.get("DEFAULT", "USECASES_OPTIONS").split(", ")