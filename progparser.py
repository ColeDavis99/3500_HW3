import re
from sys import stdin



def retRegex(word):
    keywordList = ["!", ":" ,":=", "+", "-", "*", "/", "OR", "AND", "~", "(", ")", "<", ">", "=", "#", ";", "FUNC", "IF", "ELSE", "WHILE", "PRINT", "RETURN", "END"]
    
    '''
    identPat =  ''
    intPat = ''
    decPat = ''
    strPat = ''
    '''

    if(word in keywordList):              
        print("ITS A KEYWORD!") 
    else:
        print("NOT A KEYWORD")
    
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
    (WHILE|ELSE|IF|PRINT)               {   pretty_print(tokens);   fout << "KEYWORD    LEXEME: " << yytext << endl;    tokens++;   }
    [+|-]?[0-9]+                        {   pretty_print(tokens);   fout << "INTCONST   LEXEME: " << yytext << endl;    tokens++;   }
    [+|-]?[0-9]+\.[0-9]+                {   pretty_print(tokens);   fout << "DECCONST   LEXEME: " << yytext << endl;    tokens++;   }
    \"[^ \n\t\r]*\"                     {   pretty_print(tokens);   fout << "STRCONST   LEXEME: " << yytext << endl;    tokens++;   }
    [A-Za-z][^ \n\t\r\"]*               {   pretty_print(tokens);   fout << "IDENT      LEXEME: " << yytext << endl;    tokens++;   }
'''