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
    #print("This is tokenList: " + str(tokenList))
    #print("Token is: " + tokenList[staticCtr(0)])    
    #print("StaticCtr(0): " + str(staticCtr(0)) + "\nlen(tokenList): " + str(len(tokenList)))
    print()
    print()

    if(staticCtr(0) >= len(tokenList)-1):
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
                token = getToken(tokenList, 0)
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
                print("Error parsing param sequence, expecting identifier debug1")

            token = getToken(tokenList, 1)

    else:
        print("Error parsing param sequence, expecting identifier debug2")

    if(beenLooping):
        print("We been loopin")
        getToken(tokenList, -1) #Back up the static var one so we dont mess up tokenList counter


#Parse Relation
def parseRelation(tokenList):
    print("In parseRelation()")
    token = getToken(tokenList, 1)    
    relationList = ["<", ">", "=", "#"]

    if(token not in relationList):
        print("Not a relation <, >, =, or #")
    
#Parse StatementSequence
def parseStatementSequence(tokenList):
    print("In parseStatementSequence()")
    parseStatement(tokenList)
    
    token = getToken(tokenList, 0)
    print("LIVE FROM NEW YORK: " + token)
    while(token == "!"):
        parseStatement(tokenList)

#Parse Factor
def parseFactor(tokenlist):
    print("In parseFactor()")    
    token = getToken(tokenList, 1)

    if(retRegex(token) == "int" or retRegex(token) == "dec" or retRegex(token) == "str" or retRegex(token) == "ident"):
        pass

    elif(token == "("):
        parseExpression(tokenList)
        token = getToken(tokenList, 1)
        if(token != ")"):
            print("Error parsing factor, expected ')'")

    elif(token == "~"):
        parseFactor(tokenList)
     

#Parse MulOperator
def parseMulOperator(tokenList):
    print("In parseMulOperator()")
    mulList = ["*", "/", "AND"]
    token = getToken(tokenList, 0)

    if(token not in mulList):
        print("Not a mulOperator *, /, AND")

#Parse Term
def parseTerm(tokenList):
    print("In parseTerm()")    
    parseFactor(tokenList)
    parseMulOperator(tokenList)
    
#Parse Add Operator
def parseAddOperator(tokenList):
    print("In parseAddOperator()")
    token = getToken(tokenList, 0)
    addList = ["+", "-", "OR", "&"]

    if(token not in addList):
        print("Not an add operator +, -, OR, &")

#Parse SimpleExpression
def parseSimpleExpression(tokenList):
    print("In parseSimpleExpression()")
    parseTerm(tokenList)
    parseAddOperator(tokenList) #May just be a simple contains or something
    parseTerm(tokenList)

#Parse retStatement
def parseRetStatement(tokenList):
    print("In parseRetStatement()")
    token = getToken(tokenList, 1)

    if(token == "RETURN"):
        token = getToken(tokenList, 1)
        if(retRegex(token) != "ident"):
            print("Error parsing retStatement. Expected identifier after return.")
    

#Parse expression
def parseExpression(tokenList):
    print("In parseExpression()")
    parseSimpleExpression(tokenList)
    
    #These two are optional, I think I can just leave them like this.
    parseRelation(tokenList)
    parseSimpleExpression(tokenList)

#Parse assignment
def parseAssignment(tokenList):
    token = getToken(tokenList, 0)
    if(retRegex(token) == "ident"):
        token = getToken(tokenList, 1)
        if(token == ":="):
            print("Going past :=")
            parseExpression(tokenList)    
        else:
            print("Error parsing assignment. := expected")
            return False    
    else:
        print("Error parsing assignment. Expected identifier")
        return False

    return True

#Parse print
def parsePring(tokenList):
    pass

#Parse if statement
def parseIfStatement(tokenList):
    pass

#Parse while statement
def parseWhileStatement(tokenList):
    pass


#Parse Statement
def parseStatement(tokenList):
    print("In parseStatement()")
    token = getToken(tokenList, 1)
    startTokenIdx = staticCtr(0)        #This is the index in tokenList that we'll look for one of the four statements (assignment, print, if, or while)
    statementParsedSuccesfully = False  #If one of the four are succesfully parsed, this should be set to true and will prevent displaying of statement parse error.
    

    #See if one of the 4 statements can be parsed. 
    if(parseAssignment(tokenList)):
        statementParsedSuccesfully = True
        token = getToken(tokenList, 0)

    
    if(statementParsedSuccesfully == False):
        getToken(tokenList, startTokenIdx - staticCtr(0)) #Reset tokenList idx for next parsing
        if(parsePrintStatement(tokenList)):
            statementParsedSuccesfully = True
            token = getToken(tokenList, 0)

    if(statementParsedSuccesfully == False):
        getToken(tokenList, startTokenIdx - staticCtr(0)) #Reset tokenList idx for next parsing
        if(parseIfStatement(tokenList)):
            statementParsedSuccesfully = True
            token = getToken(tokenList, 0)

    if(statementParsedSuccesfully == False):
        getToken(tokenList, startTokenIdx - staticCtr(0)) #Reset tokenList idx for next parsing
        if(parseWhileStatement(tokenList)):
            statementParsedSuccesfully = True
            token = getToken(tokenList, 0)


    if(statementParsedSuccesfully == False):
        print("Error parsing statement. Expected assignment, print, if, or while")
    else:
        print("Statement parsed succesfully (either an assignment, print, if, or while).")


    
    

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
    if("" in tokenList):
        tokenList.remove("")
    if('' in tokenList):
        tokenList.remove('')



##########################
#Start the actual parsing
##########################
parseFunctionSequence(tokenList)


