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

MATH_EXPRESSIONS = {
    "pi(": "math.pi(",
    "e(": "math.e(",
    "ln(": "math.log(",
    "sen(": "math.sin(",
    "sin(": "math.sin(",
    "cos(": "math.cos(",
    "asin(": "math.asin",
    "asen(": "math.asin(",
    "acos(": "math.acos(",
    "atan(": "math.atan(",
    "sinh(": "math.sinh(",
    "senh(": "math.sinh(",
    "cosh(": "math.cosh(",
    "tanh(": "math.tanh(",
    "asinh(": "math.asinh(",
    "asenh(": "math.asenh(",
    "acosh(": "math.acosh(",
    "atanh(": "math.atanh(",
    "rnd(": "round(",
}


class Re:
    CONSTANT = "^[-+]?(\\d+)*(.(\\d+))?$"
    TRIGONOMETRIC = "[-+]?(\\d+)*(.(\\d+))?[+-]?(?:sec|tan|cos)[(].+[)]"
    RACIONAL = "(.+)[/](.+)"
    QUADRATIC = "[+-]?[x][\\^][2]"
    CUBIC = "[+-]?[x][\\^][3]"
    POLINOMIC = "[+-]?[x][\\^][4-9]"
    EXPONENTIAL = "[+-]?(\\d+)*(.(\\d+))?[\\^][+-]?(\\d+)*(.(\\d+))?[x]"


class Set:
    EMPTY     = "∅"
    NATURALS  = "ℕ"
    INTEGERS  = "ℤ"
    RACIONALS = "ℚ"
    REALS     = "ℝ"
    COMPLEXES = "ℂ"


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
