''' Use this tool to encode or decode word using the Atbash code '''

normalAlphabet = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
reverseAlphabet = {1:'z',2:'y',3:'x',4:'w',5:'v',6:'u',7:'t',8:'s',9:'r',10:'q',11:'p',12:'o',13:'n',14:'m',15:'l',16:'k',17:'j',18:'i',19:'h',20:'g',21:'f',22:'e',23:'d',24:'c',25:'b',26:'a'}

menu = str(input("insert decode to decode a word or encode to encode: "))
if (menu =='encode'):
    word = str(input("insert word: "))
    listWord = list(word)
    for indexWord in range(0,len(listWord)):
        for indexAlphabet in normalAlphabet:
            if (listWord[indexWord] == normalAlphabet[indexAlphabet]):
                print("find letter: " + listWord[indexWord] + " in normal alphabet in position: " + str(indexAlphabet) + " encoded in: " + str(reverseAlphabet[indexAlphabet]))
                
if (menu == 'decode'):
    word = str(input("insert word: "))
    listWord = list(word)
    for indexWord in range(0,len(listWord)):
        for indexAlphabet in reverseAlphabet:
            if (listWord[indexWord] == reverseAlphabet[indexAlphabet]):
                print("find letter: " + listWord[indexWord] + " in reverse alphabet in position: " + str(indexAlphabet) + " decoded: " + str(normalAlphabet[indexAlphabet]))
    