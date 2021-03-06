import math
from .Function import Function

class FixedPoint:

    def __init__(self):
        self.values = []

    def evaluate(self, xi, tolerancia, iter, function, g_function, type_error=1):

        fun = Function(function)
        gx = Function(g_function)

        fx = fun.evaluate2(xi)

        if fx == 0:
            return f"{xi} es raiz"
        if iter < 1:
            return "El valor del iterador es incorrecto"
        if tolerancia < 0:
            return "Error en la tolerancia, debe ser mayor o igual a 0"

        self.values.append([0, str(xi), str("{:.2e}".format(fx)), None])
        contador = 0
        error = tolerancia + 0.1
        while fx != 0 and error > tolerancia and contador < iter:
            xn = gx.evaluate2(xi)
            fi = fun.evaluate2(xn)

            if type_error == 0:
                error = abs(xn-xi)
            else:
                error = abs((xn-xi)/xn)

            xi = xn

            contador = contador + 1
            self.values.append([contador, str(xn), str(
                "{:.2e}".format(fi)), str("{:.2e}".format(error))])

        if fx == 0:
            return f"{xi} es raiz"
        elif error < tolerancia:
            return f"{xi} es una aprox. con una tolerancia = {tolerancia}"
        else:
            return f"El método fracasó en {iter} iteraciones"

    def tabla_values(self):
        return self.values
