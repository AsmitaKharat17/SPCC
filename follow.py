import sys
sys.setrecursionlimit(60)
def computeFirst(string):
    first_ = set()
    if string in nonTerminals:
        alternatives = productions_dict[string]
        for alternative in alternatives:
            first_2 = computeFirst(alternative)
            first_ = first_ |first_2
    elif string in terminals:
        first_ = {string}
    elif string=='' or string=='@':
        first_ = {'@'}
    else:
        first_2 = computeFirst(string[0])
        if '@' in first_2:
            i = 1
            while '@' in first_2:
                first_ = first_ | (first_2 - {'@'})
                if string[i:] in terminals:
                    first_ = first_ | {string[i:]}
                    break
                elif string[i:] == '':
                    first_ = first_ | {'@'}
                    break
                first_2 = computeFirst(string[i:])
                first_ = first_ | first_2 - {'@'}
                i += 1
        else:
            first_ = first_ | first_2
    return  first_
def computeFollow(nT):
    follow_ = set()
    prods = productions_dict.items()
    if nT==startingSymbol:
        follow_ = follow_ | {'$'}
    for nt,rhs in prods:
        for alt in rhs:
            for char in alt:
                if char==nT:
                    following_str = alt[alt.index(char) + 1:]
                    if following_str=='':
                        if nt==nT:
                            continue
                        else:
                            follow_ = follow_ | computeFollow(nt)
                    else:
                        follow_2 = computeFirst(following_str)
                        if '@' in follow_2:
                            follow_ = follow_ | follow_2-{'@'}
                            follow_ = follow_ | computeFollow(nt)
                        else:
                            follow_ = follow_ | follow_2
    return follow_
no_of_terminals=int(input("Enter no. of terminals: "))
terminals = []
print("Enter the terminals :")
for _ in range(no_of_terminals):
    terminals.append(input())
no_of_non_terminals=int(input("Enter no. of non terminals: "))
nonTerminals = []
print("Enter the non terminals :")
for _ in range(no_of_non_terminals):
    nonTerminals.append(input())
startingSymbol = input("Enter the starting symbol: ")
no_of_productions = int(input("Enter no of productions: "))
productions = []
print("Enter the productions:")
for _ in range(no_of_productions):
    productions.append(input())
productions_dict = {}
for nT in nonTerminals:
    productions_dict[nT] = []


for production in productions:
    nonterm_to_prod = production.split("->")
    alternatives = nonterm_to_prod[1].split("/")
    for alternative in alternatives:
        productions_dict[nonterm_to_prod[0]].append(alternative)
firstOf = {}
followOf = {}
for non_terminal in nonTerminals:
    firstOf[non_terminal] = set()
for non_terminal in nonTerminals:
    followOf[non_terminal] = set()
for non_terminal in nonTerminals:
    firstOf[non_terminal] = firstOf[non_terminal] | computeFirst(non_terminal)
followOf[startingSymbol] = followOf[startingSymbol] | {'$'}
for non_terminal in nonTerminals:
    followOf[non_terminal] = followOf[non_terminal] | computeFollow(non_terminal)
print("{: ^20}{: ^20}".format('Non Terminals','Follow'))
for non_terminal in nonTerminals:
    print("{: ^20}{: ^20}".format(non_terminal, str(followOf[non_terminal])))
