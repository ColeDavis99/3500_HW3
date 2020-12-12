import re
from sys import stdin



def retRegex(inp):
    keywordPat = '(!|:|:=|+|-|*|/|OR|AND|~|(|)|<|>|=|#|;|FUNC|IF|ELSE|PRINT|RETURN|END)'
    '''
    identPat =  ''
    intPat = ''
    decPat = ''
    strPat = ''
    '''

    if(re.match(keywordPat, inp)):
        print("ITS A KEYWORD!")
    else:
        print("NOT A KEYWORD")





#Read in input for this program
inputData = ""
for line in stdin:
    inputData += line
    
word=""
for char in inputData:
    if(char == "\n" or char == " "):
        print(word, end="")       
        #Do processing here and stuff
        
        #Clear word for next one to identify        
        word = ""

    else:
        word += char

'''
    (WHILE|ELSE|IF|PRINT)               {   pretty_print(tokens);   fout << "KEYWORD    LEXEME: " << yytext << endl;    tokens++;   }
    [+|-]?[0-9]+                        {   pretty_print(tokens);   fout << "INTCONST   LEXEME: " << yytext << endl;    tokens++;   }
    [+|-]?[0-9]+\.[0-9]+                {   pretty_print(tokens);   fout << "DECCONST   LEXEME: " << yytext << endl;    tokens++;   }
    \"[^ \n\t\r]*\"                     {   pretty_print(tokens);   fout << "STRCONST   LEXEME: " << yytext << endl;    tokens++;   }
    [A-Za-z][^ \n\t\r\"]*               {   pretty_print(tokens);   fout << "IDENT      LEXEME: " << yytext << endl;    tokens++;   }
'''