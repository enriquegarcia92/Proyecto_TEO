# ------------------------------------------------------------
# Lexer para C
# ------------------------------------------------------------
import ply.lex as lex

S = 0
S2 = 1
T = 2
T2 = 3
F = 4

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
    'eof',
    'int',
    'float'
    # 'vacia'
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
t_eof = r'\$'


# t_vacia= r'\'

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
    r'(char)|(return)|(if)|(else)|(do)|(while)|(for)|(void)'
    return t


def t_identificador(t):
    r'([a-z]|[A-Z]|_)([a-z]|[A-Z]|\d|_)*'
    return t


def t_cadena(t):
    r'\".*\"'
    return t


def t_comentario(t):
    r'\/\/.*'
    return t


def t_comentario_bloque(t):
    r'\/\*(.|\n)*\*\/'
    # return t


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    return t


TT = 1
D = 2
tabla = [[S, 'identificador', None],
         [S, 'int', [TT, 'identificador', D]],
         [S, 'float', [TT, 'identificador', D]],
         [S, 'coma', None],
         [S, 'finInstruccion', None],
         [TT, 'identificador', None],
         [TT, 'int', ['int']],
         [TT, 'float', ['float']],
         [TT, 'coma', None],
         [TT, 'finInstruccion', None],
         [D, 'identificador', None],
         [D, 'int', None],
         [D, 'float', None],
         [D, 'coma', ['coma', 'identificador', D]],
         [D, 'finInstruccion', ['finInstruccion']],
         ]

stack = ['eof', 0]

# Build the lexer
lexer = lex.lex()


def miParser():
    # f = open('fuente.c','r')
    # lexer.input(f.read())
    lexer.input('int a, b c;$')

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


'''1. S -> Programa

2. Programa -> Instrucciones

3. Instrucciones -> Instruccion Instrucciones | ε

4. Instruccion -> Declaracion | Asignacion | LlamadaFuncion | EstructuraControl | Impresion

5. Declaracion -> TipoDato Identificador ;

6. TipoDato -> int | char | float

7. Identificador -> id

8. Asignacion -> Identificador = Expresion ;

9. LlamadaFuncion -> id ( Argumentos ) ;

10. Argumentos -> Expresion Argumentos' | ε

11. Argumentos' -> , Expresion Argumentos' | ε

12. EstructuraControl -> if ( Expresion ) BloqueCodigo ElseBloque

13. ElseBloque -> else BloqueCodigo | ε

14. BloqueCodigo -> { Instrucciones }

15. Impresion -> printf ( " Cadena " , Expresion ) ;

16. Expresion -> Expresion + Termino | Termino

17. Termino -> Termino * Factor | Factor

18. Factor -> ( Expresion ) | Identificador | Numero | Caracter | LlamadaFuncion

19. Numero -> entero | decimal

20. Caracter -> 'cualquierCaracter'

First(Programa) = { int, char, float, id, if, printf, ε }
First(Instrucciones) = { int, char, float, id, if, printf, ε }
First(Instruccion) = { int, char, float, id, if, printf }
First(Declaracion) = { int, char, float }
First(TipoDato) = { int, char, float }
First(Identificador) = { id }
First(Asignacion) = { id }
First(LlamadaFuncion) = { id }
First(Argumentos) = { (, id, entero, decimal, 'c', ε }
First(Argumentos') = { ,, ε }
First(EstructuraControl) = { if }
First(ElseBloque) = { else, ε }
First(BloqueCodigo) = { { }
First(Impresion) = { printf }
First(Expresion) = { (, id, entero, decimal, 'c' }
First(Termino) = { (, id, entero, decimal, 'c' }
First(Factor) = { (, id, entero, decimal, 'c' }
First(Numero) = { entero, decimal }
First(Caracter) = { 'cualquierCaracter' }

Follow(Programa) = { $ }
Follow(Instrucciones) = { $ }
Follow(Instruccion) = { int, char, float, id, if, printf, }, $ }
Follow(Declaracion) = { int, char, float, id, if, printf, }, $ }
Follow(TipoDato) = { id }
Follow(Identificador) = { =, ,, ; }
Follow(Asignacion) = { int, char, float, id, if, printf, }, $ }
Follow(LlamadaFuncion) = { int, char, float, id, if, printf, }, $ }
Follow(Argumentos) = { ) }
Follow(Argumentos') = { ) }
Follow(EstructuraControl) = { int, char, float, id, if, printf, }, $ }
Follow(ElseBloque) = { int, char, float, id, if, printf, }, $ }
Follow(BloqueCodigo) = { int, char, float, id, if, printf, }, $ }
Follow(Impresion) = { int, char, float, id, if, printf, }, $ }
Follow(Expresion) = { +, ), ; }
Follow(Termino) = { +, ), ; }
Follow(Factor) = { +, *, ), ; }
Follow(Numero) = { +, *, ), ; }
Follow(Caracter) = { +, *, ), ; }

| No Terminal      | int | char | float | id | if | else | { | } | ( | ) | , | ; | printf | + | * | / | entero | decimal | 'c' | $ |
|------------------|-----|------|-------|----|----|------|---|---|---|---|---|---|--------|---|---|---|--------|---------|-----|---|
| Programa         | 1   | 1    | 1     | 1  |    |      | 1 |   |   |   |   |   | 1      |   |   |   |        |         |     |   |
| Instrucciones    | 2   | 2    | 2     | 2  | 2  |      | 2 |   |   |   |   |   | 2      |   |   |   | 2      | 2       | 2   |   |
| Instruccion      | 5   | 5    | 5     | 5  | 12 |      | 12|   | 5 |   |   |   | 5      |   |   |   | 5      | 5       | 5   |   |
| Declaracion      | 6   | 6    | 6     | 6  |    |      |   |   |   |   |   |   |        |   |   |   |        |         |     |   |
| TipoDato         | 6   | 6    | 6     | 6  |    |      |   |   |   |   |   |   |        |   |   |   |        |         |     |   |
| Identificador    |     |      |       | 7  |    |      |   |   |   |   |   |   |        |   |   |   |        |         |     |   |
| Asignacion       |     |      |       | 8  |    |      |   |   |   |   |   |   |        |   |   |   |        |         |     |   |
| LlamadaFuncion   |     |      |       | 9  |    |      |   |   |   |   |   |   |        |   |   |   |        |         |     |   |
| Argumentos       | 16  | 16   | 16    | 16 | 16 |      | 16|   | 16|   |   |   | 16     |   |   |   | 16     | 16      | 16  |   |
| Argumentos'      | 11  | 11   | 11    | 11 | 11 |      | 11|   | 11|   |   |   | 11     |   |   |   | 11     | 11      | 11  | 11|
| EstructuraControl|     |      |       |    | 12 | 13   |   |   |   |   |   |   |        |   |   |   |        |         |     |   |
| ElseBloque       |     |      |       |    |    | 14   |   |   |   |   |   |   |        |   |   |   |        |         |     | 14|
| BloqueCodigo     | 14  | 14   | 14    | 14 | 14 | 14   | 14|   | 14|   |   |   | 14     |   |   |   | 14     | 14      | 14  |   |
| Impresion        |     |      |       |    |    |      |   |   |   |   |   |   | 15     |   |   |   |        |         |     |   |
| Expresion        | 17  | 17   | 17    | 17 |    |      |   |   | 17|   |   |   | 17     |   |   |   | 17     | 17      | 17  |   |
| Termino          |     |      |       | 17 |    |      |   |   | 17|   |   |   | 17     |   | 17|   | 17     | 17      | 17  |   |
| Factor           | 18  | 18   | 18    | 18 |    |      |   |   | 18|   |   |   | 18     |   | 18|   | 18     | 18      | 18  |   |
| Numero           | 19  | 19   | 19    | 19 |    |      |   |   | 19|   |   |   | 19     |   | 19|   | 19     | 19      |     |   |
| Caracter         |     |      |       |    |    |      |   |   |   |   |   |   |        |   |   |   |        |         | 20  |   |


'''