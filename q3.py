import string
def wordCount(t):
    wordDictionary = {}
    lineNumber = 1
    with open(t, 'r') as file:
        for line in file:
            line = line.lower().strip() # lower the word instead of capitalize
            line = line.translate(str.maketrans('', '', string.punctuation)) # Get rid of any punctuation

            words = line.split()

            for i in words:
                if i not in wordDictionary:
                    wordDictionary[i] = []
                wordDictionary[i].append(lineNumber)
            lineNumber += 1
    return wordDictionary

print(wordCount('q3.txt'))