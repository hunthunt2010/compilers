# Learning group activity for 31 Mar 2014

# See if the grammar in Figure 7.14 is unambiguous

# tokens:
tokens = (
    'id', 'assign',
    'if', 'lparen', 'rparen', 'else', 'fi',
    'while', 'do', 'od', 'semi', 'plus',
    'begin', 'end',
    'num'
)

# Error handling rules
def t_error(t):
    print("Illegal character :" + str(t.value))
    t.lexer.skip(1)

def p_error(p):
    if t is None:
        print("Syntax Error")
        return

    print("Syntax error at '%s'" % t.value)

def p_Start(p):
    'Start : Stmt'
    p[0] = p[1]

def p_Stmt(p):
    '''Stmt : id assign E
            | if lparen E rparen Stmt else Stmt fi
            | if lparen E rparen Stmt fi
            | while lparen E rparen do Stmt od
            | begin Stmts end'''

def p_Stmts(p):
    '''Stmts : Stmts semi Stmt
             | Stmt'''

def p_E(p):
    '''E : E plus T
         | T'''

def p_T(p):
    '''T : id
         | num'''

# import ply.lex as lex
# lex.lex()
import ply.yacc as yacc
parser = yacc.yacc()
 
