import ply.lex as lex

# Nombre de tokens
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
    'greater_than',
    'single_quote',
    'dot',
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
t_hash_include = r'\#include'
t_eof = r'\$'


# Reglas de tokens, expersiones regulares
def t_int(t):
    r'(int)'
    return t


def t_float(t):
    r'(float)'
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


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


def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}, position {t.lexpos}")
    t.lexer.skip(1)


# código de ejemplo a utilizar
code = """#include <stdio.h>
    
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
        }$"""

S = 0
D = 1
X = 2
Y = 3
Z = 4
W = 5
U = 6
V = 7
B = 8
Q = 9
M = 10
C = 11
F = 12
CO = 13
I = 14
P = 15
IM = 16
R = 17
FIN = 18
tabla = [
    [S, 'preprocessor_directive', ['preprocessor_directive', D]],
    [D, 'int', ['int', 'identificador', 'LPAREN', 'int', 'identificador', 'coma', 'int', 'identificador', 'RPAREN',
                'inicioBloque', U, 'finBloque', X]],
    [U, 'keyword', ['keyword', 'identificador', 'PLUS', 'identificador', 'finInstruccion']],
    [X, 'keyword',
     ['keyword', 'identificador', 'LPAREN', 'int', 'identificador', 'coma', 'int', 'identificador', 'RPAREN',
      'inicioBloque', V, 'finBloque', V]],
    [V, 'keyword',
     ['keyword', 'LPAREN', 'identificador', 'greater_than', 'identificador', 'RPAREN', 'inicioBloque', W, 'finBloque',
      Z, 'finBloque', Q]],
    [W, 'identificador',
     ['identificador', 'LPAREN', 'cadena', 'coma', 'identificador', 'coma', 'identificador', 'RPAREN',
      'finInstruccion']],
    [Z, 'keyword', ['keyword', 'inicioBloque', B, 'finBloque']],
    [B, 'identificador',
     ['identificador', 'LPAREN', 'cadena', 'coma', 'identificador', 'coma', 'identificador', 'RPAREN',
      'finInstruccion']],
    [Q, 'int', ['int', 'identificador', 'LPAREN', 'RPAREN', 'inicioBloque', M, C, F, CO, I, P, CO, IM, R, FIN]],
    [M, 'int', ['int', 'identificador', 'asignacion', 'NUMBER', 'finInstruccion']],
    [C, 'keyword',
     ['keyword', 'identificador', 'asignacion', 'single_quote', 'identificador', 'single_quote', 'finInstruccion']],
    [F, 'float', ['float', 'identificador', 'asignacion', 'NUMBER', 'dot', 'NUMBER', 'finInstruccion']],
    [CO, 'comentario', ['comentario']],
    [I, 'int',
     ['int', 'identificador', 'asignacion', 'identificador', 'LPAREN', 'identificador', 'coma', 'NUMBER', 'RPAREN',
      'finInstruccion']],
    [P, 'identificador', ['identificador', 'LPAREN', 'cadena', 'coma', 'identificador', 'RPAREN', 'finInstruccion']],
    [IM, 'identificador', ['identificador', 'LPAREN', 'NUMBER', 'coma', 'identificador', 'RPAREN', 'finInstruccion']],
    [R, 'keyword', ['keyword', 'NUMBER', 'finInstruccion']],
    [FIN, 'finBloque', ['finBloque', 'eof']]
]

stack = ['eof', 0]

#Inicialiación de lexer
lexer = lex.lex()


def miParser():
    # f = open('fuente.c','r')
    # lexer.input(f.read())
    lexer.input(code)

    tok = lexer.token()
    x = stack[-1]  # primer elemento de der a izq
    while True:
        if x == tok.type and x == 'eof':
            print("Cadena reconocida exitosamente")
            return  # aceptar
        else:
            if x == tok.type and x != 'eof':
                stack.pop()
                x = stack[-1]
                tok = lexer.token()
            if x in tokens and x != tok.type:
                print("Error: se esperaba ", tok.type)
                return 0;
            if x not in tokens:  # es no terminal
                print("van entrar a la tabla:")
                print(x)
                print(tok.type)
                celda = buscar_en_tabla(x, tok.type)
                if celda is None:
                    print("Error: NO se esperaba", tok.type)
                    print("En posición:", tok.lexpos)
                    return 0;
                else:
                    stack.pop()
                    agregar_pila(celda)
                    print(stack)
                    print("------------")
                    x = stack[-1]

                    # if not tok:
            # break
        # print(tok)
        # print(tok.type, tok.value, tok.lineno, tok.lexpos)


def buscar_en_tabla(no_terminal, terminal):
    for i in range(len(tabla)):
        if (tabla[i][0] == no_terminal and tabla[i][1] == terminal):
            return tabla[i][2]  # retorno la celda


def agregar_pila(produccion):
    for elemento in reversed(produccion):
        if elemento != 'vacia':  # la vacía no la inserta
            stack.append(elemento)


miParser()
