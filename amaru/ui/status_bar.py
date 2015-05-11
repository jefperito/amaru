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
    QStatusBar,
    QLabel
    )
from amaru.ui.main import Amaru
from amaru.core import logger
# Logger
log = logger.get_logger(__name__)


class StatusBar(QStatusBar):

    def __init__(self):
        super(StatusBar, self).__init__()
        self.setStyleSheet("border: none;")
        self._line_col = "%s / %s"
        self.label = QLabel(self._line_col % (0, 0))
        self.label.setObjectName("line-col")
        self.addWidget(self.label)

        Amaru.load_component("status_bar", self)

    def update_line_and_column(self, line, column):
        self.label.setText(self._line_col % (line, column))


log.debug("Installing status bar...")
status_bar = StatusBar()