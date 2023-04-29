# Lexical Analyser
class Output:
    def __init__(self, lineNo, tokenName, tokenType):
        self.lineNo = lineNo
        self.tokenName = tokenName
        self.tokenType = tokenType


display = []
predirect = ["include", "define"]
header = ["<stdio.h>", "<conio.h>", "<malloc.h>",
          "<process.h>", "<string.h>", "<ctype.h>"]
keywords = ["double", "int", "struct", "break", "else", "long", "switch", "case", "do", "if", "static", "while", "enum", "auto", "register", "typedef",
            "char", "extern", "return", "union", "const", "float", "short", "unsigned", "continue", "for", "signed", "void", "default", "goto", "sizeof", "volatile"]

terminals = ['\t', '\n', ',', ';', '(', ')', '{', '}', '[', ']', '#', '<', '>']
operators = ["+", "-", "++", "--", "*", "/", "%", "<", ">", "=", '!']
separators = [";", ":", ","]

# Parse
input = open("input_program.txt", "r")
for lineNo, line in enumerate(input):
    line = line.split()
    for token in line:
        if token in terminals:
            tokenName = token
            tokenType = "Terminal"

        elif token in predirect:
            tokenName = token
            tokenType = "Predirect"

        elif token in header:
            tokenName = token
            tokenType = "Header"

        elif token in operators:
            tokenName = token
            tokenType = "Operator"

        elif token in keywords:
            tokenName = token
            tokenType = "Keyword"

        else:
            tokenName = token
            tokenType = "Indetifier"

        display.append(Output(lineNo, tokenName, tokenType))

# Display
print("{:^16}{:^16}{:^16}".format("Line No", "Token Name", "Token Type"))
print("----------------------------------------------")
for i in display:
    print("{:^16}{:^16}   {:16}".format(i.lineNo, i.tokenName, i.tokenType))
    
lexical_file.txt:
#include <stdio.h>
int main() {
int a , b , c ;
printf ( " Enter two integers :" ) ;
scanf ( " %d %d ", &a , &b ) ;
c = a + b ;
printf ( " %d + %d = %d " , a , b , c ) ;
return 0 ;
}
