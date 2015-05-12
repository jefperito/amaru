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
    pyqtSignal,
    Qt
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
    fileChanged = pyqtSignal('QString')

    def __init__(self):
        QSplitter.__init__(self)
        self.setObjectName("main_container")
        self.main_tab = tab_manager.TabManager()
        self.secundary_tab = tab_manager.TabManager()
        self.secundary_tab.hide()
        self.tab = self.main_tab
        self.addWidget(self.main_tab)
        self.addWidget(self.secundary_tab)
        #self.setStyleSheet("border: none;")
        Amaru.load_component("main_container", self)

        self.fileChanged.connect(self._file_changed)
        self.tab.currentChanged[int].connect(self._current_tab_changed)

    def _file_changed(self, f):
        status_bar = Amaru.get_component("status_bar")
        status_bar.update_file_path(f)

    def _current_tab_changed(self, index):
        print(index)

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
            self.fileChanged.emit(f)

    def save_file(self):
        weditor = self.get_active_editor()
        if weditor is not None:
            if weditor.fobject.is_new:
                return self.save_file_as(weditor)
            source = weditor.text()
            weditor.fobject.write(source)
            weditor.setModified(False)

    def save_file_as(self, weditor=None):
        if weditor is None:
            weditor = self.get_active_editor()
        filename = QFileDialog.getSaveFileName(self, self.tr("Save File"))[0]
        if not filename:
            return False
        content = weditor.text()
        weditor.fobject.write(content, filename)
        weditor.setModified(False)
        weditor.set_lexer()
        return filename

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

    def split_vertically(self):
        self.split_tab(Qt.Horizontal)

    def split_horizontally(self):
        self.split_tab(Qt.Vertical)

    def split_tab(self, orientation):
        """ Show split """

        if self.get_active_editor() is None:
            return
        if self.secundary_tab.isVisible():
            self.secundary_tab.hide()
            for index in range(self.secundary_tab.count()):
                tab = self.secundary_tab.widget(0)
                tab_name = self.secundary_tab.tabText(0)
                self.main_tab.add_tab(tab, tab_name)
            # Now is current tab
            self.tab = self.main_tab
        else:
            current_widget = self.get_active_editor()
            index = self.main_tab.currentIndex()
            tab_name = self.main_tab.tabText(index)
            self.secundary_tab.add_tab(current_widget, tab_name)
            self.secundary_tab.show()
            # Now is current tab
            self.tab = self.secundary_tab
        self.setSizes([1, 1])
        self.setOrientation(orientation)

    def change_tab_index(self, index):
        self.tab.setCurrentIndex(index)

    def visibility_tab_bar(self):
        """ Change visibility Tab Bar """

        value = self.tab.tabBar().isVisible()
        self.tab.show_hide_tabbar(not value)

    def get_opened_tabs(self):
        tabs = []
        # Main tab
        for index in range(self.main_tab.count()):
            tab = self.main_tab.widget(index)
            filename = tab.fobject.get_filename
            if tab.fobject.is_new:
                continue
            tabs.append(filename)
        # Secundary tab
        for index in range(self.secundary_tab.count()):
            tab = self.secundary_tab.widget(index)
            filename = tab.fobject.get_filename
            if tab.fobject.is_new:
                continue
            tabs.append(filename)
        return tabs

    def show_whitespaces(self):
        """ Show/hide white spaces and tabs """

        weditor = self.get_active_editor()
        if weditor is not None:
            value = weditor.whitespaceVisibility()
            weditor.setWhitespaceVisibility(not value)

    def show_indentation_guides(self):
        weditor = self.get_active_editor()
        if weditor is not None:
            value = weditor.indentationGuides()
            weditor.setIndentationGuides(not value)


log.debug("Installing main container...")
main_container = MainContainer()