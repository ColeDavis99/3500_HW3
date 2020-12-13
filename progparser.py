import re
from sys import stdin



#Static Variable in Python (for when getToken is called)
def staticCtr():
    staticCtr.counter += 1
    return(staticCtr.counter)

#Attribute must be initialized
staticCtr.counter = -1



def retRegex(word):
    keywordList = ["!", ":", ":=", "+", "-", "*", "/", "OR", "AND", "~", "(", ")", "<", ">", "=", "#", ";", "FUNC", "IF", "ELSE", "WHILE", "PRINT", "RETURN", "END"]    
    intPat = '^[+|-]?[0-9]+$'
    decPat = '^[+|-]?[0-9]+[.][0-9]+$'
    strPat = '^[\"][\S]*[\"]$'
    identPat = '^[a-zA-z][a-zA-z0-9]*$'
    spaceList = [""] #Whitespace is ignored when concatenating "word" earlier in the program. It gets thrown to this function as an empty string.


    #print("Word:",end="")
    #print(word + ":")

    #Whitespace Check
    if(word in spaceList):
        print("Whitespace, ignore me")
        return("Whitespace")

    #Keyword check
    if(word in keywordList):
        print("key")            
        return("key")    

    #Int check
    if(re.match(intPat, word)):
        print("int")
        return("int")

    #Decimal check
    if(re.match(decPat, word)):
        print("dec")            
        return("dec")

    #String check
    if(re.match(strPat, word)):
        print("str")
        return("str")

    #Identifier
    elif(re.match(identPat, word)):
        print("ident")        
        return("ident")

    #Random Junk
    else:
        print("False")
        return False


#Parse Relation
def parseRelation(tokenList, token):
    relationList = ["<", ">", "=", "#"]    
    if(token in relationList):
        pass
    else:
        print("Error parsing relation: Expected <, >, =, or #")

#Parse FunctionSequence (START TOKEN)
def parseFunctionSequence(tokenList, token):
    print("This is tokenList: ")
    print(tokenList)
    print("This is token: " + token)

#Parse FunctionDeclaration
def parseFunctionDeclaration(tokenList, token):
    if(token == "FUNC"):
        pass        



####################################
#Read in input for this program
####################################
inputData = ""
for line in stdin:
    inputData += line



###########################################################
#Build tokenList array of all words in the program to parse
###########################################################
word=""
tokenList = list()

for char in inputData:
    if(char == "\n" or char == " " or char == "\t"):       
        tokenList.append(word)            
        word = ""
    else:
        #Continue building the word, char by char
        word += char

#Remove the whitespace from tokenlist
for token in tokenList:
    tokenList.remove("")
    tokenList.remove('')



##########################
#Start the actual parsing
##########################
parseFunctionSequence(tokenList, tokenList[staticCtr()])

