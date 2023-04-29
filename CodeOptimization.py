import re
import ast

def input_code():
    code = []
    n = int(input("\nEnter number of lines of code: "))
    for _ in range(n):
        code.append(input())
    return code

def const_prop(code):
    const = {}
    opt = []
    for line in code:
        l, r = map(lambda x: x.strip(), line.split("="))
        new_r = list(filter(None, re.split("([()[\]{}])|<?=>|[-+*/|%^]", r)))
        if(len(new_r) == 1):
            const[l] = r
        else:
            r = r.split(" ")
            opt.append([l, r])
        
        
    for line in opt:
        for k in const.keys():
            if(k in line[1]):
                line[1] = [const[k] if x == k else x for x in line[1]]
        
    for i, line in enumerate(opt):
        opt[i] = line[0] + " = " + " ".join(line[1])
    return opt

def dead_code(code):
    const = {}
    opt = []
    flag1 = 0
    flag2 = 0
    for line in code:
        if("{" in line):
            flag2 += 1
        elif("}" in line):
            flag2 -= 0
        elif(flag1 == 1 and flag2 > 0):
            opt.append(line)
        elif("if" in line):
            cond = re.findall("(?<=\().+?(?=\))", line)
            new_cond = [const[x.strip()] if (
                x.strip() in const.keys()) else x for x in cond[0].split(" ")]
            a, b = new_cond[0], new_cond[2]
            if(a == b):
                flag1 = 1
        else:
            opt.append(line)
            l, r = map(lambda x: x.strip(), line.split("="))
        const[l] = r[0]
    return opt


def display_code(opt):
    print("\nOptimized Code: ")
    for line in opt:
        print(line)

while True:
    print("\n***************************************")
    print("Choose Code Optimization Technique")
    print("1. Constant Propagation")
    print("2. Dead Code Elimination")
    ch = int(input("\nEnter choice: "))
    if(ch == 1):
        input_prog = input_code()
        output_prog = const_prop(input_prog)
        display_code(output_prog)
    elif(ch == 2):
        input_prog = input_code()
        output_prog = dead_code(input_prog)
        display_code(output_prog)
    else:
        print("Bye")
        break
