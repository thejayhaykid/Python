import sentenceClass

def makeASentence():
    aString = "The quick brown fox jumps over the lazy dog"
    aSentence = sentenceClass.Sentence(aString)
    print(aSentence.getSentence())
    print(aSentence.getWords())
    print(aSentence.getLength())
    print(aSentence.getNumWords())

makeASentence()
    
