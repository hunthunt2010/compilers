# lga 7: eittreim


# the AST format is a list:
# ["node type", data, (child node 1, (child node 2 ( ... ) ) ) ]
# 
# where node type is the operation or identifying trait, like "plus" or "identifier"
# data is sometimes None, but if node type is "identifier", the data is the variable name
# child node(s) could be statements or a value for an id, etc. Data can also be a list, like a
# name and a type for an id

# reserved words
reserved = {
    'if': 'if',
    'else': 'else',
    'int': 'type_int',
    'return': 'return',
}


# tokens:
tokens = [
    # binary operators:
    'lshift', 'greater_than', 

    # assignment:
    'assignment',

    # punctuation
    'semi', 'lparen', 'rparen', 'lcurbrace', 'rcurbrace',

    # constant values
    'constant_int',

    # symbols 
   'identifier',
] + list(reserved.values())

t_lshift = r'<<'
t_greater_than = r'\>'
t_assignment = r'='
t_semi = r';'
t_lparen = r'\('
t_rparen = r'\)'
t_lcurbrace = r'\{'
t_rcurbrace = r'\}'
t_constant_int = r'0|([1-9]+[0-9]*)'

t_ignore = r' '

def t_identifier(t):
    r'[a-zA-Z_]+[a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'identifier')
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rules
def t_error(t):
    print("Illegal character :" + str(t.value))
    t.lexer.skip(1)


def p_START(p):
    'START : STATEMENTS'
    p[0] = p[1]

def p_STATEMENTS(p):
    '''STATEMENTS : STATEMENT semi STATEMENTS
                  | STATEMENT semi
                  | IF'''
    p[0] = p[1]

def p_STATEMENT(p):
    '''STATEMENT : EXPRESSION
                 | DECL
                 | ASSIGNMENT
                 | RETURN'''
    p[0] = p[1]

def p_RETURN(p):
    'RETURN : return EXPRESSION'
    p[0] = ["return", p[2]]

def p_DECL(p):
    'DECL : TYPE VARIABLE assignment EXPRESSION'
    p[0] = ["decl", [p[2], p[1]], p[4]]

def p_ASSIGNMENT(p):
    'ASSIGNMENT : VARIABLE assignment EXPRESSION'
    p[0] = ["assignment", p[1], p[3]]
    
def p_TYPE(p):
    'TYPE : type_int'
    p[0] = p[1]

def p_VARIABLE(p):
    'VARIABLE : identifier'
    p[0] = ["id", p[1]]

def p_EXPRESSION(p):
    '''EXPRESSION : CONSTANT
                  | VARIABLE
                  | OPERATION'''
    p[0] = p[1]

def p_OPERATION(p):
    'OPERATION : OPERATION_BINARY'
    p[0] = p[1]


def p_OPERATION_BINARY(p):
    '''OPERATION_BINARY : EXPRESSION lshift EXPRESSION
                        | EXPRESSION greater_than EXPRESSION'''
    if p[2] == '<<':
        p[0] = ["lshift", None, p[1], p[3]]
    elif p[2] == '>':
        p[0] = ["greater_than", None, p[1], p[3]]


def p_CONSTANT(p):
    'CONSTANT : constant_int'
    p[0] = ["constant", p[1]]


def p_BOOLEAN(p):
    'BOOLEAN : EXPRESSION'
    p[0] = p[1]


def p_CODEBLOCK(p):
    '''CODEBLOCK : lcurbrace STATEMENTS rcurbrace
                 | STATEMENT semi'''
    p[0] = p[2]

def p_IF(p):
    '''IF : if lparen BOOLEAN rparen CODEBLOCK
          | if lparen BOOLEAN rparen CODEBLOCK else CODEBLOCK'''
    p[0] = ["if", p[3], p[5], ["else", p[7]]]

def p_error(p):
    if p is None:
        print("Syntax Error")
        return

    print("Syntax error at '%s'" % p.value)



import ply.lex as lex
lexer = lex.lex()
import ply.yacc as yacc
parser = yacc.yacc()



while True:
    s = ""

    try:
        s = raw_input()
    except EOFError:
        break


    print 20*"-"
    print s 
    print 20*"-"

    lexer.input(s)

    for tok in lexer:
        print 4*" ", tok


    p = parser.parse(s)

    print "AST:"
    if p is not None:
        for t in range(len(p)):
            print t*" ", p[t]

    print "\n"

