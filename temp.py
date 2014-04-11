#!/usr/bin/env python2

import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'identifier', 'closebrace', 'closeparen', 'comma', 
    'const', 'constantinteger', 'divide', 'else', 'equals', 
    'if', 'leftshift', 'lessthanorequal', 'minus', 'multiply', 
    'openbrace', 'openparen', 'plus', 'return', 'semicolon', 
    'typeinteger'
    )

t_ignore = " \t\n"

t_identifier      = r'[a-zA-Z][a-zA-Z0-9]*'
t_comma           = r','
t_const           = r'const'
t_if              = r'if'
t_else            = r'else'
t_equals          = r'='
t_leftshift       = r'<<'
t_lessthanorequal = r'<='
t_plus            = r'\+'
t_minus           = r'-'
t_multiply        = r'\*'
t_divide          = r'/'

t_openbrace       = r'\{'
t_closebrace      = r'\}'
t_openparen       = r'\('
t_closeparen      = r'\)'
t_return          = r'return'
t_semicolon       = r';'
t_typeinteger     = r'int'

def t_error(t):
    print("error" + t)
    return

def t_constantinteger(t):
    r'[1-9][0-9]'
    t.value = int(t.value)
    return t

def p_S(p):
    '''S : STATEMENTS'''
    p[0] = p[1]

def p_STATEMENTS(p):
    '''STATEMENTS : STATEMENT STATEMENTS'''
    p[0] = p[1] + p[2]

def p_STATEMENT(p):
    '''STATEMENT : STATEMENT semicolon
                 | EXPRESSION
                 | IF
                 | IF ELSE
                 | RETURN'''

def p_EXPRESSION(p):
    '''EXPRESSION : DECL
                  | OPERATION
                  | CONSTANT
                  | VARIABLE'''
    p[0] = p[1]

def p_BINARY_EXPRESSION(p):
    '''EXPRESSION : EXPRESSION OPERATIONBINARY EXPRESSION'''
    p[0] = " ".join(map(str, p[1::]))

def p_OPERATION(p):
    '''OPERATION : OPERATIONBINARY'''
    p[0] = p[1]

def p_BINARY_OPERATION(p):
    '''OPERATIONBINARY : plus
                       | minus
                       | multiply
                       | divide
                       | leftshift
                       | lessthanorequalto'''
    p[0] = p[1]

def p_VARIABLES(p):
    '''VARIABLES : VARIABLE comma VARIABLES'''

def p_ONE_VARIABLES(p):
    '''VARIABLES : VARIABLE'''

def p_VARIABLE(p):
    '''VARIABLE: IDENTIFIER'''

def p_MODIFIERS(p):
    '''MODIFIERS : MODIFIER MODIFIERS'''

def p_MODIFIERS_TO_LAMBDA(p):
    '''MODIFIERS : lambda'''
    return

def p_DECL(p):
    '''DECL : MODIFIERS DECL'''

def p_DECL_ASSIGNMENT(p):
    '''DECL : TYPE VARIABLES equals EXPRESSION'''

def p_TYPE(p):
    '''TYPE : TYPEINTEGER'''

def p_MODIFIER(p):
    '''MODIFIER : CONST'''

def p_CONSTANT(p):
    '''CONSTANT : CONSTANTINTEGER'''

def p_CODEBLOCK(p):
    '''CODEBLOCK : OPENBRACE STATEMENTS CLOSEBRACE'''

def p_IF(p):
    '''IF : if openparen EXPRESSION closeparen CODEBLOCK else'''

def p_ELSE(p):
    '''ELSE : else CODEBLOCK'''

def p_ELSE_LAMBDA(p):
    '''ELSE : lambda'''

def p_RETURN(p):
    '''RETURN : return STATEMENT'''

def p_error(p):
    print("yacc error: %s" % p)

lex.lex()
parser = yacc.yacc()
