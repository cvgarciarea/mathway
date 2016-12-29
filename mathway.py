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
from constants import FunctionType

from utils import clear_float
from utils import get_function_type_name
from utils import calculate_math_expression

from value_getter import ValueGetter


class FunctionTypeError(ArithmeticError):

     def __init__(self, message):
        super(FunctionTypeError, self).__init__(message)


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

def raise_function_type_error(function, ftype):
    message = "%s %s %s %s" % (function.formula,
                              _("isn't a"),
                              get_function_type_name(ftype),
                              _("polunomial."))

    raise FunctionTypeError(message)


class Equation(object):

    def __init__(self, function, ftype):
        if function.type != ftype:
            raise_function_type_error(function, ftype)

        """
        function = 0
        """

        self.function = function

    @classmethod
    def new_from_string(self, formula):
        raise NotImplementedError(_("You must replace 'new_from_string'"))

    @classmethod
    def new_from_two_members(self, member1, member2):
        """
        member1 = member2
        member1 - member2 = 0
        """

        raise NotImplementedError(_("You must replace 'new_from_two_members"))

    def solve(self):
        raise NotImplementedError(_("You must replace 'solve'"))

    def solve_step_by_step(self):
        raise NotImplementedError(_("You must replace 'solve_step_by_step'"))

    def get_expression(self):
        return self.function.formula + " = 0"


class FirstDegreeEquation(Equation):

    def __init__(self, function):
        Equation.__init__(self, function, FunctionType.LINEAL)

    @classmethod
    def new_from_string(self, formula):
        function = Function(formula)
        return FirstDegreeEquation(function)

    @classmethod
    def new_from_two_members(self, member1, member2):
        ftype = FunctionType.LINEAL
        if member1.type != ftype:
            raise_function_type_error(member1, ftype)

        if member2.type != ftype:
            raise_function_type_error(member2, ftype)

        formula = "%s - (%s)" % (member1.formula, member2.formula)
        function = Function(formula)
        return FirstDegreeEquation(function)

    def solve(self):
        solutions = []
        values = ValueGetter.lineal(self.function)
        a = values[0]
        b = values[1]

        if a == 0:
            solutions = []
        else:
            solutions = [b / (a * -1)]

        return solutions

    def solve_step_by_step(self):
        # ax + b = 0
        # ax = -b
        # x = -b / a

        steps = []
        step = ""
        values = ValueGetter.lineal(self.function)
        a = values[0]
        b = values[1]
        has_b = (b != 0)

        step += "%sx" % clear_float(a)

        if has_b:
            if b > 0:
                step += " +"

            step += " %s" % clear_float(b)

        step += " = 0"
        steps.append(step)
        step = ""

        # ax = -b
        if has_b:
            step = "%sx = %s" % (clear_float(a), clear_float(b * -1))
            steps.append(step)
            step = ""

        if has_b and b % (a * -1) == 0:
            steps.append("x = %s" % (clear_float(b / (a * -1))))
            step = "S = { %s }" % clear_float(b / (a * -1))
            steps.append(step)
        elif has_b and b % (a * -1) != 0:
            if (a < 0 and -b > 0) or (-b < 0 and a > 0):
                d = "-%s / %s" % (clear_float(abs(b)), clear_float(abs(a)))
            else:
                d = "%s / %s" % (clear_float(abs(b)), clear_float(abs(a)))

            steps.append("x = %s" % d)
            steps.append("S = { %s }" % d)
        elif not has_b:
            steps.append("S = { 0 }")

        return steps

