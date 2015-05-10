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

from PyQt5.QtWidgets import (
    QSplitter,
    QFileDialog
    )
from PyQt5.QtCore import (
    pyqtSignal
    )
from amaru.ui.main import Amaru
from amaru.core import (
    logger,
    fobject
    )
from amaru.ui import tab_manager
from amaru.ui.text_editor import editor
# Logger
log = logger.get_logger(__name__)


class MainContainer(QSplitter):

    # Signals
    folderOpened = pyqtSignal('PyQt_PyObject')

    def __init__(self):
        QSplitter.__init__(self)
        self.tab = tab_manager.TabManager()
        self.addWidget(self.tab)
        self.setStyleSheet("border: none;")
        Amaru.load_component("main_container", self)

    def new_file(self, amaru_file=None, filename=""):
        """ Create a new tab editor """

        #if amaru_file is None:
        amaru_file = fobject.FObject(filename)
        weditor = editor.AmaruEditor(amaru_file)
        self.tab.add_tab(weditor, amaru_file.get_name)

        weditor.modificationChanged[bool].connect(self._editor_modified)
        weditor.cursorPositionChanged[int, int].connect(
            self._update_cursor_position)
        weditor.setFocus()
        return weditor

    def open_file(self, filename=""):
        if not filename:
            filenames = QFileDialog.getOpenFileNames(self,
                                                     self.tr("Open File"))[0]
        else:
            filenames = [filename]
        for f in filenames:
            amaru_file = fobject.FObject(f)
            content = amaru_file.read()
            weditor = self.new_file(amaru_file, f)
            weditor.setText(content)
            weditor.setModified(False)

    def save_file(self):
        weditor = self.get_active_editor()
        if weditor.fobject.is_new:
            return self.save_file_as()
        source = weditor.text()
        weditor.fobject.write(source)
        weditor.setModified(False)

    def save_file_as(self):
        print("save as...")

    def close_file(self):
        self.tab.close_tab()

    def _editor_modified(self, modified):
        self.tab.editor_modified(modified)

    def get_active_editor(self):
        widget = self.tab.currentWidget()
        if isinstance(widget, editor.AmaruEditor):
            return widget
        return None

    def _update_cursor_position(self, line, column):
        status_bar = Amaru.get_component("status_bar")
        status_bar.update_line_and_column(line + 1, column)

    def open_folder(self):
        folder = QFileDialog.getExistingDirectory(self, self.tr("Open Folder"))
        if not folder:
            return
        folder_structure = {}
        #FIXME: move to manager
        for parent, dirs, files in os.walk(folder):
            dirs = [d for d in dirs
                    if not d.startswith('.')]
            folder_structure[parent] = (files, dirs)
        # Emit the signal
        self.folderOpened.emit((folder_structure, folder))
        lateral = Amaru.get_component("lateral")
        if not lateral.isVisible():
            lateral.show()

log.debug("Installing main container...")
main_container = MainContainer()