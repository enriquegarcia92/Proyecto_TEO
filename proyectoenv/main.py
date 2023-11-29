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

S = 0
LIB = 1
LIB2 = 2
LIBEND = 3
PARAM = 4
ADDPARAM = 5
NUMRETURN = 6
ARITMETIC = 8
SUMA2 = 9
RETURNNUM = 10
GHANDLER = 11
CHARFRETURN = 12
RETURNCHAR = 13
FLOATN = 16
DECIMAL = 17
THANDLER = 18
OPENNUMFUN = 19
OPENCHARFUN = 20
OPENVOID = 21
FBODY = 22
VOIDRETURN = 23
RETURNVOID = 24
CONDITIONSHANDLER = 25
LOGICSIMBOLS = 26
NOTHANDLER = 27
ELSEXTENTION = 28
PRINTCONT = 29
FUNCUSE = 30
USEPARAM = 31
tabla = [
    [S, 'hashtoken', ['hashtoken', 'identificador', 'lesser_than', LIB]],
    # Manejo de variables globales
    # Manejo de declaración de funciones
    [S, 'int', ['int', 'identificador', OPENNUMFUN, S]],
    [S, 'char', ['char', 'identificador', OPENCHARFUN, S]],
    [S, 'float', ['float', 'identificador', OPENNUMFUN, S]],
    [S, 'keyword', ['keyword', 'identificador', OPENVOID, S]],
    [S, 'comentario', ['comentario', S]],
    [S, 'identificador', ['identificador','LPAREN', USEPARAM, 'RPAREN', 'finInstruccion', S]],
    # Manejo de funcion void
    [OPENVOID, 'LPAREN', ['LPAREN', PARAM, FBODY, VOIDRETURN, 'finBloque']],
    # Manejar global scope de numericas
    [OPENNUMFUN, 'asignacion', ['asignacion', RETURNNUM, S]],
    [OPENNUMFUN, 'LPAREN', ['LPAREN', PARAM, FBODY, NUMRETURN, 'finBloque']],
    # cuerpo de funciones int
    [FBODY, 'comentario', ['comentario', FBODY]],
    [FBODY, 'int', ['int', 'identificador', 'asignacion', RETURNNUM, FBODY]],
    [FBODY, 'float', ['float', 'identificador', 'asignacion', RETURNNUM, FBODY]],
    [FBODY, 'char', ['char', 'identificador', 'asignacion', RETURNCHAR, FBODY]],
    [FBODY, 'identificador', ['identificador', 'LPAREN', USEPARAM, 'RPAREN', 'finInstruccion', FBODY]],
    [FBODY, 'if', ['if', 'LPAREN', CONDITIONSHANDLER, 'RPAREN', 'inicioBloque', FBODY, 'finBloque', FBODY]],
    [FBODY, 'while', ['while', 'LPAREN', CONDITIONSHANDLER, 'RPAREN', 'inicioBloque', FBODY, 'finBloque', FBODY]],
    [FBODY, 'else', ['else', ELSEXTENTION]],
    [FBODY, 'printf', ['printf', 'LPAREN', PRINTCONT, 'RPAREN', 'finInstruccion', FBODY]],
    [FBODY, 'aumentarvar',['aumentarvar','finInstruccion', FBODY]],
    [FBODY, 'reducirvar', ['reducirvar','finInstruccion', FBODY]],
    [FBODY, 'keyword', []],
    [FBODY, 'finBloque', []],
    #Manejo de estrucutra print
    [PRINTCONT, 'cadena', [THANDLER, PRINTCONT]],
    [PRINTCONT, 'identificador', [THANDLER,PRINTCONT]],
    [PRINTCONT, 'NUMBER', [THANDLER,PRINTCONT]],
    [PRINTCONT, 'coma', ['coma', PRINTCONT,PRINTCONT]],
    [PRINTCONT, 'RPAREN', []],
        # Manejo de else
    [ELSEXTENTION, 'inicioBloque', ['inicioBloque', FBODY, 'finBloque', FBODY]],
    [ELSEXTENTION, 'if', [FBODY]],
    # Manejo de condicionales de if
    [CONDITIONSHANDLER, 'identificador', [THANDLER, LOGICSIMBOLS]],
    [CONDITIONSHANDLER, 'NUMBER', [THANDLER, LOGICSIMBOLS]],
    [CONDITIONSHANDLER, 'not', ['not', THANDLER, LOGICSIMBOLS]],
    # Simbolos de if
    [LOGICSIMBOLS, 'and', ['and', NOTHANDLER, LOGICSIMBOLS]],
    [LOGICSIMBOLS, 'or', ['or', NOTHANDLER, LOGICSIMBOLS]],
    [LOGICSIMBOLS, 'lesser_than', ['lesser_than', NOTHANDLER, LOGICSIMBOLS]],
    [LOGICSIMBOLS, 'greater_than', ['greater_than', NOTHANDLER, LOGICSIMBOLS]],
    [LOGICSIMBOLS, 'not', ['not', NOTHANDLER, LOGICSIMBOLS]],
    [LOGICSIMBOLS, 'RPAREN', []],
    # Manejo de uso de not
    [NOTHANDLER, 'not', ['not', THANDLER]],
    [NOTHANDLER, 'identificador', [THANDLER]],
    [NOTHANDLER, 'NUMBER', [THANDLER]],
    # Manejar global scope de char
    [OPENCHARFUN, 'asignacion', ['asignacion', RETURNCHAR, S]],
    [OPENCHARFUN, 'LPAREN', ['LPAREN', PARAM, CHARFRETURN, 'finBloque']],
    # Manejo de retornos de funcion char
    [VOIDRETURN, 'keyword', ['keyword', RETURNVOID]],
    [VOIDRETURN, 'finBloque', []],
    [CHARFRETURN, 'keyword', ['keyword', RETURNCHAR]],
    # Manejo de retornos de funcion int
    [NUMRETURN, 'keyword', ['keyword', RETURNNUM]],
    # Manejo de retorno de void
    [RETURNVOID, 'single_quote', ['single_quote', 'identificador', 'single_quote', 'finInstruccion']],
    [RETURNVOID, 'identificador', ['identificador', ARITMETIC]],
    [RETURNVOID, 'LPAREN', ['LPAREN', THANDLER, ARITMETIC]],
    [RETURNVOID, 'NUMBER', [FLOATN, ARITMETIC]],
    [RETURNVOID, 'finBloque', []],
    # Manejo de retorno para funciones char
    [RETURNCHAR, 'single_quote', ['single_quote', 'identificador', 'single_quote', 'finInstruccion']],
    [RETURNCHAR, 'identificador', ['identificador', 'finInstruccion']],
    [RETURNCHAR, 'LPAREN', ['LPAREN', 'char', 'RPAREN', 'identificador', 'finInstruccion']],
    # Manejo de retornos para funciones INT
    [RETURNNUM, 'identificador', ['identificador', FUNCUSE, ARITMETIC]],
    [RETURNNUM, 'LPAREN', ['LPAREN', THANDLER, ARITMETIC]],
    [RETURNNUM, 'NUMBER', [FLOATN, ARITMETIC]],
    #Manejo de uso de funciones
    [FUNCUSE, 'LPAREN', ['LPAREN', USEPARAM, 'RPAREN', 'finInstruccion']],
    [FUNCUSE, 'PLUS', []],
    # Manejo de operaciones aritmeticas basicas
    [ARITMETIC, 'LPAREN', ['LPAREN', THANDLER, ARITMETIC]],
    [ARITMETIC, 'RPAREN', ['RPAREN', ARITMETIC]],
    [ARITMETIC, 'PLUS', ['PLUS', GHANDLER, ARITMETIC]],
    [ARITMETIC, 'MINUS', ['MINUS', GHANDLER, ARITMETIC]],
    [ARITMETIC, 'TIMES', ['TIMES', GHANDLER, ARITMETIC]],
    [ARITMETIC, 'DIVIDE', ['DIVIDE', GHANDLER, ARITMETIC]],
    [ARITMETIC, 'finInstruccion', ['finInstruccion']],
    # Manejador de parentesis en operacioens aritmeticas
    [GHANDLER, 'identificador', ['identificador']],
    [GHANDLER, 'LPAREN', ['LPAREN', THANDLER]],
    [GHANDLER, 'NUMBER', [FLOATN]],
    # Manejador de tipo de variable
    [THANDLER, 'identificador', ['identificador']],
    [THANDLER, 'NUMBER', [FLOATN]],
    [THANDLER, 'cadena', ['cadena']],
    # Cadenas para manejar parametros en funciones
    [PARAM, 'int', ['int', 'identificador', PARAM]],
    [PARAM, 'char', ['char', 'identificador', PARAM]],
    [PARAM, 'float', ['float', 'identificador', PARAM]],
    [PARAM, 'RPAREN', ['RPAREN', 'inicioBloque']],
    [PARAM, 'coma', ['coma', PARAM]],
    #Manejar uso de parametros en funciones
    [USEPARAM, 'identificador', ['identificador', USEPARAM]],
    [USEPARAM, 'NUMBER', [FLOATN, USEPARAM]],
    [USEPARAM, 'single_quote', ['single_quote', 'identificador', 'single_quote', USEPARAM]],
    [USEPARAM, 'coma', ['coma', USEPARAM]],
    [USEPARAM, 'RPAREN', []],
    # Cadenas para leer los dos tipos de liberías de C
    [LIB, 'identificador', ['identificador', LIB2]],
    [LIB2, 'greater_than', ['greater_than', S]],
    [LIB2, 'dot', ['dot', 'identificador', 'greater_than', S]],
    # Auxiliaries
    [FLOATN, 'NUMBER', ['NUMBER', DECIMAL]],
    [DECIMAL, 'dot', ['dot', 'NUMBER']],
    [DECIMAL, 'MINUS', []],
    [DECIMAL, 'PLUS', []],
    [DECIMAL, 'TIMES', []],
    [DECIMAL, 'DIVIDE', []],
    [DECIMAL, 'RPAREN', []],
    [DECIMAL, 'finInstruccion', []],
    [DECIMAL, 'coma', []],
    # Cadena de fin de archivo
    [S, 'eof', ['eof']]
]

stack = ['eof', 0]

# Inicialiación de lexer
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
                print("En posición:", tok.lexpos)
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

''' int suma(int a, int b) 
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
        
        //Bucle while
        int i = 0;
        while(i<5){
        printf("Iteración %d\n", i);
        i++
        }
    
        return 0;
        }'''
