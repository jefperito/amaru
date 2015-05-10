# -*- coding: utf-8 -*-
#
# Copyright 2015 - Zector Labs
#
# This file is part of Amaru.
#
# Amaru is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# any later version.
#
# Amaru is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Amaru; If not, see <http://www.gnu.org/licenses/>.


from PyQt5.QtGui import QColor
from PyQt5.Qsci import (
    QsciLexerPython,
    QsciLexerCPP,
    QsciLexerCoffeeScript,
    )
from amaru.ui.text_editor import scheme


class Base(object):

    def __init__(self, *args, **kwargs):
        super(Base, self).__init__(*args, **kwargs)
        self.highlighter()

    def highlighter(self):
        _scheme = scheme.DEFAULT
        self.setDefaultPaper(QColor(_scheme['BackgroundEditor']))
        self.setPaper(self.defaultPaper(0))
        self.setColor(QColor(_scheme['Color']))
        types = dir(self)
        for _type in types:
            if _type in _scheme:
                atr = getattr(self, _type)
                self.setColor(QColor(_scheme[_type]), atr)


class PythonLexer(Base, QsciLexerPython):

    def __init__(self, *args, **kwargs):
        super(PythonLexer, self).__init__(*args, **kwargs)


class CPPLexer(Base, QsciLexerCPP):

    def __init__(self, *args, **kwargs):
        super(CPPLexer, self).__init__(*args, **kwargs)


class CoffeeLexer(Base, QsciLexerCoffeeScript):

    def __init__(self, *args, **kwargs):
        super(CoffeeLexer, self).__init__(*args, **kwargs)


LEXERS = {
    "python": PythonLexer,
    "cpp": CPPLexer,
    "coffee": CoffeeLexer
    }

EXTS = {
    ".py": "python",
    ".c": "cpp",
    ".cpp": "cpp",
    ".h": "cpp",
    ".coffee": "coffee",
    }


def get_lexer(extension=""):
    language = EXTS.get(extension, None)
    if language is None:
        lexer = None
    else:
        lexer = LEXERS.get(language, None)()
    return lexer