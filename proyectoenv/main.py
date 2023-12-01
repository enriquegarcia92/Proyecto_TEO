import ply.lex as lex
import symbolTable as TablaSimbolos
import parsingTable as tabla
import time


while True:
    try:
        # Nombre de tokens
        tokens = (
            "aumentarvar",
            "reducirvar",
            "libcall",
            "NUMBER",
            "PLUS",
            "MINUS",
            "TIMES",
            "DIVIDE",
            "LPAREN",
            "while",
            "RPAREN",
            "keyword",
            "printf",
            "inicioBloque",
            "finBloque",
            "finInstruccion",
            "asignacion",
            "comentario",
            "comentario_bloque",
            "cadena",
            "coma",
            "int",
            "char",
            "float",
            "greater_than",
            "lesser_than",
            "single_quote",
            "dot",
            "hashtoken",
            "identificador",
            "if",
            "else",
            "else_if",
            "or",
            "and",
            "not",
            "eof",
        )

        # Tokens simples
        t_PLUS = r"\+"
        t_MINUS = r"-"
        t_TIMES = r"\*"
        t_DIVIDE = r"/"
        t_LPAREN = r"\("
        t_RPAREN = r"\)"
        t_inicioBloque = r"\{"
        t_finBloque = r"\}"
        t_finInstruccion = r"\;"
        t_asignacion = r"\="
        t_coma = r"\,"
        t_eof = r"\$"
        t_hashtoken = r"\#"

        # Crear instancia de la tabla de símbolos
        tabla_simbolos = TablaSimbolos.TablaSimbolos()


        # Reglas de tokens, expersiones regulares
        def t_aumentarvar(t):
            r"([a-z]|[A-Z]|_)([a-z]|[A-Z]|\d|_)*\+\+"
            return t


        def t_reducirvar(t):
            r"([a-z]|[A-Z]|_)([a-z]|[A-Z]|\d|_)*\-\-"
            return t


        def t_libcall(t):
            r"\<([a-zA-Z_][a-zA-Z0-9_]*)\>"
            t.value = t.value[1:-1]  # Extract the identifier part
            return t


        def t_int(t):
            r"(int)"
            return t


        def t_while(t):
            r"(while)"
            return t


        def t_or(t):
            r"\|\|"
            return t


        def t_and(t):
            r"(&&)"
            return t


        def t_not(t):
            r"(!)"
            return t


        def t_if(t):
            r"(if)"
            return t


        def t_else(t):
            r"(else)"
            return t


        def t_else_if(t):
            r"(else if)"
            return t


        def t_char(t):
            r"(char)"
            return t


        def t_float(t):
            r"(float)"
            return t


        def t_printf(t):
            r"(printf)"
            return t


        def t_NUMBER(t):
            r"\d+"
            t.value = int(t.value)
            return t


        def t_keyword(t):
            r"(char|return|do|while|for|void)"
            return t


        def t_identificador(t):
            r"([a-z]|[A-Z]|_)([a-z]|[A-Z]|\d|_)*"
            return t


        def t_newline(t):
            r"\n+"
            t.lexer.lineno += len(t.value)


        t_ignore = " \t"


        def t_cadena(t):
            r"\"[^\"]*\" "
            return t


        def t_comentario(t):
            r"\/\/.*"
            return t


        def t_comentario_bloque(t):
            r"\/\*(.|\n)*\*\/"
            # return t


        def t_greater_than(t):
            r">"
            return t


        def t_lesser_than(t):
            r"<"
            return t


        def t_single_quote(t):
            r"\'"
            return t


        def t_dot(t):
            r"\."
            return t


        def t_error(t):
            print(f"Illegal character '{t.value[0]}' at line {t.lineno}, position {t.lexpos}")
            t.lexer.skip(1)


        # Función para leer el código fuente desde un archivo
        def readSourceCodeFromFile(filename):
            with open(filename, "r") as file:
                source_code = file.read()
            return source_code


        stack = ["eof", 0]

        # Inicialiación de lexer
        lexer = lex.lex()


        def buscar_token_esperado(no_terminal):
            expected = []
            for row in tabla.tabla:
                if row[0] == no_terminal and row[2] is not None:
                    expected.append(row[1])
            return expected


        def miParser():
            filename = "../proyectoenv/example.c"
            code = readSourceCodeFromFile(filename)
            lexer.input(code)
            tok = lexer.token()
            x = stack[-1]  # primer elemento de der a izq
            current_var_type = None
            scope = 0
            while True:
                # Manejo de tabla de simbolos
                if tok.type == "int":
                    current_var_type = "int"
                if tok.type == "char":
                    current_var_type = "char"
                if tok.type == "float":
                    current_var_type = "float"
                if tok.type == "inicioBloque":
                    scope = 1
                if tok.type == "finBloque":
                    scope = 0
                if tok.type == "identificador":
                    if current_var_type is not None:
                        tabla_simbolos.insertar(
                            tok.value, current_var_type, tok.value, tok.lineno, scope
                        )
                        current_var_type = None
                    elif current_var_type is None:
                        tabla_simbolos.insertar(
                            tok.value, tok.type, tok.value, tok.lineno, scope
                        )
                # Parseo
                if x == tok.type and x == "eof":
                    print("Cadena reconocida exitosamente")
                    tabla_simbolos.imprimir_tabla()  # Imprimir tabla de símbolos al final
                    return  # aceptar
                else:
                    if x == tok.type and x != "eof":
                        stack.pop()
                        x = stack[-1]
                        tok = lexer.token()
                    if x in tokens and x != tok.type:
                        print("Error detectado")
                        expected_tokens = buscar_token_esperado(x)
                        if len(expected_tokens) == 0:
                            expected_tokens = ['hashToken', 'int', 'char', 'float', 'keyword', 'comentario', 'identificador']
                        print("Error: se esperaba uno de", expected_tokens, "pero se encontró", tok.type)
                        print("En linea:", tok.lineno)
                        tok = recuperar_modo_panico(expected_tokens, tok)
                        if tok is None or tok.type == 'eof':
                            print("No se pudo recuperar del error.")
                            return 0
                        # Reanuda el análisis después de la recuperación
                        x = stack[-1]
                        continue
                    if x not in tokens:  # es no terminal
                        print("van entrar a la tabla:")
                        print(x)
                        print(tok.type)
                        celda = buscar_en_tabla(x, tok.type)
                        # Manejo de Errores y Recuperación
                        if celda is None:
                            print("Error detectado")
                            expected_tokens = buscar_token_esperado(x)
                            if len(expected_tokens) == 0:
                                expected_tokens = ['hashToken', 'int', 'char', 'float', 'keyword', 'comentario',
                                                   'identificador']
                            print("Error: se esperaba uno de", expected_tokens, "pero se encontró", tok.type)
                            print("En linea:", tok.lineno)
                            print("celda: ", celda)
                            tok = recuperar_modo_panico(expected_tokens, tok)
                            if tok is None or tok.type == 'eof':
                                print("No se pudo recuperar del error.")
                                return 0
                            # Reanuda el análisis después de la recuperación
                            x = stack[-1]
                            continue
                        else:
                            stack.pop()
                            agregar_pila(celda)
                            print(stack)
                            print("/------------------------------------------------------------------------------/")
                            x = stack[-1]



        def recuperar_modo_panico(recovery_tokens, tok):
            while tok is not None and tok.type not in recovery_tokens:
                tok = lexer.token()
            while stack and (stack[-1] not in recovery_tokens and stack[-1] in tokens):
                stack.pop()
            if stack and tok is not None:
                return tok
            else:
                return tok


        def buscar_en_tabla(no_terminal, terminal):
            for i in range(len(tabla.tabla)):
                if tabla.tabla[i][0] == no_terminal and tabla.tabla[i][1] == terminal:
                    return tabla.tabla[i][2]  # retorno la celda


        def agregar_pila(produccion):
            for elemento in reversed(produccion):
                if elemento != "vacia":  # la vacía no la inserta
                    stack.append(elemento)

        miParser()

        time.sleep(120)

    except keyboard_interrupt:
        # Maneja la interrupción del teclado (Ctrl+C) para salir del bucle
        print("\n¡Programa detenido por el usuario!")
        break
