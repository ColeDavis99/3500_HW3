import re
from sys import stdin



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



####################################
#Read in input for this program
####################################
inputData = ""
for line in stdin:
    inputData += line


######################################################
#Loop through each space-separated work from the input
######################################################
word=""
for char in inputData:
    if(char == "\n" or char == " " or char == "\t"):
        #print(word, end=": ")       
        
        #Do processing here and stuff
        retRegex(word)
        
        #Clear word for next one to identify        
        word = ""

    else:
        #Continue building the word, char by char
        word += char