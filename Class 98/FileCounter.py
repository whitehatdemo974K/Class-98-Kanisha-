def countWordsFromFile():
    fileName=input("File Name: ")
    file=open(fileName,"r")
    wordCount=0
    for line in file:
        word=line.split()
        print(word)
        wordCount=wordCount+len(word)
    print("number of words in the file: ")
    print(wordCount)

countWordsFromFile()