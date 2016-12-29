#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2016, Cristian García <cristian99garcia@gmail.com>
#
# This library is free software you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation either
# version 3 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

import re
import math

from constants import Re
from constants import Set

from utils import sgn
from utils import is_number
from utils import ignore_values
from utils import get_priority
from utils import calculate_math_expression


def char_at(string, index):
    if len(string) > index:
        return string[index]
    else:
        return ""


class MathSintaxError(ArithmeticError):

     def __init__(self, message):
        super(MathSintaxError, self).__init__(message)


class Stack(list):

     def __init__(self):
        list.__init__(self)

     def empty(self):
         return len(self) == 0

     def push(self, item):
         self.append(item)

     def peek(self):
         return self[-1]

     def size(self):
         return len(self)


class FunctionType:
    NULL          = 0
    CONSTANT      = 1  # x + a = 0
    LINEAL        = 2  # ax + b = 0
    QUADRATIC     = 3  # ax^2 + bx + c = 0
    CUBIC         = 4  # ax^3 + bx^2 + cx + d = 0
    POLINOMIC     = 5  # ax^n + bx^n-1 + ... = 0
    EXPONENTIAL   = 6  # a^x + b = 0
    RACIONAL      = 7  # (ax + b) / (cx + d) = 0
    LOGARITHMIC   = 8  # 
    TRIGONOMETRIC = 9  # cos/sin/tan (ax) + b = 0


class Function(object):

    def __init__(self, formula):
        self.name = "F"
        self.variable = "x"
        self.formula = formula

        self.guess_type()

    @classmethod
    def new_with_type(self, formula, type):
        self.name = "F"
        self.formula = formula
        self.type = type

    def get_y(self, x):
        expression = self.formula.replace("x", str(float(x)))
        return calculate_math_expression(expression)

    def guess_type(self):
        string = self.formula.replace(" ", "").replace("^", "**").replace(",", ".").lower()

        if re.compile(Re.CONSTANT).match(string):
            self.type = FunctionType.CONSTANT

        elif "x" in string and not re.compile("[+-]?[x][\\^][-+]?(\\d+)*(.(\\d+))?").match(string) and not re.compile("(?:sec|tan|cos)").match(string) and not "^x" in string:
            self.type = FunctionType.LINEAL

        elif re.compile(Re.RACIONAL).match(string):
            self.type = FunctionType.RACIONAL

        elif re.compile(Re.QUADRATIC).match(string) and not re.compile("[+-]?[x][\\^][3-9]").match(string):
            self.type = FunctionType.QUADRATIC

        elif re.compile(Re.CUBIC).match(string) and not re.compile("[+-]?[x][\\^][4-9]").match(string):
            self.type = FunctionType.CUBIC

        elif re.compile(Re.POLINOMIC).match(string):
            self.type = FunctionType.POLINOMIC

        elif re.compile(Re.EXPONENTIAL).match(string):
            self.type = FunctionType.EXPONENTIAL

        elif re.compile(Re.TRIGONOMETRIC).match(string):
            self.type = FunctionType.TRIGONOMETRIC

    def get_type(self):
        return self.type

    def get_domain(self):
        if self.type == FunctionType.CONSTANT:
            return Set.REALS

        elif self.type == FunctionType.LINEAL:
            return Set.REALS

        elif self.type == FunctionType.QUADRATIC:
            return Set.REALS

        elif self.type == FunctionType.CUBIC:
            return Set.REALS

        elif self.type == FunctionType.POLINOMIC:
            return Set.REALS

        elif self.type == FunctionType.EXPONENTIAL:
            return Set.REALS

        elif self.type == FunctionType.RACIONAL:
            # TODO: No son todos los reales, hay que sacar los problemas de existencia
            return Set.REALS

        elif self.type == FunctionType.LOGARITMIC:
            # TODO: No son todos los reales, solo los valores que hagan que la expresión dentro del logarítmo sea mayor que cero
            return Set.REALS

        elif self.type == FunctionType.TRIGONOMETRIC:
            # TODO: No siempre son todos los reales, depende del type de función:
            # sen: R
            # cos: R
            # tan: R - { (2k + 1) * pi/2 k e Z }
            # cot: R - { k*pi k e Z }
            # sec: R - { (2k + 1) * pi/2 k e Z }
            return Set.REALS

        else:
            return Set.EMPTY

    def get_recorrido(self):  # TODO: Translate
        if self.type == FunctionType.CONSTANT:
            return str(self.get_y(0))

        elif self.type == FunctionType.LINEAL:
            return Set.REALS

        elif self.type == FunctionType.QUADRATIC:
            # Si a > 0:
            # Recorrido = [VY, infinito)
            # Si a < 0:
            # Recorrido = (-infinito, VY]
            return Set.REALS

        elif self.type == FunctionType.CUBIC:
            return Set.REALS

        elif self.type == FunctionType.POLINOMIC:
            # Solo si el máximo exponente es impar
            return Set.REALS

        elif self.type == FunctionType.EXPONENTIAL:
            # Si b >= 0
            # R+
            # Si b < 0
            # R+ + (b, 0]
            return Set.REALS

        elif self.type == FunctionType.RACIONAL:
            # TODO: buscar asíntota horizontal
            return Set.REALS

        elif self.type == FunctionType.LOGARITMIC:
            return Set.REALS

        elif self.type == FunctionType.TRIGONOMETRIC:
            # TODO: Estudiar más en profundidad
            return Set.REALS

        else:
            return Set.EMPTY


import sys
expr = "3 + 2"

if len(sys.argv) == 2:
    expr = sys.argv[1]

f = Function(expr)
print f.type