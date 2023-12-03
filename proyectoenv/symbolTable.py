import shutil


# Clase para la tabla de símbolos
class TablaSimbolos:
    def __init__(self):
        self.simbolos = {}

    def insertar(self, identificador, tipo, valor, linea, ambito):
        if identificador not in self.simbolos:
            self.simbolos[identificador] = {
                "tipo": tipo,
                "valor": valor,
                "linea": linea,
                "ambito": ambito,
            }

    def buscar(self, identificador):
        return self.simbolos.get(identificador, None)

    def actualizar(self, identificador, valor):
        if identificador in self.simbolos:
            self.simbolos[identificador]["valor"] = valor

    def eliminar(self, identificador):
        if identificador in self.simbolos:
            del self.simbolos[identificador]

    def imprimir_tabla(self):
        terminal_width = shutil.get_terminal_size().columns
        print("\nTabla de Símbolos:")

        # Distribuir el ancho uniformemente entre las columnas
        column_width = terminal_width // 5

        header = "{:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}}".format(
            "Identificador",
            column_width,
            "Tipo",
            column_width,
            "Valor",
            column_width,
            "Línea",
            column_width,
            "Ámbito",
            column_width,
        )
        separator = "-" * (column_width * 6)

        print(header)
        print(separator)

        for identificador, info in self.simbolos.items():
            tipo = info["tipo"]
            valor = info["valor"]
            linea = info["linea"]
            ambito_nivel = info["ambito"]
            ambito = (
                "global"
                if ambito_nivel == 0
                else ("metodo/funcion" if ambito_nivel == 1 else "instruccion")
            )

            row = "{:<{}} | {:<{}} | {:<{}} | {:<{}} | {:<{}}".format(
                identificador,
                column_width,
                tipo,
                column_width,
                valor,
                column_width,
                linea,
                column_width,
                ambito,
                column_width,
            )
            print(row)
