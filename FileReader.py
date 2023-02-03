class FileReader:
    def __init__(self):
        self.__data = []
        self.__dataDict = {}

    def getFileContent(self, fileName):
        currFile = open(fileName, "r")
        self.__data = currFile.read().split('\n')

        for val in range(len(self.__data)):
            currData = self.__data[val]
            key, value = currData.split(":")
            self.__dataDict[key] = value

    def getData(self):
        return self.__data

    def getDataDict(self):
        return self.__dataDict


fr = FileReader()

fr.getFileContent("demoDict.txt")

print(fr.getDataDict())
