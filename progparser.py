import re
from sys import stdin

#For marching through tokenList
global i
i=0
global tokenList
tokenList = list()


def retRegex(word):
    keywordList = ["!", ":", ":=", "+", "-", "*", "/", "OR", "AND", "~", "(", ")", "<", ">", "=", "#", ";", "FUNC", "IF", "ELSE", "WHILE", "PRINT", "RETURN", "END"]    
    intPat = '^[+|-]?[0-9]+$'
    decPat = '^[+|-]?[0-9]+[.][0-9]+$'
    strPat = '^[\"][\S]*[\"]$'
    identPat = '^[a-zA-z][a-zA-z0-9]*$'
    spaceList = [""] #Whitespace is ignored when concatenating "word" earlier in the program. It gets thrown to this function as an empty string.


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



#Read in input for this program
inputData = ""
for line in stdin:
    inputData += line


#Build tokenList array of all words in the program to parse
word=""

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



################################################################################################

def Factor():
    global i
    print("In Factor(): " + tokenList[i])

    if(retRegex(tokenList[i]) == "int" or retRegex(tokenList[i]) == "dec" or retRegex(tokenList[i]) == "str" or retRegex(tokenList[i]) == "ident"):
        i+=1
        return True
    elif(tokenList[i] == "("):
        i+=1
        Expression()
        if(tokenList[i] == ")"):
            return True

def MulOperator():
    if(tokenList[i] in ["*", "/", "AND"]):
        return True
    return False

def Term():
    global i
    Factor()
    while(MulOperator()):
        i+=1
        Factor()
    

def AddOperator():
    print("In AddOperator(): " + tokenList[i])
    if(tokenList[i] in ["+", "-", "OR", "&"]):
        return True
    return False


def SimpleExpression():
    global i    
    Term()
    while(AddOperator()):
        i+=1
        Term()        

def Relation():
    if(tokenList[i] in ["<", ">", "=", "#"]):
        return True
    return False

def Expression():
    global i
    SimpleExpression()
    if(Relation()):
        i+=1
        SimpleExpression()
        
    

def Assignment():
    global i

    print("In assignment: " + tokenList[i])
    if(retRegex(tokenList[i]) == "ident"):
        i+=1
        print("In assignment: " + tokenList[i])
        if(tokenList[i] == ":="):
            i+=1
            Expression()

def Statement():
    global i    
    Assignment()

def StatementSequence():
    global i    
    Statement()
    while(tokenList[i] == "!"):
        Statement()

def FunctionDeclaration():
    global i    
    if(tokenList[i] == "FUNC"):
        i+=1
        if(retRegex(tokenList[i]) == "ident"):
            i+=1
            if(tokenList[i] == "("):
                i+=1
                #ParamSequence()
                if(tokenList[i] == ")"):
                    i+=1
                    StatementSequence()
                    #RetStatement()
                    i+=1
                    if(tokenList[i] == "END."):
                        return True
                    else:
                        print("REJECTED, in FunctionalDeclaration() expected 'END.'")
                        return False
                else:
                    print("REJECTED, in FunctionalDeclaration() expected ')'")
                    return False
            else:
                print("REJECTED, in FunctionalDeclaration() expected '('")
                return False
        else:
            print("REJECTED, in FunctionalDeclaration() expected identifier")
            return False
    else:
        print("REJECTED, in FunctionalDeclaration() expected 'FUNC'")
        return False
                
                

def FunctionSequence():
    if(FunctionDeclaration()):
        return True


##########################
#Start the actual parsing
##########################
if(FunctionSequence()):
    print("Program accepted!")
else:
    print("Program not accepted")