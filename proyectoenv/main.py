# ------------------------------------------------------------
# Lexer para C
# ------------------------------------------------------------
import ply.lex as lex

# List of token names. This is always required
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
    'float',
    'INCLUDE',  # Added for #include
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


# Preprocessor directive rule
def t_INCLUDE(t):
    r'\#include\s*\<[^\>]+\>'
    return t


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
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}, position {t.lexpos}")
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

lexer.input("""
    #include <stdio.h>
    """)

# Print the tokens produced by the lexer
for tok in lexer:
    print(tok)

S = 0
S2 = 1
T = 2
T2 = 3
F = 4
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


def miParser():
    # f = open('fuente.c','r')
    # lexer.input(f.read())
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
    lexer.input("""
        #include <stdio.h>
        int a, b, c;$""")

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

"""
1. Program -> IncludeDeclaration MainFunction

2. IncludeDeclaration -> INCLUDE STRING finInstruccion

3. MainFunction -> 'int' 'main' '(' ')' '{' Declaration* Statement* 'return' NUMBER ';' '}'

4. Declaration -> Type IdentifierList finInstruccion

5. Type -> 'int' | 'char' | 'float'

6. IdentifierList -> 'identificador' IdentifierList'

7. IdentifierList' -> ',' 'identificador' IdentifierList' | ε

8. Statement -> 'identificador' '=' Expression finInstruccion
              | 'if' '(' Expression ')' '{' Statement* '}' 'else' '{' Statement* '}'
              | 'printf' '(' STRING ',' ExpressionList ')' finInstruccion
              | 'return' Expression finInstruccion
              | 'void' 'imprimir_mayor' '(' Expression ',' Expression ')' '{' Statement* '}'
              | 'while' '(' Expression ')' '{' Statement* '}'

9. ExpressionList -> Expression ExpressionList'

10. ExpressionList' -> ',' Expression ExpressionList' | ε

11. Expression -> SimpleExpression ComparisonOp SimpleExpression | SimpleExpression

12. ComparisonOp -> '>' | '<' | '>=' | '<=' | '==' | '!='

13. SimpleExpression -> Term SimpleExpression'

14. SimpleExpression' -> '+' Term SimpleExpression' | '-' Term SimpleExpression' | ε

15. Term -> Factor Term'

16. Term' -> '*' Factor Term' | '/' Factor Term' | ε

17. Factor -> 'identificador' | NUMBER | '(' Expression ')' | 'printf' | STRING

18. StatementList -> Statement StatementList' | ε

19. StatementList' -> Statement StatementList' | ε

FIRST(Program) = {INCLUDE, 'int'}
FIRST(IncludeDeclaration) = {INCLUDE}
FIRST(MainFunction) = {'int'}
FIRST(Declaration) = {'int', 'char', 'float'}
FIRST(Type) = {'int', 'char', 'float'}
FIRST(IdentifierList) = {'identificador'}
FIRST(IdentifierList') = {',', ε}
FIRST(Statement) = {'identificador', 'if', 'printf', 'return', 'void', 'while'}
FIRST(ExpressionList) = {'identificador', NUMBER, '(', 'printf', STRING, ε}
FIRST(ExpressionList') = {',', ε}
FIRST(Expression) = {'identificador', NUMBER, '(', 'printf', STRING}
FIRST(ComparisonOp) = {'>', '<', '>=', '<=', '==', '!='}
FIRST(SimpleExpression) = {'identificador', NUMBER, '(', 'printf', STRING}
FIRST(SimpleExpression') = {'+', '-', ε}
FIRST(Term) = {'identificador', NUMBER, '(', 'printf', STRING}
FIRST(Term') = {'*', '/', ε}
FIRST(Factor) = {'identificador', NUMBER, '(', 'printf', STRING}

FOLLOW Sets:
plaintext
Copy code
FOLLOW(Program) = {eof}
FOLLOW(IncludeDeclaration) = {INCLUDE, 'int'}
FOLLOW(MainFunction) = {eof}
FOLLOW(Declaration) = {INCLUDE, 'int', 'char', 'float', '}', 'if', 'printf', 'return', 'void', 'while'}
FOLLOW(Type) = {'identificador'}
FOLLOW(IdentifierList) = {';', ')'}
FOLLOW(IdentifierList') = {';', ')'}
FOLLOW(Statement) = {'identificador', 'if', 'printf', 'return', 'void', 'while', '}', eof}
FOLLOW(ExpressionList) = {')'}
FOLLOW(ExpressionList') = {')'}
FOLLOW(Expression) = {')', ';', '==', '!=', '>', '<', '>=', '<='}
FOLLOW(ComparisonOp) = {'identificador', NUMBER, '(', 'printf', STRING}
FOLLOW(SimpleExpression) = {')', ';', '==', '!=', '>', '<', '>=', '<=', '+', '-', 'identificador', NUMBER, '(', 'printf', STRING}
FOLLOW(SimpleExpression') = {')', ';', '==', '!=', '>', '<', '>=', '<='}
FOLLOW(Term) = {')', ';', '==', '!=', '>', '<', '>=', '<=', '+', '-', 'identificador', NUMBER, '(', 'printf', STRING}
FOLLOW(Term') = {')', ';', '==', '!=', '>', '<', '>=', '<=', '+', '-'}
FOLLOW(Factor) = {'*', '/', ')', ';', '==', '!=', '>', '<', '>=', '<=', '+', '-', 'identificador', NUMBER, '(', 'printf', STRING}
LL(1) Parsing Table:

|        | INCLUDE | int | char | float | identificador | NUMBER | ( | ) | { | } | ; | , | if | else | printf | return | void | while | + | - | * | / | < | > | <= | >= | == | != | STRING | eof |
|--------|---------|-----|------|-------|----------------|--------|---|---|---|---|---|---|----|------|--------|--------|------|-------|---|---|---|---|---|---|----|----|----|----|--------|-----|
| Program        |         | S   |     |       | S              |        |   |   |   |   |   |   |    |      |        |        |      |        |   |   |   |   |   |   |    |    |    |    |        |     |
| IncludeDeclaration | INCLUDE |     |     |       |                |        |   |   |   |   |   |   |    |      |        |        |      |        |   |   |   |   |   |   |    |    |    |    |        |     |
| MainFunction    |         |     |     |       |                |        |   |   |   |   |   |   |    |      |        |        |      |        |   |   |   |   |   |   |    |    |    |    |        |     |
| Declaration    |         | S   | S   | S     |                |        |   |   |   |   |   |   |    |      |        |        |      |        |   |   |   |   |   |   |    |    |    |    |        |     |
| Type           |         | S   | S   | S     |                |        |   |   |   |   |   |   |    |      |        |        |      |        |   |   |   |   |   |   |    |    |    |    |        |     |
| IdentifierList |         | S   |     |       | S              |        |   |   |   |   |   |   |    |      |        |        |      |        |   |   |   |   |   |   |    |    |    |    |        |     |
| IdentifierList'|   ε     |     |     |       |                |        |   |   |   |   |   |   |    |      |        |        |      |        |   |   |   |   |   |   |    |    |    |    |        |     |
| Statement      |         | S   |     |       | S              |        |   |   |   |   |   |   |    |      |        |        |      |        |   |   |   |   |   |   |    |    |    |    |        |     |
| ExpressionList |         | S   |     |       | S              |        |   |   |   |   |   |   |    |      |        |        |      |        |   |   |   |   |   |   |    |    |    |    |        |     |
| ExpressionList'|   ε     |     |     |       |                |        |   |   |   |   |   |   |    |      |        |        |      |        |   |   |   |   |   |   |    |    |    |    |        |     |
| Expression     |         | S   |     |       | S              | S      | S |   |   |   |   |   |    |      |        |        |      |        |   |   |   |   |   |   |    |    |    |    |        |     |
| ComparisonOp   |         |     |     |       |                |        |   |   |   |   |   |   |    |      |        |        |      |        |   |   |   |   |   |   |    |    |    |    |        |     |
| SimpleExpression|        | S   |     |       | S              | S      | S |   |   |   |   |   |    |      |        |        |      |        |   |   |   |   |   |   |    |    |    |    |        |     |
| SimpleExpression'|   ε  |     |     |       |                |        |   |   |   |   |   |   |    |      |        |        |      |        |   |   |   |   |   |   |    |    |    |    |        |     |
| Term           |         | S   |     |       | S              | S      | S |   |   |   |   |   |    |      |        |        |      |        |   |   |   |   |   |   |    |    |    |    |        |     |
| Term'          |   ε     |     |     |       |                |        |   |   |   |   |   |   |    |      |        |        |      |        |   |   |   |   |   |   |    |    |    |    |        |     |
| Factor         |         | S   |     |       | S              | S      | S |   |   |   |   |   |    |      |        |        |      |        |   |   |   |   |   |   |    |    |    |    |        |     |

"""