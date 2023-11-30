#include <stdio.h>
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

        $