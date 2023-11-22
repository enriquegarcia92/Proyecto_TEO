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

N: Conjunto de símbolos no terminales
   N = {S, D, U, X, V, W, Z, B, Q, M, C, F, CO, I, P, IM, R, FIN}

Σ: Conjunto de símbolos terminales
   Σ = {'preprocessor_directive', 'int', 'keyword', 'identificador', 'LPAREN', 'RPAREN',
        'inicioBloque', 'finBloque', 'PLUS', 'greater_than', 'cadena', 'coma', 'NUMBER',
        'asignacion', 'single_quote', 'float', 'dot', 'comentario', 'eof'}

P: Conjunto de reglas de producción
   P es la tabla proporcionada en el código

S: Símbolo inicial
   S = 0

S → preprocessor_directive D
D → int identificador LPAREN int identificador coma int identificador RPAREN inicioBloque U finBloque X
U → keyword identificador PLUS identificador finInstruccion
X → keyword identificador LPAREN int identificador coma int identificador RPAREN inicioBloque V finBloque V
V → keyword LPAREN identificador greater_than identificador RPAREN inicioBloque W finBloque Z finBloque Q
W → identificador LPAREN cadena coma identificador coma identificador RPAREN finInstruccion
Z → keyword inicioBloque B finBloque
B → identificador LPAREN cadena coma identificador coma identificador RPAREN finInstruccion
Q → int identificador LPAREN RPAREN inicioBloque M C F CO I P CO IM R FIN
M → int identificador asignacion NUMBER finInstruccion
C → keyword identificador asignacion single_quote identificador single_quote finInstruccion
F → float identificador asignacion NUMBER dot NUMBER finInstruccion
CO → comentario
I → int identificador asignacion identificador LPAREN identificador coma NUMBER RPAREN finInstruccion
P → identificador LPAREN cadena coma identificador RPAREN finInstruccion
IM → identificador LPAREN NUMBER coma identificador RPAREN finInstruccion
R → keyword NUMBER finInstruccion
FIN → finBloque eof

Conjuntos First

First(S) = {preprocessor_directive}
First(D) = {int}
First(U) = {keyword}
First(X) = {keyword}
First(V) = {keyword}
First(W) = {identificador}
First(Z) = {keyword}
First(B) = {identificador}
First(Q) = {int}
First(M) = {int}
First(C) = {keyword}
First(F) = {float}
First(CO) = {comentario}
First(I) = {int}
First(P) = {identificador}
First(IM) = {identificador}
First(R) = {keyword}
First(FIN) = {finBloque}

Conjuntos Follow

Follow(S) = {eof}
Follow(D) = {eof}
Follow(U) = {finBloque}
Follow(X) = {finBloque}
Follow(V) = {finBloque}
Follow(W) = {finBloque}
Follow(Z) = {finBloque}
Follow(B) = {finBloque}
Follow(Q) = {finBloque}
Follow(M) = {int, keyword, identificador, finBloque}
Follow(C) = {int, keyword, identificador, finBloque}
Follow(F) = {int, keyword, identificador, finBloque}
Follow(CO) = {int, keyword, identificador, float, comentario, finBloque}
Follow(I) = {int, keyword, identificador, finBloque}
Follow(P) = {int, keyword, identificador, finBloque}
Follow(IM) = {int, keyword, identificador, finBloque}
Follow(R) = {int, keyword, identificador, finBloque}
Follow(FIN) = {eof}

Tabla LL1

+--------------------------+--------------------------------------------------------------------------------------------+
| No terminal / Terminal   | preprocessor_directive | int       | keyword   | identificador | LPAREN | RPAREN | inicioBloque | finBloque | PLUS | greater_than | cadena | coma | NUMBER | asignacion | single_quote | float    | dot  | comentario | eof | finInstruccion |
+--------------------------+--------------------------------------------------------------------------------------------+
| S                        | S -> preprocessor_directive D                                                         |                                                      |
| D                        | D -> int identificador LPAREN int identificador coma int identificador RPAREN inicioBloque U finBloque X |                                                      |
| U                        | U -> keyword identificador PLUS identificador finInstruccion                                |                                                      |
| X                        | X -> keyword identificador LPAREN int identificador coma int identificador RPAREN inicioBloque V finBloque V |                                                      |
| V                        | V -> keyword LPAREN identificador greater_than identificador RPAREN inicioBloque W finBloque Z finBloque Q |                                                      |
| W                        | W -> identificador LPAREN cadena coma identificador coma identificador RPAREN finInstruccion |                                                      |
| Z                        | Z -> keyword inicioBloque B finBloque                                                        |                                                      |
| B                        | B -> identificador LPAREN cadena coma identificador coma identificador RPAREN finInstruccion |                                                      |
| Q                        | Q -> int identificador LPAREN RPAREN inicioBloque M C F CO I P CO IM R FIN                    |                                                      |
| M                        | M -> int identificador asignacion NUMBER finInstruccion                                    |                                                      |
| C                        | C -> keyword identificador asignacion single_quote identificador single_quote finInstruccion |                                                      |
| F                        | F -> float identificador asignacion NUMBER dot NUMBER finInstruccion                        |                                                      |
| CO                       | CO -> comentario                                                                         |                                                      |
| I                        | I -> int identificador asignacion identificador LPAREN identificador coma NUMBER RPAREN finInstruccion |                                                      |
| P                        | P -> identificador LPAREN cadena coma identificador RPAREN finInstruccion                      |                                                      |
| IM                       | IM -> identificador LPAREN NUMBER coma identificador RPAREN finInstruccion                  |                                                      |
| R                        | R -> keyword NUMBER finInstruccion                                                         |                                                      |
| FIN                      | FIN -> finBloque eof                                                                      |                                                      |
+--------------------------+--------------------------------------------------------------------------------------------+
