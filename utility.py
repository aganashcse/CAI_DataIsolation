import configparser

class Utility:

    @staticmethod
    def loadJsonFile(fileName):
        cfg = configparser.ConfigParser()
        cfg.read(fileName)
        return cfg

if __name__=="__main__":
    #Below line(s) is used to test the static method(s)
    Utility.loadJsonFile("properties.ini")