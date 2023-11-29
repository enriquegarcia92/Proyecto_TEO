import ply.lex as lex

# Nombre de tokens
tokens = (
    'libcall',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'keyword',
    'inicioBloque',
    'finBloque',
    'finInstruccion',
    'asignacion',
    'comentario',
    'comentario_bloque',
    'cadena',
    'coma',
    'int',
    'char',
    'float',
    'greater_than',
    'lesser_than',
    'single_quote',
    'dot',
    'hashtoken',
    'identificador',
    'if',
    'else',
    'else_if',
    'or',
    'and',
    'not',
    'eof'
)

# Tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_inicioBloque = r'\{'
t_finBloque = r'\}'
t_finInstruccion = r'\;'
t_asignacion = r'\='
t_coma = r'\,'
t_eof = r'\$'
t_hashtoken = r'\#'

# Reglas de tokens, expersiones regulares

def t_libcall(t):
    r'\<([a-zA-Z_][a-zA-Z0-9_]*)\>'
    t.value = t.value[1:-1]  # Extract the identifier part
    return t

def t_int(t):
    r'(int)'
    return t

def t_or(t):
    r'\|\|'
    return t

def t_and(t):
    r'(&&)'
    return t

def t_not(t):
    r'(!)'
    return t
def t_if(t):
    r'(if)'
    return t

def t_else(t):
    r'(else)'
    return t
def t_else_if(t):
    r'(else if)'
    return t

def t_char(t):
    r'(char)'
    return t

def t_float(t):
    r'(float)'
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_keyword(t):
    r'(char|return|do|while|for|void)'
    return t
def t_identificador(t):
    r'([a-z]|[A-Z]|_)([a-z]|[A-Z]|\d|_)*'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_cadena(t):
    r'\"[^\"]*\"'
    return t


def t_comentario(t):
    r'\/\/.*'
    return t


def t_comentario_bloque(t):
    r'\/\*(.|\n)*\*\/'
    # return t


def t_greater_than(t):
    r'>'
    return t


def t_lesser_than(t):
    r'<'
    return t


def t_single_quote(t):
    r'\''
    return t


def t_dot(t):
    r'\.'
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}, position {t.lexpos}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test input
code = """#include <stdio.h>
   
        int suma(int a, int b){
        return a+b;
        }
        void imprimir_mayor(int x, int y) {
        if (!x) {
        }
        }$"""

# Give the lexer the input
lexer.input(code)

# Tokenize and print
while True:
    token = lexer.token()
    if not token:
        break  # No more tokens
    print(f'Token: {token.type}, Lexeme: {token.value}, {token.lexpos}')
