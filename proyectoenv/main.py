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
    'lesser_than',
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


# t.type está mal, también t.lexpos
def t_identificador(t):
    r'([a-z]|[A-Z]|_)([a-z]|[A-Z]|\d|_)*'
    insert_symbol(t.value, t.type, t.value, t.lineno, t.lexpos)
    t.value = (t.value,)
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
        
        //Bucle while
        int i = 0;
        while(i<5){
        printf("Iteración %d\n", i);
        i++
        }
    
        return 0;
        }$"""

# Inicialización de lexer
lexer = lex.lex()

# Inicialización de la tabla de símbolos
symbol_table = {}

# Se declara el diccionario de datos (Tabla Hash)
myDict = {}
# Se declara el arreglo de errores
errors = []


# Función para insertar un símbolo en la tabla de símbolos
def insert_symbol(identifier, symbol_type, value, line_number, scope):
    if identifier not in symbol_table:
        symbol_table[identifier] = {
            'type': symbol_type,
            'value': value,
            'line_number': line_number,
            'scope': scope
        }
    else:
        print(f"Error: El símbolo '{identifier}' ya existe en la tabla de símbolos.")


# Función para buscar un símbolo en la tabla de símbolos
def search_symbol(identifier):
    return symbol_table.get(identifier, None)


# Función para actualizar un símbolo en la tabla de símbolos
def update_symbol(identifier, symbol_type, value, line_number, scope):
    print("=====================================")
    print(symbol_table)
    if identifier in symbol_table:
        print("SE METIOO")
        symbol_table[identifier] = {
            'type': symbol_type,
            'value': value,
            'line_number': line_number,
            'scope': scope
        }
    else:
        print(f"Error: El símbolo '{identifier}' no existe en la tabla de símbolos.")


# Función para eliminar un símbolo de la tabla de símbolos
def delete_symbol(identifier):
    if identifier in symbol_table:
        del symbol_table[identifier]
    else:
        print(f"Error: El símbolo '{identifier}' no existe en la tabla de símbolos.")


def print_tokens(lexer, code):
    lexer.input(code)
    while True:
        token = lexer.token()
        if not token:
            break  # No more tokens
        print(token)


def get_hash(key):
    h = 20
    for char in key:
        h += ord(char)
    return h % 100


S = 0
F = 1
V = 2
R = 3
SUM = 4
FV = 5
IF = 6
C = 7
P = 8
E = 9
M = 10
VA = 11
VC = 12
VF = 13
COM = 14
VS = 15
P2 = 16
FI = 17
W = 18
C2 = 20
WC = 21
RET = 22
FIN = 23
tabla = [
    [S, 'preprocessor_directive', ['preprocessor_directive', F]],
    [F, 'int', ['int', 'identificador', 'LPAREN', V, 'coma', V, 'RPAREN', 'inicioBloque', R, 'finBloque', FV]],
    [V, 'int', ['int', 'identificador']],
    [R, 'keyword', ['keyword', SUM, 'finInstruccion']],
    [SUM, 'identificador', ['identificador', 'PLUS', 'identificador']],
    [FV, 'keyword', ['keyword', 'identificador', 'LPAREN', V, 'coma', V, 'RPAREN', 'inicioBloque', IF, 'finBloque', M]],
    [IF, 'keyword', ['keyword', 'LPAREN', C, 'RPAREN', 'inicioBloque', P, 'finBloque', E]],
    [C, 'identificador', ['identificador', 'greater_than', 'identificador']],
    [P, 'identificador',
     ['identificador', 'LPAREN', 'cadena', 'coma', 'identificador', 'coma', 'identificador', 'RPAREN',
      'finInstruccion']],
    [E, 'keyword', ['keyword', 'inicioBloque', P, 'finBloque']],
    [M, 'int',
     ['int', 'identificador', 'LPAREN', 'RPAREN', 'inicioBloque', VA, VC, VF, COM, VS, P2, COM, FI, COM, VA, W, RET,
      'finBloque', ]],
    [VA, 'int', ['int', 'identificador', 'asignacion', 'NUMBER', 'finInstruccion']],
    [VC, 'keyword',
     ['keyword', 'identificador', 'asignacion', 'single_quote', 'identificador', 'single_quote', 'finInstruccion']],
    [VF, 'float', ['float', 'identificador', 'asignacion', 'NUMBER', 'dot', 'NUMBER', 'finInstruccion']],
    [VS, 'int',
     ['int', 'identificador', 'asignacion', 'identificador', 'LPAREN', 'identificador', 'coma', 'NUMBER', 'RPAREN',
      'finInstruccion']],
    [P2, 'identificador', ['identificador', 'LPAREN', 'cadena', 'coma', 'identificador', 'RPAREN', 'finInstruccion']],
    [FI, 'identificador', ['identificador', 'LPAREN', 'NUMBER', 'coma', 'identificador', 'RPAREN', 'finInstruccion']],
    [W, 'keyword', ['keyword', 'LPAREN', C2, 'RPAREN', 'inicioBloque', P2, WC, 'finBloque']],
    [WC, 'identificador', ['identificador', 'PLUS', 'PLUS']],
    [C2, 'identificador', ['identificador', 'lesser_than', 'NUMBER']],
    [COM, 'comentario', ['comentario']],
    [RET, 'keyword', ['keyword', 'NUMBER', 'finInstruccion']],
    [FIN, 'finBloque', ['finBloque', 'eof']]
]

stack = ['eof', 0]


def miParser():
    global current_scope
    lexer.input(code)
    tok = lexer.token()
    hashWord = "Token 1"
    x = stack[-1]
    while True:
        if x == tok.type and x == 'eof':
            print("Cadena reconocida exitosamente")
            break
        else:
            if x == tok.type and x != 'eof':
                stack.pop()
                x = stack[-1]
                tok = lexer.token()
                hashKey = get_hash(hashWord)
                hashWord += "1"
                if tok.type != "error":
                    auxDict = {
                        hashKey: {"Type": tok.type, "Token": tok.value, "Line": tok.lineno, "Position": tok.lexpos,
                                  "TypeValue": type(tok.value)}}
                    print(auxDict)
                    myDict.update(auxDict)
            if x in tokens and x != tok.type:
                print("Error: se esperaba ", tok.type)
                print("En posición:", tok.lexpos)
                # Panic Mode - Manejador de Errores
                errors.append({"Error": "Se encontro un error de tipo " + tok.type + " en la linea " + str(
                    tok.lineno) + " se obtuvo: " + '"' + tok.value + '"'})
                while True:
                    tok = lexer.token()
                    if tok is None:
                        break
                    if tok.type == x:
                        break
                if tok is None:
                    break
            if x not in tokens:
                print("van entrar a la tabla:")
                print(x)
                print(tok.type)
                celda = buscar_en_tabla(x, tok.type)
                if celda is None:
                    print("Error: NO se esperaba", tok.type)
                    print("En posición:", tok.lexpos)
                    # errors.append(
                    #     {"Error": "Se encontro un error de tipo " + tok.type + " en la linea " + str(
                    #         tok.lineno) + " se obtuvo: " + '"' + tok.value + '"'})
                    return 0
                else:
                    stack.pop()
                    agregar_pila(celda)
                    print(stack)
                    print("------------")
                    x = stack[-1]
    print("\nTabla de símbolos:")
    for identifier, attributes in symbol_table.items():
        print(
            f"ID: {identifier}, Tipo: {attributes['type']}, Valor: {attributes['value']}, Línea: {attributes['line_number']}, Ámbito: {attributes['scope']}")
    print("----------------")
    print("\n")
        # if not tok:
        # break
        # print(tok)
        # print(tok.type, tok.value, tok.lineno, tok.lexpos)


def buscar_en_tabla(no_terminal, terminal):
    for i in range(len(tabla)):
        if tabla[i][0] == no_terminal and tabla[i][1] == terminal:
            return tabla[i][2]  # retorno la celda


def agregar_pila(produccion):
    for elemento in reversed(produccion):
        if elemento != 'vacia':  # la vacía no la inserta
            stack.append(elemento)


miParser()

# Imprimir valores del diccionario de datos
print("Diccionario de palabras")
print("Key", "\t", "Value")
for key, value in myDict.items():
    print(key, "\t", value)
print("----------------")

semanticHash = []


def findVariableDeclarations():
    hashedList = list(myDict.values())
    n = len(hashedList)
    for i in range(0, n):
        if (hashedList[i]['Token'] == 'int' or hashedList[i]['Token'] == 'float') and hashedList[i + 2]["Token"] == '=':
            semanticHash.append(
                {"Type": hashedList[i]['Token'], "Value": hashedList[i + 3]['Token'], 'Line': hashedList[i]['Line']})

        if hashedList[i]['Token'] == 'if' and hashedList[i + 2]['Type'] == 'identifier':
            semanticHash.append(
                {"Type": hashedList[i]['Token'], 'Value': hashedList[i + 2]['Type'], 'Line': hashedList[i]['Line']})


def checkVariableDeclarations():
    for i in semanticHash:
        if (i['Type'] == 'int') and type(i['Value']) != int:
            print("Error semántico: Declaracion de variable Int se espera un entero en la linea ", i['Line'],
                  "se obtuvo:", '"', i['Value'], '"')

        if (i['Type'] == 'if') and i['Value'] == 'identifier':
            print("Error semántico: Tipos no Compatibles en la linea ", i['Line'])

        if (i['Type'] == 'float') and type(i['Value']) != float:
            print("Error semántico: Declaracion de variable Float se espera un flotante en la linea ", i['Line'],
                  "se obtuvo:", '"', i['Value'], '"')

    print("\n")


def checkErrors():
    if len(errors) > 0:
        for i in errors:
            print("Error sintactico: ", i['Error'])
    else:
        print("No se encontraron errores")


def miAnalizadorSemantico():
    findVariableDeclarations()
    checkVariableDeclarations()
    checkErrors()


miAnalizadorSemantico()
