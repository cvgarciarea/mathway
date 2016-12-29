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

import math
from gettext import gettext as _

from constants import FunctionType
from constants import MATH_EXPRESSIONS


def is_number(value):
    try:
        int(value)
        return True
    except:
        return False
    #return value.replace(".", "", 1).isdigit()


def log(value):
    return math.log(value) / math.log(10)

def sec(value):
    return 1.0 / math.cos(value)

def csc(value):
    return 1 / math.sin(value)

def cot(value):
    return 1 / math.tan(value)

def asec(value):
    return math.acos(1 / a)

def acsc(value):
    return math.asin(1 / a)

def acot(value):
    return math.atan(1 / a)

def sech(value):
    return 2 / (math.exp(value) + math.exp(-a))

def csch(value):
    return 2 / (math.exp(value) - math.exp(-a))

def coth(value):
    return (math.exp(value) + math.exp(-a)) / (math.exp(value) - math.exp(-a))

def asech(value):
    return math.log((math.sqrt(1 - a * a) + 1) / a)

def acsch(value):
    return math.log((sgn(value) * math.sqrt(a * a + 1) + 1) / a)

def acoth(value):
    return math.log((a + 1) / (a - 1)) / 2


def parse_math_expression(expression):
    for replazable in MATH_EXPRESSIONS.keys():
        value = MATH_EXPRESSIONS[replazable]
        expression = expression.replace(replazable, value)

    return expression


def calculate_math_expression(expression):
    parsed = parse_math_expression(expression)
    return eval(parsed)


def get_function_type_name(ftype):
    if ftype == FunctionType.CONSTANT:
        return _("Constant")

    elif ftype == FunctionType.LINEAL:
        return _("Lineal")

    elif ftype == FunctionType.QUADRATIC:
        return _("Quadratic")

    elif ftype == FunctionType.CUBIC:
        return _("Cubic")

    elif ftype == FunctionType.POLINOMIC:
        return _("Polinomic")

    elif ftype == FunctionType.EXPONENTIAL:
        return _("Exponential")

    elif ftype == FunctionType.RACIONAL:
        return _("Racional")

    elif ftype == FunctionType.LOGARITHMIC:
        return _("Logarithmic")

    elif ftype == FunctionType.TRIGONOMETRIC:
        return _("Trigonometric")

    else:
        return _("Null")


def ignore_values(old_list, ignored=""):
    new_list = []
    for value in old_list:
        if value != ignored:
            new_list.append(value)

    return new_list


def clear_float(number):
    format = "%d" if number.is_integer() else "%s"
    return format % number
