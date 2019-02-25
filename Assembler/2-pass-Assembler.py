with open('program.txt') as f:
    lines = f.readlines()
# print(lines)
lines = [x.strip() for x in lines]
# print(lines)
lines = [x.split() for x in lines]
# print(lines)

symbol_t, literal_t, constants, lc, base_t, flag1, no_constants, program_table = [], [], [], 0, [], 0, 0, []
mnemonic = {'START': 0, 'USING': 0, 'DROP': 0, 'EQU': 0, 'L': 4, 'ST': 4, 'C': 4, 'A': 4, 'BNE': 4, 'LA': 4, 'SR': 2,'AR': 2, 'LR': 2, 'BR': 2, 'DS': 0, 'DC': 0, 'LTORG': 0, 'END': 0}
# print("Enumerate:")
for i, l in enumerate(lines):# for making code table
    # print(i,l)
    # print("l[0]=",l[0])
    if l[0] not in mnemonic:  # first word not mnemonic
        # print("Appending Mnemonic")
        program_table.append([l[0], l[1], ''.join(l[2:])])  # ( label, mnemonic, rest )
    elif l[0] != 'LTORG' and l[0] != 'END' and l[0] != 'START':
        # print("Appending LTORG")
        program_table.append([-1, l[0], ''.join(l[1:])])  # ( -1, mnemonic, rest )
    else:
        # print("Appending else block")
        program_table.append([-1, ''.join(l[0:]), -1])  # ( -1, mnemonic, -1 )

# print("Program Table=",program_table)

intermediate_t = [i[:] for i in program_table]
# print("Intermediate Table=",intermediate_t)
for i, val in enumerate(intermediate_t):
    if val[2] != -1:   #if there are operands
        intermediate_t[i][2] = val[2].split(',')  #ith line operand

# print("Intermediate after splitting:",intermediate_t)

print("\n\nConstants=",constants)

for n, p in enumerate(program_table):
    intermediate_t[n].append(lc)  #Append Lc to each and every line of the code
    if p[0] != -1 and p[0] != '':  # if label found
        if p[1] == 'EQU' and '*' not in p[2]:
            symbol_t.append([p[0], p[2], 'A'])  #Allocation type symbol
        else:
            symbol_t.append([p[0], lc, 'R'])   #Relocation type symbol
            lc += mnemonic[p[1]]
            print("\n\nlc=",lc)
    else:  # if not label found
        lc += mnemonic[p[1]]
        print("Lc=",lc)
    if p[1] == 'DS':  # lc does not increments for DS and DC
        if 'F' in p[2]:  #i.e eg :  DS 2000F  Full word
            lc += (4 * int(p[2][:p[2].index('F')]))  #  eg 10F = 4 * 10+LC
            print("lc=", lc)
        else:
            lc += (2 * int(p[2][:p[2].index('A')]))    # Half word
            print("lc=", lc)
    elif p[1] == 'DC':
        if 'F' in p[2]:
            lc += (lc % 4) + 4
            print("lc=", lc)
        else:
            lc += (lc % 2) + 2
            print("lc=", lc)
    elif p[1] == 'LTORG':
        lc += lc % 8  # Lc Should be a multiple of 8
        print("lc=",lc)
        print("\n\nConstant inside the program:",constants)
        for _ in constants:
            literal_t.append([_, lc])  # Assigning values in literal table
            lc += 4 if 'F' in _ else 4  #incrementing the location counter according to the length of literal instruction
            print("lc=", lc)
    elif 'USING' in p[1]:
        print("Base table=",base_t)
        base_t.append(p[2].split(','))
        if base_t[-1][0] == '*':  #if it is USING *,15
            base_t[-1][0] = lc    #Store the value of location counter in the base register
        base_t[-1].append(lc)
        print("After appending lc to base=",base_t)
    if '=' in str(p[2]):  # list all constants
        constants.append(p[2][p[2].index('='):])  #storing the value of constants in constant ka list

print("\n\nConstants after the program:",constants)
print("\n\nBase table after the program:",base_t)
print("\n\nSymbol table=",symbol_t)
for i in range(len(base_t)):
    if base_t[i][0] in [x[0] for x in symbol_t]:  #if there was a forward reference symbol in base table
        base_t[i][0] = symbol_t[[x[0] for x in symbol_t].index(base_t[i][0])][1]   #Assigning the value to symbol in the base register table
    if base_t[i][1] in [x[0] for x in symbol_t]:  #if there was a forward reference symbol for second element in base register
        base_t[i][1] = symbol_t[[x[0] for x in symbol_t].index(base_t[i][1])][1]   #Assigning the value to symbol in the base register table

for n1, val in enumerate(intermediate_t):  # update intermediate_t
    if val[2] != -1:  #if there is an operand
        for n2, j in enumerate(val[2]):
            if j in [x[0] for x in symbol_t]: #if any of the operand is referenced forward in symbol table
                intermediate_t[n1][2][n2] = str([x[0] for x in symbol_t].index(j)) + ' ST'  #Assigning the values of symbol to the operands
            elif j in [x[0] for x in literal_t]:  #if any of the operand is referenced forward in literal table
                intermediate_t[n1][2][n2] = str([x[0] for x in literal_t].index(j)) + ' LT'
            elif '(' in j and j[: j.index('(')]: #if there is '(' in the operands
                if j[: j.index('(')] in [x[0] for x in symbol_t]:  #if there a symbol before '(' eg: DATABASE,DATA1(INDEX)
                    intermediate_t[n1][2][n2] = str(
                        [x[0] for x in symbol_t].index(j[: j.index('(')])) + ' ST'  # for st with index Assigning the values
                else:
                    intermediate_t[n1][2][n2] = str(
                        [x[0] for x in literal_t].index(j[: j.index('(')])) + ' I'  # for lit_t with index Assigning the values from the literal table

print('\nSymbol Table\n', symbol_t)
print('\nLiteral Table\n', literal_t)
print('\nBase Table\n', base_t)
print('\nIntermediate Table')
for x in intermediate_t:
    print(x)
mc_table = [x[1:4] for x in intermediate_t] #filling the machine code table

for x in mc_table:
    if x[0] in ['START', 'USING', 'LTORG', 'END', 'EQU']:
        mc_table.pop(mc_table.index(x))   #if it is any assembly Directive removing that assembly directive

for x in mc_table:
    if x[0] == 'USING':
        mc_table.pop(mc_table.index(x)) #if still USING is left in mc_table then too remove it

for n1, x1 in enumerate(mc_table):
    flag, index = 0, 0
    for n2, x2 in enumerate(x1[1]):
        if not x2.isdigit():  #if the mnemonic is not digit
            flag = 1
    if flag != 1:   
        pass                 #if the mnemonic is digit leave it as it is
    else:
        flag1 = 0
        if len(base_t) > 1:
            if x1[2] > base_t[1][2]:  # switch using in base_t
                base_t.pop(0)
        for n2, x2 in enumerate(x1[1]):
            if not x2.isdigit():
                if 'ST' in x2:
                    mc_table[n1][1][n2] = symbol_t[int(x2[0])][1]
                    if intermediate_t[[x[0] for x in intermediate_t].index(symbol_t[int(x2[0])][0])][1] == 'EQU':
                        pass
                    else:
                        flag1 = 1
                elif 'LT' in x2:
                    mc_table[n1][1][n2] = literal_t[int(x2[0])][1]
                    flag1 = 1
                elif 'I' in x2:
                    temp = program_table[[x[0] for x in program_table].index(x1[0])][2]
                    b = 0
                    for b in literal_t:
                        if b[0] in ''.join(temp):
                            break
                    temp1 = ''.join(temp)
                    index = temp1[(x2.index['('] + 1): (x2.index['('])]
                    cons = b[0]
                else:
                    pass
            else:
                pass
        if flag1 != 1:  # both digit/equ
            pass
        else:
            if len(mc_table[n1][1]) > 1:
                mc_table[n1][1] = str(mc_table[n1][1][0]) + str(', ') + str(
                    int(mc_table[n1][1][1]) - int(base_t[0][0])) + str(' (') + str(index) + str(', ') + str(
                    base_t[0][1]) + str(' )')
print('\nMachine code table')
for _ in mc_table:
    print(_)
