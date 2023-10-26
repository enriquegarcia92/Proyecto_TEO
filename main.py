import ply.yacc as yacc
import ply.lex as lex

# Definición de tokens (lexer) - Aquí definirías tus tokens en C
tokens = (
    'ID', 'INT', 'FLOAT', 'CHAR', 'IF', 'ELSE', 'INCLUDE', 'RETURN',
    'VOID', 'MAIN', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMI',
    'COMMA', 'ASSIGN', 'EQ', 'NEQ', 'LT', 'LTE', 'GT', 'GTE', 'PLUS',
    'MINUS', 'TIMES', 'DIVIDE', 'MOD', 'LBRACKET', 'RBRACKET', 'WHILE', 'FOR', 'INCLUDE_DIRECTIVE',
)

# Reglas para tokens simples
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_INT = r'\d+'
t_FLOAT = r'\d+\.\d+'
t_CHAR = r'\'[a-zA-Z]\''
t_RETURN = r'return'
t_VOID = r'void'
t_MAIN = r'main'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMI = r';'
t_COMMA = r','
t_ASSIGN = r'='
t_EQ = r'=='
t_NEQ = r'!='
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'

# Ignorar espacios en blanco y saltos de línea
t_ignore = ' \t\n'

def t_INCLUDE(t):
    r'\#include\s+<[^>\s]+>'
    return t

# Reglas de error
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


def p_include_statement(p):
    '''include_statement : INCLUDE_DIRECTIVE'''
    pass


# Reglas sintácticas

def p_function_declaration(p):
    '''function_declaration : type ID LPAREN params RPAREN LBRACE statements return_statement RBRACE'''
    pass


def p_params(p):
    '''params : type ID
              | type ID COMMA params'''
    pass


def p_return_statement(p):
    '''return_statement : RETURN expression SEMI
                        | RETURN SEMI'''
    pass


def p_statements(p):
    '''statements : statement statements
                  | empty'''
    pass


def p_statement(p):
    '''statement : if_statement
                 | declaration
                 | expression_statement
                 | while_statement
                 | for_statement
                 | function_call SEMI'''
    pass


def p_if_statement(p):
    '''if_statement : IF LPAREN expression RPAREN LBRACE statements RBRACE
                    | IF LPAREN expression RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE'''
    pass


def p_declaration(p):
    '''declaration : type ID SEMI
                   | type ID ASSIGN expression SEMI
                   | type ID LBRACKET INT RBRACKET SEMI
                   | type ID LBRACKET INT RBRACKET ASSIGN LBRACE INT RBRACE SEMI'''
    pass


def p_type(p):
    '''type : INT
            | CHAR
            | FLOAT
            | VOID'''
    pass


def p_expression(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression MOD expression
                  | expression EQ expression
                  | expression NEQ expression
                  | expression LT expression
                  | expression LTE expression
                  | expression GT expression
                  | expression GTE expression
                  | LPAREN expression RPAREN
                  | ID
                  | INT
                  | FLOAT
                  | CHAR
                  | function_call'''
    pass


def p_expression_statement(p):
    '''expression_statement : expression SEMI'''
    pass


def p_while_statement(p):
    '''while_statement : WHILE LPAREN expression RPAREN LBRACE statements RBRACE'''
    pass


def p_for_statement(p):
    '''for_statement : FOR LPAREN declaration expression_statement expression RPAREN LBRACE statements RBRACE'''
    pass


def p_function_call(p):
    '''function_call : ID LPAREN args RPAREN'''
    pass


def p_args(p):
    '''args : expression
            | expression COMMA args'''
    pass


def p_empty(p):
    'empty :'
    pass


def p_error(p):
    print(f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token '{p.value}'")


# Construye el parser
lexer = lex.lex()
parser = yacc.yacc(debug=False)

# Entrada de prueba (reemplaza esto con tu código fuente en C)
data = '''#include <stdio.h>

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
}'''

# Analiza la entrada
parser.parse(data)
