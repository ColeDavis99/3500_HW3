import re
from sys import stdin



def retRegex(word):
    keywordList = ["!", ":" ,":=", "+", "-", "*", "/", "OR", "AND", "~", "(", ")", "<", ">", "=", "#", ";", "FUNC", "IF", "ELSE", "WHILE", "PRINT", "RETURN", "END"]    
    intPat = '^[+|-]?[0-9]+$'

    '''
    identPat =  ''
    decPat = ''
    strPat = ''
    '''

    #Keyword check
    if(word in keywordList):              
        print("Its a KEYWORD!") 
    else:
        print("Not a KEYWORD")
    

    #Int check
    if(re.match(intPat, word)):
        print("Its an INT")
    else:
        print("Not an int")    

    print(word)
    print()

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
        #print(word, end="")       
        #Do processing here and stuff
        retRegex(word)
        
        #Clear word for next one to identify        
        word = ""

    else:
        #Continue building the word, char by char
        word += char

'''
    [+|-]?[0-9]+                        {   pretty_print(tokens);   fout << "INTCONST   LEXEME: " << yytext << endl;    tokens++;   }
    [+|-]?[0-9]+\.[0-9]+                {   pretty_print(tokens);   fout << "DECCONST   LEXEME: " << yytext << endl;    tokens++;   }
    \"[^ \n\t\r]*\"                     {   pretty_print(tokens);   fout << "STRCONST   LEXEME: " << yytext << endl;    tokens++;   }
    [A-Za-z][^ \n\t\r\"]*               {   pretty_print(tokens);   fout << "IDENT      LEXEME: " << yytext << endl;    tokens++;   }
'''