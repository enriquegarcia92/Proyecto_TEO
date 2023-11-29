import ply.lex as lex

# Nombre de tokens
tokens = (
    'aumentarvar',
    'reducirvar',
    'libcall',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'while',
    'RPAREN',
    'keyword',
    'printf',
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
def t_aumentarvar(t):
    r'([a-z]|[A-Z]|_)([a-z]|[A-Z]|\d|_)*\+\+'
    return t


def t_reducirvar(t):
    r'([a-z]|[A-Z]|_)([a-z]|[A-Z]|\d|_)*\-\-'
    return t


def t_libcall(t):
    r'\<([a-zA-Z_][a-zA-Z0-9_]*)\>'
    t.value = t.value[1:-1]  # Extract the identifier part
    return t


def t_int(t):
    r'(int)'
    return t


def t_while(t):
    r'(while)'
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


def t_printf(t):
    r'(printf)'
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


# código de ejemplo a utilizar
# código de ejemplo a utilizar
code = """#include <stdio.h>
        int suma(int a, int b){
        return a+b;
        }

        void imprimir_mayor(int x, int y) {
        if (x > y) {
            printf("El número %d es mayor que %d\n", x, y);
        } else {
            printf("El número %d es menor o igual que %d\n", x, y);
        }
        }

        int main(){
        int numero_entero = 10;
        char caracter = 'A';
        float numero_flotante = 5.5;

         // Llamando a la función suma
        int resultado = suma(numero_entero,s);
        printf("El resultado de la suma es: %d\n", resultado);

        // Llamando a la funcion imprimir_mayor
        imprimir_mayor(8, numero_entero);

        //Bucle while
        int i = 0;
        while(i<5){
        printf("Iteración %d\n", i);
        i++;
        }
        return 0;
        }

        $"""

lexer = lex.lex()
# Give the lexer the input
lexer.input(code)


# Tokenize and print
while True:
    token = lexer.token()
    if not token:
        break  # No more tokens
    print(f'Token: {token.type}, Lexeme: {token.value}, {token.lexpos}')
