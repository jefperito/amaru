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
    #QFileDialog
    )
from amaru.ui.main import Amaru
from amaru.core import (
    logger,
    #fobject
    )
from amaru.ui import tab_manager
#from amaru.ui.text_editor import editor
# Logger
log = logger.get_logger(__name__)


class MainContainer(QSplitter):

    def __init__(self):
        QSplitter.__init__(self)
        self.tab = tab_manager.TabManager()
        self.addWidget(self.tab)

        Amaru.load_component("main_container", self)

    def new_file(self, ffobject=None):
        """ Create a new tab editor """
        pass

    def open_file(self, filename=""):
        pass

    def save_file(self):
        pass

    def save_file_as(self):
        pass


log.debug("Installing main container...")
main_container = MainContainer()