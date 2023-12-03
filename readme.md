Sub set de C por analizar:

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

Gramática formal

G = (N, Σ, P, S)

# Conjunto de No Terminales (N)
no_terminales = ['S', 'LIB', 'LIB2', 'LIBEND', 'PARAM', 'ADDPARAM', 'NUMRETURN', 'ARITMETIC', 
                 'SUMA2', 'RETURNNUM', 'GHANDLER', 'CHARFRETURN', 'RETURNCHAR', 'FLOATN', 
                 'DECIMAL', 'THANDLER', 'OPENNUMFUN', 'OPENCHARFUN', 'OPENVOID', 'FBODY', 
                 'VOIDRETURN', 'RETURNVOID', 'CONDITIONSHANDLER', 'LOGICSIMBOLS', 'NOTHANDLER', 
                 'ELSEXTENTION', 'PRINTCONT', 'FUNCUSE', 'USEPARAM']

# Conjunto de Terminales (Σ)
terminales = ['hashtoken', 'int', 'char', 'float', 'keyword', 'comentario', 'identificador', 
              'LPAREN', 'RPAREN', 'asignacion', 'coma', 'finInstruccion', 'inicioBloque', 
              'finBloque', 'else', 'printf', 'aumentarvar', 'reducirvar', 'single_quote', 
              'and', 'or', 'lesser_than', 'greater_than', 'not', 'NUMBER', 'dot', 'eof', 'cadena']



S: Símbolo inicial
   S = 0

P: Conjunto de reglas de producción

La gramática descrita en el formato S->alfa es la siguiente:

1. S -> hashtoken identificador lesser_than LIB
2. S -> int identificador OPENNUMFUN S
3. S -> char identificador OPENCHARFUN S
4. S -> float identificador OPENNUMFUN S
5. S -> keyword identificador OPENVOID S
6. S -> comentario S
7. S -> identificador LPAREN USEPARAM RPAREN finInstruccion S
8. OPENVOID -> LPAREN PARAM FBODY VOIDRETURN finBloque
9. OPENNUMFUN -> asignacion RETURNNUM S
10. OPENNUMFUN -> LPAREN PARAM FBODY NUMRETURN finBloque
11. FBODY -> comentario FBODY
12. FBODY -> int identificador asignacion RETURNNUM FBODY
13. FBODY -> float identificador asignacion RETURNNUM FBODY
14. FBODY -> char identificador asignacion RETURNCHAR FBODY
15. FBODY -> identificador LPAREN USEPARAM RPAREN finInstruccion FBODY
16. FBODY -> if LPAREN CONDITIONSHANDLER RPAREN inicioBloque FBODY finBloque FBODY
17. FBODY -> while LPAREN CONDITIONSHANDLER RPAREN inicioBloque FBODY finBloque FBODY
18. FBODY -> else ELSEXTENTION
19. FBODY -> printf LPAREN PRINTCONT RPAREN finInstruccion FBODY
20. FBODY -> aumentarvar finInstruccion FBODY
21. FBODY -> reducirvar finInstruccion FBODY
22. FBODY -> keyword
23. FBODY -> finBloque
24. PRINTCONT -> cadena THANDLER PRINTCONT
25. PRINTCONT -> identificador THANDLER PRINTCONT
26. PRINTCONT -> NUMBER THANDLER PRINTCONT
27. PRINTCONT -> coma PRINTCONT PRINTCONT
28. PRINTCONT -> RPAREN
29. ELSEXTENTION -> inicioBloque FBODY finBloque FBODY
30. ELSEXTENTION -> if FBODY
31. CONDITIONSHANDLER -> identificador THANDLER LOGICSIMBOLS
32. CONDITIONSHANDLER -> NUMBER THANDLER LOGICSIMBOLS
33. CONDITIONSHANDLER -> not NOTHANDLER LOGICSIMBOLS
34. LOGICSIMBOLS -> and NOTHANDLER LOGICSIMBOLS
35. LOGICSIMBOLS -> or NOTHANDLER LOGICSIMBOLS
36. LOGICSIMBOLS -> lesser_than NOTHANDLER LOGICSIMBOLS
37. LOGICSIMBOLS -> greater_than NOTHANDLER LOGICSIMBOLS
38. LOGICSIMBOLS -> not NOTHANDLER LOGICSIMBOLS
39. LOGICSIMBOLS -> RPAREN
40. NOTHANDLER -> not THANDLER
41. NOTHANDLER -> identificador THANDLER
42. NOTHANDLER -> NUMBER THANDLER
43. OPENCHARFUN -> asignacion RETURNCHAR S
44. OPENCHARFUN -> LPAREN PARAM CHARFRETURN finBloque
45. VOIDRETURN -> keyword RETURNVOID
46. VOIDRETURN -> finBloque
47. CHARFRETURN -> keyword RETURNCHAR
48. NUMRETURN -> keyword RETURNNUM
49. RETURNVOID -> single_quote identificador single_quote finInstruccion
50. RETURNVOID -> identificador ARITMETIC
51. RETURNVOID -> LPAREN THANDLER ARITMETIC
52. RETURNVOID -> NUMBER FLOATN ARITMETIC
53. RETURNVOID -> finBloque
54. RETURNCHAR -> single_quote identificador single_quote finInstruccion
55. RETURNCHAR -> identificador finInstruccion
56. RETURNCHAR -> LPAREN char RPAREN identificador finInstruccion
57. RETURNNUM -> identificador ARITMETIC
58. RETURNNUM -> LPAREN THANDLER ARITMETIC
59. RETURNNUM -> NUMBER FLOATN ARITMETIC
60. ARITMETIC -> LPAREN THANDLER ARITMETIC
61. ARITMETIC -> RPAREN ARITMETIC
62. ARITMETIC -> PLUS GHANDLER ARITMETIC
63. ARITMETIC -> MINUS GHANDLER ARITMETIC
64. ARITMETIC -> TIMES GHANDLER ARITMETIC
65. ARITMETIC -> DIVIDE GHANDLER ARITMETIC
66. ARITMETIC -> coma THANDLER ARITMETIC
67. ARITMETIC -> finInstruccion
68. GHANDLER -> identificador
69. GHANDLER -> LPAREN THANDLER
70. GHANDLER -> NUMBER FLOATN
71. THANDLER -> identificador
72. THANDLER -> NUMBER FLOATN
73. THANDLER -> cadena
74. PARAM -> int identificador PARAM
75. PARAM -> char identificador PARAM
76. PARAM -> float identificador PARAM
77. PARAM -> RPAREN inicioBloque
78. PARAM -> coma PARAM
79. USEPARAM -> identificador USEPARAM
80. USEPARAM -> NUMBER FLOATN USEPARAM
81. USEPARAM -> single_quote identificador single_quote USEPARAM
82. USEPARAM -> coma USEPARAM
83. USEPARAM -> RPAREN
84. LIB -> identificador LIB2
85. LIB2 -> greater_than S
86. LIB2 -> dot identificador greater

_than S
87. FLOATN -> NUMBER DECIMAL
88. DECIMAL -> dot NUMBER
89. DECIMAL -> MINUS
90. DECIMAL -> PLUS
91. DECIMAL -> TIMES
92. DECIMAL -> DIVIDE
93. DECIMAL -> RPAREN
94. DECIMAL -> finInstruccion
95. DECIMAL -> coma
96. S -> eof


Conjuntos First

FIRST(S) = {'hashtoken', 'int', 'char', 'float', 'keyword', 'comentario', 'identificador', 'printf', 'aumentarvar', 'reducirvar', 'single_quote', 'and', 'or', 'lesser_than', 'greater_than', 'not', 'NUMBER', 'dot', 'eof', 'cadena', 'else', 'while', 'LPAREN', 'RPAREN', 'finInstruccion', 'inicioBloque', 'finBloque'}

FIRST(LIB) = {'identificador'}

FIRST(LIB2) = {'greater_than', 'dot'}

FIRST(LIBEND) = {}

FIRST(PARAM) = {'int', 'char', 'float', 'RPAREN'}

FIRST(ADDPARAM) = {'int', 'char', 'float', 'RPAREN'}

FIRST(NUMRETURN) = {'int', 'char', 'float', 'RPAREN'}

FIRST(ARITMETIC) = {'LPAREN', 'RPAREN', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'coma', 'finInstruccion'}

FIRST(SUMA2) = {'PLUS', 'MINUS'}

FIRST(RETURNNUM) = {'identificador', 'LPAREN', 'NUMBER'}

FIRST(GHANDLER) = {'identificador', 'LPAREN', 'NUMBER', 'finInstruccion', 'RPAREN'}

FIRST(CHARFRETURN) = {'char', 'single_quote', 'identificador', 'finInstruccion'}

FIRST(RETURNCHAR) = {'single_quote', 'identificador', 'LPAREN'}

FIRST(FLOATN) = {'NUMBER'}

FIRST(DECIMAL) = {'dot', 'MINUS', 'PLUS', 'TIMES', 'DIVIDE', 'RPAREN', 'finInstruccion', 'coma'}

FIRST(THANDLER) = {'identificador', 'NUMBER', 'cadena'}

FIRST(OPENNUMFUN) = {'asignacion', 'LPAREN'}

FIRST(OPENCHARFUN) = {'asignacion', 'LPAREN'}

FIRST(OPENVOID) = {'asignacion', 'LPAREN'}

FIRST(FBODY) = {'comentario', 'int', 'float', 'char', 'identificador', 'if', 'while', 'else', 'printf', 'aumentarvar', 'reducirvar', 'keyword', 'finBloque', 'finInstruccion'}

FIRST(VOIDRETURN) = {'single_quote', 'identificador', 'LPAREN', 'finBloque', 'finInstruccion'}

FIRST(RETURNVOID) = {'single_quote', 'identificador', 'LPAREN', 'NUMBER', 'finBloque', 'finInstruccion'}

FIRST(CONDITIONSHANDLER) = {'identificador', 'NUMBER', 'not', 'RPAREN'}

FIRST(LOGICSIMBOLS) = {'and', 'or', 'lesser_than', 'greater_than', 'not', 'RPAREN'}

FIRST(NOTHANDLER) = {'not', 'identificador', 'NUMBER'}

FIRST(ELSEXTENTION) = {'inicioBloque', 'if'}

FIRST(PRINTCONT) = {'cadena', 'identificador', 'NUMBER', 'RPAREN'}

FIRST(FUNCUSE) = {'identificador', 'LPAREN'}

FIRST(USEPARAM) = {'identificador', 'NUMBER', 'single_quote', 'coma', 'RPAREN'}



Conjuntos Follow

FOLLOW(S) = {'eof'}

FOLLOW(LIB) = {'greater_than', 'dot', 'identificador', 'eof'}

FOLLOW(LIB2) = {'eof'}

FOLLOW(LIBEND) = {'eof'}

FOLLOW(PARAM) = {'RPAREN'}

FOLLOW(ADDPARAM) = {'RPAREN'}

FOLLOW(NUMRETURN) = {'finBloque'}

FOLLOW(ARITMETIC) = {'finInstruccion', 'RPAREN'}

FOLLOW(SUMA2) = {'finInstruccion', 'RPAREN'}

FOLLOW(RETURNNUM) = {'finInstruccion', 'RPAREN'}

FOLLOW(GHANDLER) = {'finInstruccion', 'RPAREN'}

FOLLOW(CHARFRETURN) = {'finInstruccion', 'RPAREN'}

FOLLOW(RETURNCHAR) = {'finInstruccion', 'RPAREN'}

FOLLOW(FLOATN) = {'PLUS', 'MINUS', 'RPAREN', 'finInstruccion', 'coma'}

FOLLOW(DECIMAL) = {'PLUS', 'MINUS', 'RPAREN', 'finInstruccion', 'coma'}

FOLLOW(THANDLER) = {'PLUS', 'MINUS', 'RPAREN', 'finInstruccion', 'coma'}

FOLLOW(OPENNUMFUN) = {'PLUS', 'MINUS', 'RPAREN', 'finInstruccion', 'coma'}

FOLLOW(OPENCHARFUN) = {'PLUS', 'MINUS', 'RPAREN', 'finInstruccion', 'coma'}

FOLLOW(OPENVOID) = {'PLUS', 'MINUS', 'RPAREN', 'finInstruccion', 'coma'}

FOLLOW(FBODY) = {'else', 'finBloque'}

FOLLOW(VOIDRETURN) = {'else', 'finBloque'}

FOLLOW(RETURNVOID) = {'else', 'finBloque'}

FOLLOW(CONDITIONSHANDLER) = {'RPAREN', 'and', 'or', 'lesser_than', 'greater_than', 'not', 'finInstruccion', 'finBloque', 'else', 'coma'}

FOLLOW(LOGICSIMBOLS) = {'identificador', 'NUMBER', 'not', 'RPAREN', 'and', 'or', 'lesser_than', 'greater_than', 'finInstruccion', 'else', 'coma'}

FOLLOW(NOTHANDLER) = {'identificador', 'NUMBER', 'RPAREN', 'and', 'or', 'lesser_than', 'greater_than', 'finInstruccion', 'else', 'coma'}

FOLLOW(ELSEXTENTION) = {'identificador', 'NUMBER', 'LPAREN', 'cadena', 'else', 'finBloque', 'RPAREN', 'and', 'or', 'lesser_than', 'greater_than', 'not', 'finInstruccion', 'coma'}

FOLLOW(PRINTCONT) = {'RPAREN', 'finInstruccion', 'coma'}

FOLLOW(FUNCUSE) = {'RPAREN', 'finInstruccion', 'coma'}

FOLLOW(USEPARAM) = {'RPAREN', 'finInstruccion', 'coma'}




Tabla LL1