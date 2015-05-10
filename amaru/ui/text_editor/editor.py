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

import os
from PyQt5.QtGui import QFontMetrics, QColor
from PyQt5.Qsci import QsciScintilla
from amaru.ui.text_editor import lexer
from amaru.core import settings


class AmaruEditor(QsciScintilla):

    """ Editor """

    # Signals

    def __init__(self, fobject=None):
        super(AmaruEditor, self).__init__()
        # FObject
        self.fobject = fobject
        # Scintilla configuration
        self.SendScintilla(QsciScintilla.SCI_SETHSCROLLBAR, False)
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        self.setAutoIndent(True)
        self.setBackspaceUnindents(True)
        self.SendScintilla(QsciScintilla.SCI_SETCARETFORE, QColor("#FFFFFF"))
        self.setMarginsBackgroundColor(QColor("#272822"))
        self.setMarginsForegroundColor(QColor("#8f908a"))
        # Font
        self._font = settings.DEFAULT_FONT
        # Lexer
        ext = os.path.splitext(fobject.get_name)[-1]
        self._lexer = lexer.get_lexer(ext)
        if self._lexer is not None:
            self.setLexer(self._lexer)
            self._lexer.setFont(self._font)
        else:
            self.setPaper(QColor("#272822"))
            self.setColor(QColor("#f8f8f2"))

        self.linesChanged.connect(self.update_sidebar)

    def update_sidebar(self):
        fmetrics = QFontMetrics(self._font)
        lines = str(self.lines()) + '0'
        width = fmetrics.width(lines)
        self.setMarginWidth(0, width)