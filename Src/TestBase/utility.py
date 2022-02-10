import configparser

class Utility:

    @staticmethod
    def loadPropertiesFile(fileName):
        cfg = configparser.ConfigParser()
        cfg.read(fileName)
        # print(cfg.get("SystemProperties", "chromeDriverPath"))
        return cfg

if __name__=="__main__":
    #Below line(s) is used to test the static method(s)
    properties = Utility.loadPropertiesFile("properties.ini")
    import pdb
    pdb.set_trace()
    # print(properties.get("SystemProperties", "chromeDriverPath"))