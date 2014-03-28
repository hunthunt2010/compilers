tokens = (
    'IDENTIFIER', 'CLOSECURLYBRACE', 'CLOSEPAREN', 'COMMA', 
    'CONST', 'CONSTANTINTEGER', 'DIVIDE', 'ELSE', 'EQUALS', 
    'IF', 'LEFTSHIFT', 'LESSTHANOREQUAL', 'MINUS', 'MULTIPLY', 
    'OPENCURLYBRACE', 'OPENPAREN', 'PLUS', 'RETURN', 'SEMICOLON', 
    'TYPEINTEGER'
    )

t_ignore = " \t\n"

t_IDENTIFIER = r'[a-zA-Z]+[a-zA-Z0-9]*'
t_CLOSECURLYBRACE = r'\}'
t_CLOSEPAREN  = r'\)'
t_COMMA = r','
t_CONST	= r'const'
t_CONSTANTINTEGER = r'[1-9][0-9]*'
t_DIVIDE = r'/'
t_ELSE	= r'else'
t_EQUALS = r'='
t_IF = r'if'
t_LEFTSHIFT = r'<<'
t_LESSTHANOREQUAL = r'<='
t_MINUS	= r'-'
t_MULTIPLY = r'\*'
t_OPENCURLYBRACE = r'\{'
t_OPENPAREN = r'\('
t_PLUS = r'\+'
t_RETURN = r'return'
t_SEMICOLON = r';'
t_TYPEINTEGER = r'int'
