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
    QsciLexerCSS,
    QsciLexerCoffeeScript,
    QsciLexerHTML,
    )
from amaru.ui.text_editor import scheme


class Base(object):

    def __init__(self, *args, **kwargs):
        super(Base, self).__init__(*args, **kwargs)

    def highlighter(self, language):
        _scheme = scheme.get_lexer_scheme(language)
        self.setDefaultPaper(QColor(_scheme['BackgroundEditor']))
        #self.setPaper(self.defaultPaper()
        self.setColor(QColor(_scheme['Default']))
        types = dir(self)
        for _type in types:
            if _type in _scheme:
                atr = getattr(self, _type)
                self.setColor(QColor(_scheme[_type]), atr)


class PythonLexer(Base, QsciLexerPython):

    def __init__(self, *args, **kwargs):
        super(PythonLexer, self).__init__(*args, **kwargs)

    def keywords(self, kset):
        if kset == 1:
            return ('class def if else elif return and or as assert '
                    'break continue del except finally for from global '
                    'import in is lambda not pass raise try while with yield')
        elif kset == 2:
            return ('self super all any basestring bin bool bytearray nonlocal '
                    'callable chr abs classmethod cmp compile complex delattr '
                    'dict dir divmod enumerate eval execfile file filter '
                    'float format frozenset getattr globals hasattr hash help '
                    'hex id input int isinstance issubclass iter len list '
                    'locals long map max memoryview min next object oct open '
                    'ord pow property range raw_input reduce reload repr '
                    'reversed round set setattr slice sorted staticmethod '
                    'str sum tuple type unichr unicode vars xrange zip apply '
                    'buffer coerce intern True False')
        super(PythonLexer, self).keywords(kset)


class CPPLexer(Base, QsciLexerCPP):

    def __init__(self, *args, **kwargs):
        super(CPPLexer, self).__init__(*args, **kwargs)


class CoffeeLexer(Base, QsciLexerCoffeeScript):

    def __init__(self, *args, **kwargs):
        super(CoffeeLexer, self).__init__(*args, **kwargs)


class HTMLLexer(Base, QsciLexerHTML):

    def __init__(self, *args, **kwargs):
        super(HTMLLexer, self).__init__(*args, **kwargs)


class CSSLexer(Base, QsciLexerCSS):

    def __init__(self, *args, **kwargs):
        super(CSSLexer, self).__init__(*args, **kwargs)


LEXERS = {
    "python": PythonLexer,
    "cpp": CPPLexer,
    "coffee": CoffeeLexer,
    "html": HTMLLexer,
    "css": CSSLexer,
    }

EXTS = {
    ".py": "python",
    ".c": "cpp",
    ".cpp": "cpp",
    ".h": "cpp",
    ".coffee": "coffee",
    '.html': "html",
    '.css': "css",
    '.qss': "css"
    }


def get_lexer(extension=""):
    language = EXTS.get(extension, None)
    if language is None:
        lex = None
    else:
        Lexer = LEXERS.get(language, None)
        lex = Lexer()
        lex.highlighter(language)
    return lex