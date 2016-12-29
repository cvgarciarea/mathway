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

from utils import ignore_values


class ValueGetter:

    @classmethod
    def split_monomials(self, data):
        data = data.replace("+", "SPLIT+").replace("-", "SPLIT-")

        if "SPLIT" in data:
            return ignore_values(data.split("SPLIT"))
        else:
            return [data]

    @classmethod
    def extract_coefficient(self, monomial):
        monomial = monomial.replace(" ", "")
        number = 0
        snumber = ""

        if monomial != "" and not "x" in monomial:
            return float(monomial)

        if "x" in monomial:
            splited = monomial.split("x")
            if splited[0] != "":
                snumber = splited[0]
            else:
                snumber = splited[1]

        else:
            snumber = monomial

        if snumber.endswith("^"):
            snumber = snumber[:len(snumber) - 1]

        if snumber == "+":
            number = 1
        elif snumber == "-":
            number = -1
        elif snumber != "":
            number = float(snumber)
        else:
            number = 1

        return number

    @classmethod
    def lineal(self, function):
        monomials = self.split_monomials(function.formula)
        a = 0
        b = 0

        for monomial in monomials:
            if monomial != "":
                if "x" in monomial:
                    a = self.extract_coefficient(monomial)
                else:
                    b = self.extract_coefficient(monomial)

        return [a, b]

    @classmethod
    def quadratic(self, function):
        monomials = self.split_monomials(function.formula)
        a = 0
        b = 0
        c = 0

        for monomial in monomials:
            if monomial.trim() != "":
                if "x^" in monomial:
                    a = self.extract_coefficient(monomial)
                elif "x" in monomial and not "x^" in monomial:
                    b = self.extract_coefficient(monomial)
                else:
                    c = self.extract_coefficient(monomial)

        return [a, b, c]

    @classmethod
    def quibic(self, function):
        # TODO
        return []

    @classmethod
    def polinomic(self, function):
        # TODO
        return []

    @classmethod
    def exponential(self, function):
        # TODO
        return []

    @classmethod
    def racional(self, function):
        # TODO
        return []

    @classmethod
    def logaritmic(self, function):
        # TODO
        return []

    @classmethod
    def trigonometric(self, function):
        # TODO
        return []
