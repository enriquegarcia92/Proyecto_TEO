import ply.lex as lex

# List of token names.   This is always required
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'keyword',
    'identificador',
    'inicioBloque',
    'finBloque',
    'finInstruccion',
    'asignacion',
    'comentario',
    'comentario_bloque',
    'cadena',
    'coma',
    'hash_include',
    'preprocessor_directive',
    'int',
    'float',
    'greater_than',  # Nuevo token para '>'
    'single_quote',  # Nuevo token para comilla simple
    'dot',  # Nuevo token para punto
)

# Regular expression rules for simple tokens
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
t_hash_include = r'\#include'

def t_int(t):
    r'(int)'
    return t


def t_float(t):
    r'(float)'
    return t


# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


def t_keyword(t):
    r'(char|return|if|else|do|while|for|void)'
    return t


def t_identificador(t):
    r'([a-z]|[A-Z]|_)([a-z]|[A-Z]|\d|_)*'
    return t


def t_cadena(t):
    r'\"[^\"]*\"'
    return t


def t_comentario(t):
    r'\/\/.*'
    return t


def t_comentario_bloque(t):
    r'\/\*(.|\n)*\*\/'
    # return t


def t_preprocessor_directive(t):
    r'\#.*'
    return t


def t_greater_than(t):
    r'>'
    return t


def t_single_quote(t):
    r'\''
    return t


def t_dot(t):
    r'\.'
    return t


# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}, position {t.lexpos}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Agregamos el código C a la entrada del lexer
code = """
#include <stdio.h>

int suma(int a, int b) {
    return a + b;
}

void imprimir_mayor(int x, int y) {
    if (x > y) {
        printf("El número %d es mayor que %d\n", x, y);
    } else {
        printf("El número %d es menor o igual que %d\n", x, y);
    }
}

int main() {
    int numero_entero = 10;
    char caracter = 'A';
    float numero_flotante = 5.5;

    // Llamando a la función suma
    int resultado = suma(numero_entero, 20);
    printf("El resultado de la suma es: %d\n", resultado);

    // Llamando a la funcion imprimir_mayor
    imprimir_mayor(8, numero_entero);

    return 0;
}
"""

lexer.input(code)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)