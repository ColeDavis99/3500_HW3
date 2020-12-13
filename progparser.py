import re
from sys import stdin



def retRegex(word):
    keywordList = ["!", ":", ":=", "+", "-", "*", "/", "OR", "AND", "~", "(", ")", "<", ">", "=", "#", ";", "FUNC", "IF", "ELSE", "WHILE", "PRINT", "RETURN", "END"]    
    intPat = '^[+|-]?[0-9]+$'
    decPat = '^[+|-]?[0-9]+[.][0-9]+$'
    strPat = '^[\"][\S]*[\"]$'
    identPat = '^[a-zA-z][a-zA-z0-9]*$'


    #Keyword check
    if(word in keywordList):              
        return("key")    

    #Int check
    if(re.match(intPat, word)):
        return("int")

    #Decimal check
    if(re.match(decPat, word)):
        return("dec")

    #String check
    if(re.match(strPat, word)):
        return("str")

    #Identifier
    elif(re.match(identPat, word)):
        return("ident")

    else:
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
    if(char == "\n" or char == " "):
        #print(word, end=": ")       
        
        #Do processing here and stuff
        #retRegex(word)
        
        #Clear word for next one to identify        
        word = ""

    else:
        #Continue building the word, char by char
        word += char