mot = [['Mnemonic_Opcode','Binary_Opcode','Instruction_Length','Instruction_Format'],['L','4A','4','001'],['A','5A','4','001'],['ST','1E','3','100']]
pot = [['Pseudo_Opcode','Address of routine to process Pseudo Op ( Predefined )'],['START','P1START'],['USING','P1USING'],['END','P1END'],['DC','P1DC'],['DS','P1DS']]
machineOpInstructions=['L','A','ST']
pseudoOpInstructions=['START','END','USING','DC','DS']
symbol_table = [['Symbol','Address']]

print("MOT table :\n")
for row in mot:
    for column in row:
       print(column,end='\t\t')
    print("\n")  
print("_________________________________________________________________________________________________________________________________") 
print("\n\n POT Table :\n")
for row in pot:
    for column in row:
        print(column,end='\t\t')
    print("\n")
print("_________________________________________________________________________________________________________________________________")
print("\n")

f = open("SampleCodeForPass1.txt")
lines = f.read().splitlines()

labels,registers,machineOps,pseudoOps=[],[],[],[]
k=0
for line in lines:
    k+=1
    words=line.split(' ')
    if(words[0]!=''):
        if(words[1]=='DS'):
           symbol_table.append([words[0],program_counter])
        if(words[1]!='START' and words[1]!='DS'):
           word_sep_by_apostrophe=words[2].split('\'')
           symbol_table.append([words[0],program_counter])
           program_counter+=4
    if('START' in words):
        symbol_table.append([words[0],'0'])
        program_counter = int(words.pop()) 
    for word in words:
        word_sep_by_comma=word.split(',')
        if(word in machineOpInstructions):
            print("Machine Op Instruction " + word + " Found at line  : " + str(k))
            for row in mot:
                if(word in row):
                    program_counter+=int(row[2])
                    break
            machineOps.append(word) 
        if(word in pseudoOpInstructions):
            print("Pseudo Op Instruction " + word + " Found at line  : " + str(k))
            pseudoOps.append(word)
            if(word=='START'):
                pass
            elif(word=='END'):
                print("\n\nPass 1 Completed.............")
                print("Program Counter resetted to zero")
                program_counter=0
            else:     
                # program_counter+=1
                pass
        if(word.isalpha() and word not in machineOpInstructions and word not in pseudoOpInstructions):
            print("Label " + word + " found at line : " + str(k)) 
            labels.append(word)
        if(len(word_sep_by_comma) > 1):
          for w in word_sep_by_comma:
            if(w.isnumeric()):
                print("Register R" + w + " found at line : " + str(k))
                if("R"+w not in registers):
                  registers.append("R" + w)
            if(w.isalpha()): 
                print("Label " + w + " found at line : " + str(k))
    print("Program Counter : \t" + str(program_counter) + "\n")

print("_________________________________________________________________________________________________________________________________")
print("\nLabels : ",labels) 
print("\nRegisters : ",registers) 
print("\nMachine Ops : ",machineOps) 
print("\nPseudo Ops : ",pseudoOps)
print("_________________________________________________________________________________________________________________________________")
print("\nSymbol table :\n ")
for row in symbol_table:
    for c in row:
        print(c,end='\t\t')
    print("\n")

SampleCodeForPass1.txt:
JOHN START 0
 USING *,15
 L 1,FOUR
 A 1,FIVE
 ST 1,TEMP
FOUR DC F'4'
FIVE DC F'5'
TEMP DS 1F
 END

