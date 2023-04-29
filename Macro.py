class MDT():

    def __init__(self, index, card):
        self.index = index
        self.card = card

    def __repr__(self):
        return "" + str(self.index) + "\t" + self.card

class MNT():

    def __init__(self, index, card, mdtindex):
        self.index = index
        self.card = card
        self.mdtindex = mdtindex

    def __repr__(self):
        return "" + str(self.index) + "\t" + self.card + "\t" + str(self.mdtindex)

class ALA():

    def __init__(self, index_marker, args):
        self.index_marker = index_marker
        self.args = args

    def __repr__(self):
        return "" + str(self.index_marker) + "\t\t" + self.args

def remove_values_from_list(the_list, val):
    return [value for value in the_list if value != val]

import re

indexmnt = 0
MNT_list = []
ALA_list = []
indexala = 0
MDT_list = []
done = False
line_list = []

if __name__ == '__main__':
    f = open("Macro.txt", "rt")
    addr = 0
    index = 0
    for line in f:
      s = re.split(" |\t|\n", line)
      s = remove_values_from_list(s, "")
      line_list.append(s)
    args_list = []
    for i, line in enumerate(line_list):
      wordString = ""
      for word in line:
        if ("&" in word):
            if ("," not in word and (word not in args_list)):
                ALA_list.append(ALA(indexala, word))
                indexala += 1
                args_list.append(word)
        wordString += word + " "
        if (word == 'PROG'):
          done = True
          break
      if done == True:
        break
      if "MACRO" not in wordString:
        MDT_list.append(MDT(index, wordString))
        index = index + 1
      if "MACRO" in line_list[i - 1]:
        MNT_list.append(MNT(indexmnt, line_list[i][0], index - 1))
        indexmnt += 1
    print("MDT Table")
    print("index\tcard")
    print(*MDT_list, sep="\n")
    print()
    print("MNT Table")
    print("index\tcard\tmdtindx")
    print(*MNT_list, sep="\n")
    print()

Macro.txt:
MACRO
INCR4 &AR1,&AR2,&AR3
  A     1,&AR1
  A     2,&AR2
  A     3,&AR3
MEND
