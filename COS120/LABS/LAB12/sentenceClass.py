class Sentence:
    def __init__(self, aString):
        self.sentence = aString
        wordList = aString.split()
        self.listWords = wordList

    def getSentence(self):
        return self.sentence

    def getWords(self):
        return self.listWords

    def getLength(self):
        return len(self.sentence)

    def getNumWords(self):
        return len(self.listWords)
