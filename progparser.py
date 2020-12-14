# Cole Davis        
# CS3500 Homework #3 
# Professor Morales 
#####################


import re
from sys import stdin

#For progressing through tokenList
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

    if(retRegex(tokenList[i]) == "int" or retRegex(tokenList[i]) == "dec" or retRegex(tokenList[i]) == "str" or retRegex(tokenList[i]) == "ident"):
        i+=1
        return True
    elif(tokenList[i] == "("):
        i+=1
        Expression()
        if(tokenList[i] == ")"):
            i+=1
            return True
    elif(tokenList[i] == "~"):
        i+=1
        Factor()

def IfStatement():
    global i

    if(tokenList[i] == "IF"):
        i+=1
        Expression()
        if(tokenList[i] == ":"):
            i+=1
            StatementSequence()
            if(tokenList[i] == "ELSE"):
                i+=1
                StatementSequence()
            if(tokenList[i] == ";"):
                i+=1
                return True
            else:
                print("REJECTED, in IfStatement() expected ';' but got " + tokenList[i])
                return False
        else:
            print("REJECTED, in IfStatement() expected ';'")
            return False    

def WhileStatement():
    global i

    if(tokenList[i] == "WHILE"):
        i+=1
        Expression()
        if(tokenList[i] == ":"):
            i+=1
            StatementSequence()
            if(tokenList[i] == ";"):
                i+=1
                return True
            else:
                print("REJECTED, in WhileStatement() expected ';' but got " + tokenList[i])
                return False
        else:
            print("REJECTED, in WhileStatement() expected ':' but got " + tokenList[i])
            return False
    return False

def RetStatement():
    global i

   
    if(tokenList[i] == "RETURN"):
        i+=1
        if(retRegex(tokenList[i]) == "ident"):
            i+=1
            return True
        else:
            print("Rejected, in RetStatement() expected identifier")
            return False

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
    global i
    
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
    global i

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

    if(retRegex(tokenList[i]) == "ident"):
        i+=1

        if(tokenList[i] == ":="):
            i+=1
            Expression()
            return True
        else:
            return False
    else:
        return False

def ParamSequence():
    global i

    if(retRegex(tokenList[i]) == "ident"):
        i+=1
        while(tokenList[i] == ","):
            i+=1
            if(retRegex(tokenList[i]) == "ident"):
                i+=1
            else:
                print("REJECTED in ParamSequence, expected identifier, got " + tokenList[i])
                return False


def PrintStatement():
    global i


    if(tokenList[i] == "PRINT"):
        i+=1
        if(tokenList[i] == "("):
            i+=1
            Expression()
            if(tokenList[i] == ")"):
                i+=1
                return True
            else:
                print("REJECTED in PrintStatement(), expected ')'")
                return False
            
        else:
            print("REJECTED in PrintStatement(), expected '('")
            return False
    else:
        return False


def Statement():
    global i
    temp_i = i  #Store for backtracking
    
    if(Assignment()):
        return True
    else:
        i = temp_i

    if(PrintStatement()):
        return True
    else:
        i = temp_i

    if(IfStatement()):
        return True
    else:
        i = temp_i

    if(WhileStatement()):
        return True


    print("REJECTED in Statement(). Expected a statement of some sort assignment, print, if, or while")
    return False
    

def StatementSequence():
    global i

    Statement()

    while(tokenList[i] == "!"):
        i+=1        
        Statement()

def FunctionDeclaration():
    global i    
    if(tokenList[i] == "FUNC"):
        i+=1
        if(retRegex(tokenList[i]) == "ident"):
            i+=1
            if(tokenList[i] == "("):
                i+=1
                ParamSequence()
                if(tokenList[i] == ")"):
                    i+=1
                    StatementSequence()
                    RetStatement()
                    if(tokenList[i] == "END."):
                        i+=1
                        return True
                    else:
                        print("REJECTED, in FunctionalDeclaration() expected 'END.' but got " + tokenList[i])
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
    global i
    result = False

    result = FunctionDeclaration()


    while(i < len(tokenList) and result == True):
        result = FunctionDeclaration()

    return result



##########################
#Start the actual parsing
##########################
if(FunctionSequence()):
    print("Program accepted!")
else:
    print("Program not accepted")