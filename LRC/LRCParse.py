tokens = (
    'NON_TERM',
    'TERM',
    'LHS_START',
    'LHS_ALT',
    'EOL',
    'EOS'
)

t_NON_TERM = r'[A-Z\_]+'
t_TERM = r'[a-z\_]+'
t_LHS_START = r'\-\>'
t_LHS_ALT = r'\|'
t_EOL = r'\n'
t_EOS = r'\$'
t_ignore = r'[ ]'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
lex.lex()

prodRules = []
cancSet = []
workList = []
uniqTok = set([])

gotoSet = {}

#Find the indx of a prg indc
def PrgIdx(rule):
    i = 0
    while(i < len(rule[1]) and rule[1][i].type != 'PRG'):
        i += 1
    return i

#pretty print a rule
def PrintRule(rule):
    print(rule[0] + ' ->', end="")
    for i in rule[1] :
        print(' ' + i.value, end="")
    print()

#Get a list of indicies of productions for a provided non terminal
def GetProductions(nonTerm):
    ruleSet = []
    i = 0
    #Check all LHS and if there is a match add the indx
    while i < len(prodRules):
        if(prodRules[i][0] == nonTerm):
            ruleSet.append(i)
        i += 1
    return ruleSet

#Check if a set contains the rule
def Contains(iset, rule):
    #Loop over all items in the set
    for i in iset:
        #if they dont have the same LHS or the RHS are different sizes skip to next item
        if(i[0] != rule[0] or len(i[1]) != len(rule[1])):
            continue
        #Compare all items in the RHS
        x = 0
        while(x < len(rule[1])):
            if(i[1][x].value != rule[1][x].value):
                break
            x += 1

        if(x == len(rule[1])):
            return True

    return False

#Check if a set is unique
def UniqueSet(iset):
    setNum = -1
    for es in cancSet:
        setNum += 1
        if(len(es) != len(iset)):
            continue
        cnt = 0
        for i in iset:
            if(Contains(es, i)):
               cnt += 1
        if(cnt == len(iset)):
            return setNum

    return -1

#Compute the closure of a set
def Closure(iset):
    lastSize = -1
    retSet = iset[:]
    #Loop until no more changes
    while(lastSize != len(retSet)):
        #Loop over all items in the set to close
        for i in retSet:
            #Get all possible rules for the non terminal to the right of the prg indc
            if(PrgIdx(i) >= len(i[1]) - 1 ):
                continue
            for f in GetProductions(i[1][PrgIdx(i) + 1].value):
                #Create a fresh start for that rule and save it iff its unique
                fs = FreshStart(prodRules[f])
                if(not Contains(retSet, fs)):
                    retSet.append(fs)
        #Update the last size to check for changes
        lastSize = len(retSet)
    return retSet

def Goto(iset, sym):
    retSet = []

    for i in iset:
        if(PrgIdx(i) >= len(i[1]) - 1 ):
            continue
        if(i[1][PrgIdx(i) + 1].value == sym):
            advRule = (i[0], i[1][:])
            Adv(advRule)
            retSet.append(advRule)

    return Closure(retSet)

#Advance the progress indc for a provided rule
def Adv(rule):
    #Get indx of prg
    i = PrgIdx(rule)
    #Make sure it can be moved
    if(i == len(rule[1])):
        return
    #pop from cur indx and insert at i+1
    rule[1].insert(i+1,rule[1].pop(i))

#Return the fresh start for a prod rule
def FreshStart(prodRule):
    #Create a token for the indc
    indc = lex.LexToken()
    indc.type = 'PRG'
    indc.value = '.'
    indc.lineno = 0
    indc.lexpos = 0

    #copy the tuple
    fs = (prodRule[0], prodRule[1][:])
    #insert the prg and return
    fs[1].insert(0, indc)
    return fs

def AddState(newState):
    if(len(newState) == 0):
        return -1
    i = UniqueSet(newState)
    if(i == -1):
        cancSet.append(newState)
        workList.append(newState)
        return len(cancSet) - 1
    return i

lex.input(open('CFG.txt', 'r').read())
RHS = ''

while 1:
    #Read token or break
    tok = lex.token()
    if not tok: break

    if(tok.type != 'LHS_ALT'):
        RHS = tok
        lex.token()
        tok = lex.token()
    else:
        tok = lex.token()

    curRule = []

    while(tok.type != 'EOL'):
        tok.lineno = 0
        tok.lexpos = 0
        curRule.append(tok)
        uniqTok.add(tok.value)
        tok = lex.token()

        if(tok.value == '|'):
            prodRules.append((RHS.value, curRule))
            curRule = []
            tok = lex.token()


    prodRules.append((RHS.value, curRule))

print('Grammar Symbols')
print(uniqTok)

print('Production Rules')
for i in prodRules:
    PrintRule(i)

#Calculate sets
prevSize = -1
AddState(Closure([FreshStart(prodRules[0])]))
while(len(cancSet) != prevSize):
    while(len(workList) > 0):
        nextState = workList.pop(0)
        stateIndx = UniqueSet(nextState)
        gotoSet[stateIndx] = {}
        for x in uniqTok:
            sn = AddState(Goto(nextState, x))
            if sn != -1:
                gotoSet[stateIndx][x] = sn


    prevSize = len(cancSet)


print("Canonical Sets")



setNums = 0
for state in cancSet:
    print("State " + str(setNums))
    for i in state:
        PrintRule(i)

    setNums += 1


print("Goto")

for skey in gotoSet.keys():
    for gkey in gotoSet[skey].keys():
        print("Goto " + str(skey) + ", " + gkey + " : \t" + str(gotoSet[skey][gkey]))






