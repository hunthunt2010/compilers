#   CFG Used
#   START -> STMTS
#   STMTS -> TYPE id sc
#          | TYPE id assign EXPR sc
#          | if lp EXPR rp lb STMTS rb
#          | if lp EXPR rp lb STMTS rb else lb STMTS rb
#          | return EXPR sc
#          | STMTS STMTS
#   TYPE -> int
#   EXPR -> EXPR OP EXPR
#          | id
#          | num
#          | lp EXPR rp
#   OP   -> << | >> | < | > | >= | <= | ==
#          | + | - | * | /

#TOKEN DEF
tokens = (
    'TYPE',
    'id',
    'if',
    'else',
    'return',
    'sc',
    'assign',
    'lp',
    'rp',
    'lb',
    'rb',
    'OP',
    'num'
)

def t_TYPE(t): r'int'; return t;
def t_if(t): r'if'; return t;
def t_else(t): r'else'; return t;
def t_return(t): r'return'; return t;

t_id = r'[a-zA-Z\_]+[a-zA-Z\_0-9]*'

t_sc = r'\;'

t_assign = r'\='

t_lp = r'\('
t_rp = r'\)'
t_lb = r'\{'
t_rb = r'\}'

t_OP = r'(\<\< | \>\> | \< | \> | \>\= | \<\= | \=\= | \+ | \- | \* | \\)'

t_num = r'\d+'

t_ignore_EOL = r'\n'
t_ignore = r' '

def t_error(t):
    print("Illegal character :" + str(t.value))
    t.lexer.skip(1)

#YACC DEF
def p_error(t):
    if t is None:
        print("Syntax Error")
        return

    print("Syntax error at '%s'" % t.value)


def p_START(t):
    '''
    START : STMTS
    '''
    t[0] = ('start', t[1])


def p_STMTS_VAR_DCL(t):
    '''
    STMTS : TYPE id sc
          | TYPE id assign EXPR sc
    '''
    if len(t) == 4 :
        t[0] = ('STMT_VAR_DCL', t[1], t[2])
    elif len(t) == 6 :
        t[0] = ('STMT_VAR_DCL', t[1], t[2], t[4])

def p_STMTS_ASSIGN(t):
    '''
    STMTS : id assign EXPR sc
    '''
    t[0] = ('STMT_ASSIGN', t[1], t[3])

def p_STMTS_IF(t):
    '''
    STMTS : if lp EXPR rp lb STMTS rb
    '''
    t[0] = ('STMT_IF', t[3], t[6])

def p_STMTS_IF_ELSE(t):
    '''
    STMTS : if lp EXPR rp lb STMTS rb else lb STMTS rb
    '''
    t[0] = ('STMT_IF_ELSE' , t[3], t[6], t[10])

def p_STMTS_RETURN(t):
    '''
    STMTS : return EXPR sc
    '''
    t[0] = ('STMT_RETURN', t[2])

def p_STMTS_STMTS(t):
    '''
    STMTS : STMTS STMTS
    '''
    t[0] = (t[1], t[2])

def p_EXPR_OP(t):
    '''
    EXPR : EXPR OP EXPR
    '''
    t[0] = ("EXPR_OP", t[1], t[2], t[3])

def p_EXPR_ID_NUM(t):
    '''
    EXPR : id
         | num
    '''
    t[0] = t[1]

def p_EXPR_PAREN(t):
    '''
    EXPR : lp EXPR rp
    '''
    t[0] = t[2]


#Import the lexer and initilize
import ply.lex as lex
lex.lex()
import ply.yacc as yacc
parser = yacc.yacc()

import types

s = open('Source.c', 'r').read()

def printTree(item, depth=0):

    for p in item:
        if type(p) is tuple:
            printTree(p, depth + 1)
        else:
            indent = '\t' * depth
            print(indent + p)


lex.input(s)
while True:
    tok = lex.token()
    if not tok: break
    print(tok)


print("Result Returned: " + str(parser.parse(s)))

printTree(parser.parse(s))

