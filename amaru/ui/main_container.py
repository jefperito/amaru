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


from PyQt5.QtWidgets import (
    QSplitter,
    QFileDialog
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

    def __init__(self):
        QSplitter.__init__(self)
        self.tab = tab_manager.TabManager()
        self.addWidget(self.tab)

        Amaru.load_component("main_container", self)

    def new_file(self, amaru_file=None, filename=""):
        """ Create a new tab editor """

        #if amaru_file is None:
        amaru_file = fobject.FObject(filename)
        weditor = editor.AmaruEditor(amaru_file)
        self.tab.add_tab(weditor, amaru_file.get_name)
        return weditor

    def open_file(self, filename=""):
        if not filename:
            filenames = QFileDialog.getOpenFileNames(self,
                                                     self.tr("Open File"))
        else:
            filenames = [filename]
        for f in filenames[0]:
            amaru_file = fobject.FObject(f)
            content = amaru_file.read()
            weditor = self.new_file(amaru_file, f)
            weditor.setText(content)

    def save_file(self):
        pass

    def save_file_as(self):
        pass

    def close_file(self):
        self.tab.close_tab()


log.debug("Installing main container...")
main_container = MainContainer()