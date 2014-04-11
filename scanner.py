#!/usr/bin/env python

# const int a = 1;
# int x = 1<<a;
# int y, z = 3;
# 
# y = z - x;
# if ( y <= 0 ) {
#    z = (x+2) + z*z ;
# } else {
#    z = z / y;
# }
# 
# return z;

import ply.lex as lex
import ply.yacc as yacc

reserved = {'int' : 'int',
        'const' : 'const',
        }

tokens = [
        'semi', 
        'identifier',
    ] + list(reserved.values())

t_semi = r';'
t_ignore = " \t\n"

def t_identifier(t):
    r'[a-zA-Z_]+[a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved[ t.value ]
    return t

def t_error(t):
    print("Illegal character :" + str(t.value))
    t.lexer.skip(1)

def p_START(p):
    '''START : STMT'''
    #print("START" + p[0])
    return

def p_STMT(p):
    '''STMT : DECL semi'''
    #print("STMT:" + p[1] + p[2])

def p_DECL(p):
    '''DECL : TYPE VARIABLE'''
    #p[0] = p[1] + p[2]
    #print("p[1]: <%s>" % p[1])
    #print("p[2]: <%s>" % p[2])
    #print("DECL:" + p[0])

def p_VARIABLE(p):
    '''VARIABLE : identifier'''
    #p[0] = ["id", p[1]]

def p_TYPE(p):
    '''TYPE : MODIFIER int'''
    #p[0] = p[1] + p[2]
    #print("TYPE:" + p[0])

def p_TYPE_INT(p):
    '''TYPE : int'''
    #p[0] = p[1]
    print("TYPE: %s" % p)

def p_MODIFIER(p):
    'MODIFIER : const'
    p[0] = ('MODIFIER', p[1])
    #p[0] = p[1]
    #print("MOD:" + p[0])

def p_error(p):
    print("yacc error: %s" % p)

lex.lex()
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

    print("Result returned: " + str(parser.parse(s)))
