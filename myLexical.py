import re

keyword = ['break','case','char','const','countinue','deafult','do','int','else','enum','extern','float','for','goto','if','long','register','return','short','signed','sizeof','static','switch','typedef','union','unsigned','void','volatile','while']
built_in_functions = ['clrscr()','printf','scanf','getch()','main()']
library = ['<stdio.h>','<conio.h>']
operators = ['+','-','*','/','%','==','!=','>','<','>=','<=','&&','||','!','&','|','^','~','>>','<<','=','+=','-=','*=']
specialsymbol = ['@','#','$','_','!','//']
separator = [',',':',';','\n','\t','{','}','(',')','[',']',' ']
formatspecifier = ['%d','%i','%f','%s']

file = open("lexical_file.txt")
contents = file.read()
count = 0
program = contents.split("\n")
for line in program:
    count = count + 1
    print("\nLine", count, "\n", line)
    tokens = line.split(' ')
    print("Tokens are ", tokens)
    print("Line", count, "properties: ")
    length = len(tokens)      # count the number of word in program
    for i in range(0,length):
        if tokens[i] in keyword:
           print("Keyword -->",tokens[i])
           continue
        if tokens[i] in operators:
            print("Operator --> ",tokens[i])
            continue
        if tokens[i] in specialsymbol:
            print("Special Operator -->",tokens[i])
            continue
        if tokens[i] in formatspecifier:
            print("Format Specifier -->",tokens[i])
            continue
        if tokens[i] in built_in_functions:
            print("Built_in Function -->",tokens[i])
            continue
        if tokens[i] in separator:
            print("Separator -->",tokens[i])
            continue
        if tokens[i] in library:
            print("library -->",tokens[i])
            continue
        if re.match(r'(#include*).*', tokens[i]):
            print ("Header File -->", tokens[i])
            continue
        if re.match(r'^[-+]?[0-9]+$',tokens[i]):
            print("Number --> ",tokens[i])
            continue
        if re.match(r"^[^\d\W]\w*\Z",tokens[i]):
            print("Identifier --> ",tokens[i])
  
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
