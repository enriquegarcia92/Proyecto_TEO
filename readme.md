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

S -> preprocessor_directive F
F -> int identificador LPAREN V coma V RPAREN inicioBloque R finBloque FV
V -> int identificador
R -> keyword SUM finInstruccion
SUM -> identificador PLUS identificador
FV -> keyword identificador LPAREN V coma V RPAREN inicioBloque IF finBloque M
IF -> keyword LPAREN C RPAREN inicioBloque P finBloque E
C -> identificador greater_than identificador
P -> identificador LPAREN cadena coma identificador coma identificador RPAREN finInstruccion
E -> keyword inicioBloque P finBloque
M -> int identificador LPAREN RPAREN inicioBloque VA VC VF COM VS P2 COM FI COM VA W RET finBloque
VA -> int identificador asignacion NUMBER finInstruccion
VC -> keyword identificador asignacion single_quote identificador single_quote finInstruccion
VF -> float identificador asignacion NUMBER dot NUMBER finInstruccion
VS -> int identificador asignacion identificador LPAREN identificador coma NUMBER RPAREN finInstruccion
P2 -> identificador LPAREN cadena coma identificador RPAREN finInstruccion
FI -> identificador LPAREN NUMBER coma identificador RPAREN finInstruccion
W -> keyword LPAREN C2 RPAREN inicioBloque P2 WC finBloque
WC -> identificador PLUS PLUS
C2 -> identificador lesser_than NUMBER
COM -> comentario
RET -> keyword NUMBER finInstruccion
FIN -> finBloque eof


Conjuntos First

FIRST(S) = {preprocessor_directive}
FIRST(F) = {int}
FIRST(V) = {int}
FIRST(R) = {keyword}
FIRST(SUM) = {identificador}
FIRST(FV) = {keyword}
FIRST(IF) = {keyword}
FIRST(C) = {identificador}
FIRST(P) = {identificador}
FIRST(E) = {keyword}
FIRST(M) = {int}
FIRST(VA) = {int}
FIRST(VC) = {keyword}
FIRST(VF) = {float}
FIRST(VS) = {int}
FIRST(P2) = {identificador}
FIRST(FI) = {identificador}
FIRST(W) = {keyword}
FIRST(WC) = {identificador}
FIRST(C2) = {identificador}
FIRST(COM) = {comentario}
FIRST(RET) = {keyword}
FIRST(FIN) = {finBloque}

Conjuntos Follow

FOLLOW(S) = {eof}
FOLLOW(F) = {intBloque, eof}
FOLLOW(V) = {RPAREN}
FOLLOW(R) = {intBloque, eof}
FOLLOW(SUM) = {finInstruccion}
FOLLOW(FV) = {intBloque, eof}
FOLLOW(IF) = {finInstruccion}
FOLLOW(C) = {RPAREN}
FOLLOW(P) = {finInstruccion}
FOLLOW(E) = {intBloque, eof}
FOLLOW(M) = {eof}
FOLLOW(VA) = {finInstruccion}
FOLLOW(VC) = {finInstruccion}
FOLLOW(VF) = {finInstruccion}
FOLLOW(VS) = {finInstruccion}
FOLLOW(P2) = {finInstruccion}
FOLLOW(FI) = {finInstruccion}
FOLLOW(W) = {finBloque}
FOLLOW(WC) = {finBloque}
FOLLOW(C2) = {RPAREN}
FOLLOW(COM) = {intBloque, eof}
FOLLOW(RET) = {finBloque}
FOLLOW(FIN) = {eof}


Tabla LL1