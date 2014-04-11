import sys
import node as Node

reservedWords = {
    "if" : "IF",
    "else" : "ELSE",
    "const" : "CONST",
    "int" : "INT",
    "return" : "RETURN"
}

tokens = [
    "ID"

] + list(reservedWords.values())

def t_ID(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = reservedWords.get(t.value, "ID")    # Check for reserved words
    return t



import ply.lex as lex
lex.lex()
import ply.yacc as yacc
parser = yacc.yacc()

if sys.argv[1] is None: sys.exit(1)
fileName = sys.argv[1]

fileData = open(fileName, 'r').read()

rootNode = parser.parse(fileData)

outPutData = open("output.lis" , "w")
outPutData.write(rootNode.getNames())
outPutData.write(rootNode.getChildren())
