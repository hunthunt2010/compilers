#!/usr/bin/env python2

# Problem grammar:
# Start -> Stmt $
# Stmt  -> id assign E
#        | if lparen E rParen Stmt else Stmt fi
#        | if lparen E rParen Stmt fi
#        | while lparen E rparen do Stmt od
#        | begin Stmts end
# Stmts -> Stmts semi Stmt
#        | Stmt
# E     -> E plus T
#        | T
# T     -> id
#        | num

import ply.lex as lex
import ply.yacc as yacc

tokens = (
        'ID',
        'NUM',
        'ASSIGN',
        'LPAREN',
        'RPAREN',
        'SEMI',
        'PLUS',
        'IF',
        'ELSE',
        'FI',
        'WHILE',
        'DO',
        'OD',
        'BEGIN',
        'END',
)

t_ID     = r'[a-zA-Z][a-zA-Z0-9]*'
t_ASSIGN = r'='
t_PLUS   = r'\+'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMI   = r';'
t_IF     = r'if'
t_ELSE   = r'else'
t_FI     = r'fi'
t_WHILE  = r'while'
t_DO     = r'do'
t_OD     = r'od'
t_BEGIN  = r'begin'
t_END    = r'end'

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print("Illegal Character : " + str(t.value))
    t.lexer.skip(1)

def p_error(p):
    if p is None:
        print("Syntax Error")
        return

def p_statements(p):
    '''statements : statements SEMI statement
                  | statement'''
    if len(p) == 4:
        p[0] = p[1] + p[3]
    else:
        p[0] = p[1]

def p_statement(p):
    '''statement : ID ASSIGN e
                 | IF LPAREN e RPAREN statement ELSE statement FI
                 | IF LPAREN e RPAREN statement FI
                 | WHILE LPAREN e RPAREN DO statement OD
                 | BEGIN statements END'''

def p_e(p):
    '''e : e PLUS t
         | t'''
    if len(p) == 4:
        p[0] = p[1] + p[3]
    else:
        p[0] = [1]

def p_t(p):
    '''t : ID
         | NUM'''
    p[0] = p[1]

lex.lex()
parser = yacc.yacc()

while True:
   try:
       s = raw_input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)
