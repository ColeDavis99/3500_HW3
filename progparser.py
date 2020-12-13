import re
from sys import stdin



#Static Variable in Python (for when getToken is called)
def staticCtr(inc_dec):
    staticCtr.counter = staticCtr.counter + inc_dec
    return(staticCtr.counter)

#Attribute must be initialized
staticCtr.counter = -1


#Get the next token to parse
def getToken(tokenList, inc_dec):
    print("This is tokenList: " + str(tokenList))
    print("StaticCtr(0): " + str(staticCtr(0)) + "\nlen(tokenList): " + str(len(tokenList)))
    print()
    print()

    if(staticCtr(0) >= len(tokenList)):
        print("Error: Unexpected end of line")
        return("Error: Unexpected end of line")
    else:
        return(tokenList[staticCtr(inc_dec)])


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
        #print("Whitespace, ignore me")
        return("Whitespace")

    #Keyword check
    if(word in keywordList):
        #print("key")            
        return("key")    

    #Int check
    if(re.match(intPat, word)):
        #print("int")
        return("int")

    #Decimal check
    if(re.match(decPat, word)):
        #print("dec")            
        return("dec")

    #String check
    if(re.match(strPat, word)):
        #print("str")
        return("str")

    #Identifier
    elif(re.match(identPat, word)):
        #print("ident")        
        return("ident")

    #Random Junk
    else:
        #print("False")
        return False





#Parse FunctionSequence (START TOKEN)
def parseFunctionSequence(tokenList):
    print("In parseFunctionSequence()")
    parseFunctionDeclaration(tokenList)

#Parse FunctionDeclaration
def parseFunctionDeclaration(tokenList):
    print("In parseFunctionDeclaration()")
    token = getToken(tokenList, 1)
    
    if(token == "FUNC"):
        token = getToken(tokenList, 1)
        if(retRegex(token) == "ident"):
            token = getToken(tokenList, 1)
            if(token == "("):
                parseParamSequence(tokenList)
                token = getToken(tokenList, 1)
                if(token == ")"):
                    parseStatementSequence(tokenList)
                else:
                    print("Error parsing function declaration, expecting \")\"")
            else:
                print("Error parsing function declaration, expecting \"(\"")
        else:
            print("Error parsing function declaration, expecting identifier")        
    else:
        print("Error parsing function declaration, expecting FUNC")

#Parse ParamSequence
def parseParamSequence(tokenList):
    print("In parseParamSequence()")
    beenLooping = False
    token = getToken(tokenList, 1)

    if(retRegex(token) == "ident"):
        token = getToken(tokenList, 1)
        while(token == ","):
            beenLooping = True
            token = getToken(tokenList, 1)
            if(retRegex(token) == "ident"):
                pass
            else:
                return("Error parsing param sequence, expecting identifier (debug:2)")

            token = getToken(tokenList, 1)

    else:
        return("Error parsing param sequence, expecting identifier (debug:1)")

    if(beenLooping):
        getToken(tokenList, -1) #Back up the static var one so we dont mess up tokenList counter
    

#Parse Relation
def parseRelation(tokenList):
    print("In parseRelation()")
    token = getToken(tokenList, 1)    
    relationList = ["<", ">", "=", "#"]    
    
    if(token in relationList):
        pass
    else:
        print("Error parsing relation: Expected <, >, =, or #")
    
#Parse StatementSequence
def parseStatementSequence(tokenList):
    print("In parseStatementSequence()")
    parseStatement(tokenList)

def parseStatement(tokenList):
    print("In parseStatement()")
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
    if(token == ""):
        tokenList.remove("")
    if(token == ''):
        tokenList.remove('')



##########################
#Start the actual parsing
##########################
parseFunctionSequence(tokenList)


