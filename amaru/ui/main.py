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

""" Main Window """


from PyQt5.QtWidgets import (
    QMainWindow
    )

from amaru.ui import status_bar
from amaru.core import logger
# Logger
log = logger.get_logger(__name__)


class Amaru(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle(self.tr("[Amaru]"))
        #FIXME: read from settings
        self.showMaximized()

        # Menu bar
        menu_bar = self.menuBar()
        self._install_menubar(menu_bar)

        # Status bar
        self.status_bar = status_bar.StatusBar()
        self.setStatusBar(self.status_bar)

    def _install_menubar(self, menubar):
        log.debug("Installing menu bar...")
        menubar_items = [
            self.tr("&File"),
            self.tr("&Edit"),
            self.tr("&View"),
            self.tr("F&ind"),
            self.tr("&Goto"),
            self.tr("&Help")
            ]
        for item in menubar_items:
            menubar.addMenu(item)

    def _install_toolbar(self):
        log.debug("Installing status bar...")