#Basic Grammar for the demo language
#START ->   S $
#SEN ->     PVQ ADJECTIVE NOUN
#   |       PVQ NOUN
#PVQ ->     PRONOUN VERB QUANTITY

#List Of possible tokens
tokens = (
    'PRONOUN',
    'VERB',
    'QUANTITY',
    'ADJECTIVE',
    'NOUN',
)

#RegEx for the tokens
t_PRONOUN       = r'(I|we|she|he)'
t_VERB          = r'(ate|made|sold|bought|threw\ away)'
t_ADJECTIVE     = r'(candy|chocolate|(Rice\ Krispie))'
t_NOUN          = r'(bars?)'
t_ignore = r'[ ]'
#Tokens can also be defined as a function
def t_QUANTITY(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print("Illegal character :" + str(t.value))
    t.lexer.skip(1)

#YACC Rules
#Error Rule
def p_error(t):
    if t is None:
        print("Syntax Error")
        return

    print("Syntax error at '%s'" % t.value)
# GRAMMAR RULES FOR THE PARSER
#Start Rule
def p_START(t):
    'START : SEN'
    print("Start:" + t[1])
    t[0] = "OK"

#Rule with alternate productions
def p_SEN(t):
    '''SEN : PVQ ADJECTIVE NOUN
           | PVQ NOUN'''
    if len(t) == 4:
        t[0] = t[1] + t[2] + t[3]
    else:
        t[0] = t[1] + t[2]
    print("SEN:" + t[0])

def p_PVQ(t):
    'PVQ : PRONOUN VERB QUANTITY'
    t[0] = t[1] + t[2] + str(t[3])
    print("PVQ:" + t[0])

#Import the lexer and initilize
import ply.lex as lex
lex.lex()
import ply.yacc as yacc
parser = yacc.yacc()

while True:
    try:
        s = input('Validate String > ')
    except EOFError:
        break
    if s == 'quit':
        break
    lex.input(s)
    while True:
        tok = lex.token()
        if not tok: break
        print(tok)

    print("Result Returned: " + str(parser.parse(s)))