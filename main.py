import pandas as pd

# Global variables
fileName = "input.txt"
inputFile = open(file=fileName, mode="r", encoding="utf8")
inputContent = inputFile.read()
fileIndex = 0
EOF = "EOF"

# Character classes
LETTER = 0
DIGIT = 1
UNKNOWN = 99
lexeme = ""
lexLen = 0


def getChar():
    global inputContent
    global fileIndex
    if (fileIndex < len(inputContent)):
        nextChar = inputContent[fileIndex]
        fileIndex += 1
        return nextChar
    else:
        return EOF


def getNonBlank():
    char = getChar()
    while (char.isspace()):
        char = getChar()
    return char


def getCharClass(char):
    if char.isalpha():
        charClass = LETTER
    elif char.isdigit():
        charClass = DIGIT
    else:
        charClass = UNKNOWN
    return charClass


def lex(char):
    lexeme = ""
    charClass = getCharClass(char)
    global fileIndex
    words = []
    if (charClass == LETTER):
        lexeme += char
        nextChar = getChar()
        while(nextChar != EOF and nextChar != " " and (getCharClass(nextChar) == LETTER or getCharClass(nextChar) == DIGIT)):
            lexeme += nextChar
            nextChar = getChar()

        if nextChar != " " and nextChar != EOF:
            fileIndex -= 1

    elif (charClass == DIGIT):
        lexeme += char
        nextChar = getChar()
        while((nextChar != EOF) and (nextChar != " ") and (getCharClass(nextChar) == DIGIT)):
            lexeme += nextChar
            nextChar = getChar()
        if nextChar != " " and nextChar != EOF:
            fileIndex -= 1

    elif (charClass == UNKNOWN):
        lexeme += char
    words.append(lexeme)

    return lexeme


def main():
    word = []
    symbols = []
    symbolsList = ['!', '#', '$', '%', '&', '(',')','*','+',',',".","-","="]
    nextChar = getNonBlank()
    if (nextChar == EOF):
        print("File is empty")
        return

    while nextChar != EOF:
        nextToken = lex(nextChar)
        nextChar = getNonBlank()

        if(nextToken in symbolsList):
            symbols.append(nextToken)
        if(nextToken not in symbols):
            word.append(nextToken)

        data = {
            'کلمه ها':word,
            'نماد ها': symbols
        }
        df = pd.DataFrame.from_dict(data, orient='index')
        df = df.transpose()
        df.to_excel(r'./export_dataframe.xlsx', index=False)


main()
