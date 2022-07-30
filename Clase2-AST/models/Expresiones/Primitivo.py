from models.Expresiones.Expresion import Expresion
from models.TablaSimbolos.Tipos import definirTipo


class Primitivo(Expresion):

    def __init__(self, primitivo, linea: int, columna: int):
        self.primitivo = primitivo
        self.linea = linea
        self.columna = columna

    def getTipo(self, driver, ts):
        value = self.getValor(driver, ts)
        return definirTipo(value)

    def getValor(self, driver, ts):
        return self.primitivo

