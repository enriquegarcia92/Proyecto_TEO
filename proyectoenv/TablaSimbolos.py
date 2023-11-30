# Clase para la tabla de símbolos
class TablaSimbolos:
    def __init__(self):
        self.simbolos = {}

    def insertar(self, identificador, tipo, valor, linea, ambito):
        if identificador not in self.simbolos:
            self.simbolos[identificador] = {'tipo': tipo, 'valor': valor, 'linea': linea, 'ambito': ambito}
    def buscar(self, identificador):
        return self.simbolos.get(identificador, None)

    def actualizar(self, identificador, valor):
        if identificador in self.simbolos:
            self.simbolos[identificador]['valor'] = valor

    def eliminar(self, identificador):
        if identificador in self.simbolos:
            del self.simbolos[identificador]

    def imprimir_tabla(self):
        print("\nTabla de Símbolos:")
        print("{:<15} | {:<10} | {:<10} | {:<10} | {:<10}".format("Identificador", "Tipo", "Valor", "Línea", "Ámbito"))
        print("------------------------------------------------------")
        for identificador, info in self.simbolos.items():
            tipo = info['tipo']
            valor = info['valor']
            linea = info['linea']
            ambito_nivel = info['ambito']
            ambito = 'global' if ambito_nivel == 0 else ('metodo/funcion' if ambito_nivel == 1 else 'instruccion')
            print("{:<15} | {:<10} | {:<10} | {:<10} | {:<10}".format(identificador, tipo, valor, linea, ambito))
