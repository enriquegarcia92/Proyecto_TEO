import nonTerminal as nt

tabla = [
    [nt.S, "hashtoken", ["hashtoken", "identificador", "lesser_than", nt.LIB]],
    # Manejo de variables globales
    # Manejo de declaración de funciones
    [nt.S, "int", ["int", "identificador", nt.OPENNUMFUN, nt.S]],
    [nt.S, "char", ["char", "identificador", nt.OPENCHARFUN, nt.S]],
    [nt.S, "float", ["float", "identificador", nt.OPENNUMFUN, nt.S]],
    [nt.S, "keyword", ["keyword", "identificador", nt.OPENVOID, nt.S]],
    [nt.S, "comentario", ["comentario", nt.S]],
    [
        nt.S,
        "identificador",
        ["identificador", "LPAREN", nt.USEPARAM, "RPAREN", "finInstruccion", nt.S],
    ],
    # Manejo de funcion void
    [nt.OPENVOID, "LPAREN", ["LPAREN", nt.PARAM, nt.FBODY, nt.VOIDRETURN, "finBloque"]],
    # Manejar global scope de numericas
    [nt.OPENNUMFUN, "asignacion", ["asignacion", nt.RETURNNUM, nt.S]],
    [
        nt.OPENNUMFUN,
        "LPAREN",
        ["LPAREN", nt.PARAM, nt.FBODY, nt.NUMRETURN, "finBloque"],
    ],
    [nt.OPENNUMFUN, "finInstruccion", ["finInstruccion", nt.S]],
    # Variables sin inicializar
    [nt.EMPTYVAR, "asignacion", ["asignacion"]],
    [nt.EMPTYVAR, "finInstrucción", ["finInstrucción", nt.FBODY]],
    # cuerpo de funciones int
    [nt.FBODY, "comentario", ["comentario", nt.FBODY]],
    [nt.FBODY, "int", ["int", "identificador", nt.EMPTYVAR, nt.RETURNNUM, nt.FBODY]],
    [
        nt.FBODY,
        "float",
        ["float", "identificador", nt.EMPTYVAR, nt.RETURNNUM, nt.FBODY],
    ],
    [nt.FBODY, "char", ["char", "identificador", nt.EMPTYVAR, nt.RETURNCHAR, nt.FBODY]],
    [
        nt.FBODY,
        "identificador",
        ["identificador", "LPAREN", nt.USEPARAM, "RPAREN", "finInstruccion", nt.FBODY],
    ],
    [
        nt.FBODY,
        "if",
        [
            "if",
            "LPAREN",
            nt.CONDITIONSHANDLER,
            "RPAREN",
            "inicioBloque",
            nt.FBODY,
            "finBloque",
            nt.FBODY,
        ],
    ],
    [
        nt.FBODY,
        "while",
        [
            "while",
            "LPAREN",
            nt.CONDITIONSHANDLER,
            "RPAREN",
            "inicioBloque",
            nt.FBODY,
            "finBloque",
            nt.FBODY,
        ],
    ],
    [nt.FBODY, "else", ["else", nt.ELSEXTENTION]],
    [
        nt.FBODY,
        "printf",
        ["printf", "LPAREN", nt.PRINTCONT, "RPAREN", "finInstruccion", nt.FBODY],
    ],
    [nt.FBODY, "aumentarvar", ["aumentarvar", "finInstruccion", nt.FBODY]],
    [nt.FBODY, "reducirvar", ["reducirvar", "finInstruccion", nt.FBODY]],
    [nt.FBODY, "keyword", []],
    [nt.FBODY, "finBloque", []],
    # Manejo de estrucutra print
    [nt.PRINTCONT, "cadena", [nt.THANDLER, nt.PRINTCONT]],
    [nt.PRINTCONT, "identificador", [nt.THANDLER, nt.PRINTCONT]],
    [nt.PRINTCONT, "NUMBER", [nt.THANDLER, nt.PRINTCONT]],
    [nt.PRINTCONT, "coma", ["coma", nt.PRINTCONT, nt.PRINTCONT]],
    [nt.PRINTCONT, "RPAREN", []],
    # Manejo de else
    [
        nt.ELSEXTENTION,
        "inicioBloque",
        ["inicioBloque", nt.FBODY, "finBloque", nt.FBODY],
    ],
    [nt.ELSEXTENTION, "if", [nt.FBODY]],
    # Manejo de condicionales de if
    [nt.CONDITIONSHANDLER, "identificador", [nt.THANDLER, nt.LOGICSIMBOLS]],
    [nt.CONDITIONSHANDLER, "NUMBER", [nt.THANDLER, nt.LOGICSIMBOLS]],
    [nt.CONDITIONSHANDLER, "not", ["not", nt.THANDLER, nt.LOGICSIMBOLS]],
    # Simbolos de if
    [nt.LOGICSIMBOLS, "and", ["and", nt.NOTHANDLER, nt.LOGICSIMBOLS]],
    [nt.LOGICSIMBOLS, "or", ["or", nt.NOTHANDLER, nt.LOGICSIMBOLS]],
    [nt.LOGICSIMBOLS, "lesser_than", ["lesser_than", nt.NOTHANDLER, nt.LOGICSIMBOLS]],
    [nt.LOGICSIMBOLS, "greater_than", ["greater_than", nt.NOTHANDLER, nt.LOGICSIMBOLS]],
    [nt.LOGICSIMBOLS, "not", ["not", nt.NOTHANDLER, nt.LOGICSIMBOLS]],
    [nt.LOGICSIMBOLS, "RPAREN", []],
    # Manejo de uso de not
    [nt.NOTHANDLER, "not", ["not", nt.THANDLER]],
    [nt.NOTHANDLER, "identificador", [nt.THANDLER]],
    [nt.NOTHANDLER, "NUMBER", [nt.THANDLER]],
    # Manejar global scope de char
    [nt.OPENCHARFUN, "asignacion", ["asignacion", nt.RETURNCHAR, nt.S]],
    [nt.OPENCHARFUN, "LPAREN", ["LPAREN", nt.PARAM, nt.CHARFRETURN, "finBloque"]],
    [nt.OPENNUMFUN, "finInstruccion", ["finInstruccion", nt.S]],
    # Manejo de retornos de funcion char
    [nt.VOIDRETURN, "keyword", ["keyword", nt.RETURNVOID]],
    [nt.VOIDRETURN, "finBloque", []],
    [nt.CHARFRETURN, "keyword", ["keyword", nt.RETURNCHAR]],
    # Manejo de retornos de funcion int
    [nt.NUMRETURN, "keyword", ["keyword", nt.RETURNNUM]],
    # Manejo de retorno de void
    [
        nt.RETURNVOID,
        "single_quote",
        ["single_quote", "identificador", "single_quote", "finInstruccion"],
    ],
    [nt.RETURNVOID, "identificador", ["identificador", nt.ARITMETIC]],
    [nt.RETURNVOID, "LPAREN", ["LPAREN", nt.THANDLER, nt.ARITMETIC]],
    [nt.RETURNVOID, "NUMBER", [nt.FLOATN, nt.ARITMETIC]],
    [nt.RETURNVOID, "finBloque", []],
    # Manejo de retorno para funciones char
    [
        nt.RETURNCHAR,
        "single_quote",
        ["single_quote", "identificador", "single_quote", "finInstruccion"],
    ],
    [nt.RETURNCHAR, "identificador", ["identificador", "finInstruccion"]],
    [
        nt.RETURNCHAR,
        "LPAREN",
        ["LPAREN", "char", "RPAREN", "identificador", "finInstruccion"],
    ],
    # Manejo de retornos para funciones INT
    [nt.RETURNNUM, "identificador", ["identificador", nt.ARITMETIC]],
    [nt.RETURNNUM, "LPAREN", ["LPAREN", nt.THANDLER, nt.ARITMETIC]],
    [nt.RETURNNUM, "NUMBER", [nt.FLOATN, nt.ARITMETIC]],
    # Manejo de operaciones aritmeticas basicas
    [nt.ARITMETIC, "LPAREN", ["LPAREN", nt.THANDLER, nt.ARITMETIC]],
    [nt.ARITMETIC, "RPAREN", ["RPAREN", nt.ARITMETIC]],
    [nt.ARITMETIC, "PLUS", ["PLUS", nt.GHANDLER, nt.ARITMETIC]],
    [nt.ARITMETIC, "MINUS", ["MINUS", nt.GHANDLER, nt.ARITMETIC]],
    [nt.ARITMETIC, "TIMES", ["TIMES", nt.GHANDLER, nt.ARITMETIC]],
    [nt.ARITMETIC, "DIVIDE", ["DIVIDE", nt.GHANDLER, nt.ARITMETIC]],
    [nt.ARITMETIC, "coma", ["coma", nt.THANDLER, nt.ARITMETIC]],
    [nt.ARITMETIC, "finInstruccion", ["finInstruccion"]],
    # Manejador de parentesis en operacioens aritmeticas
    [nt.GHANDLER, "identificador", ["identificador"]],
    [nt.GHANDLER, "LPAREN", ["LPAREN", nt.THANDLER]],
    [nt.GHANDLER, "NUMBER", [nt.FLOATN]],
    # Manejador de tipo de variable
    [nt.THANDLER, "identificador", ["identificador"]],
    [nt.THANDLER, "NUMBER", [nt.FLOATN]],
    [nt.THANDLER, "cadena", ["cadena"]],
    # Cadenas para manejar parametros en funciones
    [nt.PARAM, "int", ["int", "identificador", nt.PARAM]],
    [nt.PARAM, "char", ["char", "identificador", nt.PARAM]],
    [nt.PARAM, "float", ["float", "identificador", nt.PARAM]],
    [nt.PARAM, "RPAREN", ["RPAREN", "inicioBloque"]],
    [nt.PARAM, "coma", ["coma", nt.PARAM]],
    # Manejar uso de parametros en funciones
    [nt.USEPARAM, "identificador", ["identificador", nt.USEPARAM]],
    [nt.USEPARAM, "NUMBER", [nt.FLOATN, nt.USEPARAM]],
    [
        nt.USEPARAM,
        "single_quote",
        ["single_quote", "identificador", "single_quote", nt.USEPARAM],
    ],
    [nt.USEPARAM, "coma", ["coma", nt.USEPARAM]],
    [nt.USEPARAM, "RPAREN", []],
    # Cadenas para leer los dos tipos de liberías de C
    [nt.LIB, "identificador", ["identificador", nt.LIB2]],
    [nt.LIB2, "greater_than", ["greater_than", nt.S]],
    [nt.LIB2, "dot", ["dot", "identificador", "greater_than", nt.S]],
    # Auxiliaries
    [nt.FLOATN, "NUMBER", ["NUMBER", nt.DECIMAL]],
    [nt.DECIMAL, "dot", ["dot", "NUMBER"]],
    [nt.DECIMAL, "MINUS", []],
    [nt.DECIMAL, "PLUS", []],
    [nt.DECIMAL, "TIMES", []],
    [nt.DECIMAL, "DIVIDE", []],
    [nt.DECIMAL, "RPAREN", []],
    [nt.DECIMAL, "finInstruccion", []],
    [nt.DECIMAL, "coma", []],
    # Cadena de fin de archivo
    [nt.S, "eof", ["eof"]],
]
