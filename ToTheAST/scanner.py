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

import node

reserved = {'int' : 'int',
        'const' : 'const',
        'if' : 'if',
        'else' : 'else',
        'return' : 'return',
        }

tokens = [
        'assign',
        'semi', 
        'comma',
        'lp', 'rp',
        'lb', 'rb',
        'leftshift',
        'plus',
        'minus',
        'multiply',
        'lessequal',
        'divide',
        'int_value',
        'identifier',
    ] + list(reserved.values())

t_assign = r'='
t_comma = r','
t_lp = r'\('
t_rp = r'\)'
t_lb = r'{'
t_rb = r'}'
t_leftshift = r'<<'
t_lessequal = r'<='
t_plus = r'\+'
t_minus = r'-'
t_multiply = r'\*'
t_divide = r'/'
t_semi = r';'
t_ignore = " \t\n"

def t_identifier(t):
    r'[a-zA-Z_]+[a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved[ t.value ]
    return t

def t_int_value(t):
    r'[0-9][0-9]*'
    return int(t.value)

def t_error(t):
    print("Illegal character :" + str(t.value))
    t.lexer.skip(1)

def p_START(p):
    '''START : STMTS'''

def p_STMTS(p):
    'STMTS : STMT STMTS'
    p[0] = ('STATEMENT', p[1])   #This could be a problem

def p_EMPTY_STMTS(p):
    'STMTS :'

def p_STMT_DECL(p):
    '''STMT : DECL semi'''

def p_STMT_EXPR(p):
    'STMT : EXPR semi'

def p_STMT_RETURN(p):
    'STMT : RETURN semi'

def p_STMT_ASSIGN(p):
    'STMT : identifier assign EXPR'

def p_IF_STMT(p):
    'STMT : if lp EXPR rp CODEBLOCK'

def p_IF_ELSE_STMT(p):
    'STMT : if lp EXPR rp CODEBLOCK else CODEBLOCK'

def p_DECL(p):
    '''DECL : TYPE VARIABLE MULTI'''

def p_DECL_ASSIGN(p):
    '''DECL : TYPE VARIABLE assign EXPR MULTI'''
    
def p_MULTI(p):
    '''MULTI : comma VARIABLE'''

def p_MULTI_ASSIGN(p):
    '''MULTI : comma VARIABLE assign EXPR'''

def p_MULTI_LAMBDA(p):
    '''MULTI : '''

def p_VARIABLE(p):
    '''VARIABLE : identifier'''
    p[0] = ('VARIABLE', p[1])

def p_EXPR_ORDER(p):
    'EXPR : lp EXPR rp'

def p_EXPR_BINOP(p):
    'EXPR : EXPR BINARYOPERATOR EXPR'

def p_EXPR_VALUE(p):
    'EXPR : VALUE'

def p_BINARYOPERATOR(p):
    '''BINARYOPERATOR : leftshift
                      | plus
                      | minus
                      | multiply
                      | divide
                      | lessequal'''
    p[0] = ('BINARYOPERATOR', p[1])

def p_RETURN(p):
    'RETURN : return'

def p_RETURN_EXPR(p):
    'RETURN : EXPR'

def p_CODEBLOCK(p):
    'CODEBLOCK : lb STMTS rb'

def p_VALUE(p):
    '''VALUE : int_value
             | identifier'''

def p_TYPE(p):
    '''TYPE : MODIFIER TYPE'''
    p[0] = ('TYPE', "%s %s" % (p[1], p[2]))

def p_TYPE_INT(p):
    '''TYPE : int'''
    p[0] = ('TYPE', p[1])
                          
def p_MODIFIER(p):
    'MODIFIER : const'
    p[0] = ('MODIFIER', p[1])

def p_error(p):
    print("yacc error: %s" % p)

lex.lex()
parser = yacc.yacc()

while True:
    try:
        s = input()
    except EOFError:
        break
    #if s == 'quit':
    #    break
    re.sub(r'//.*$', '', s)
    lex.input(s)
    while True:
        tok = lex.token()
        if not tok: break
        print(tok)

    print("Result returned: " + str(parser.parse(s)))
