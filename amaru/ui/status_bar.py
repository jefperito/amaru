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
    QStatusBar,
    QLabel,
    QWidget,
    QHBoxLayout
    )
from amaru.ui.main import Amaru
from amaru.core import (
    logger,
    helpers
    )
# Logger
log = logger.get_logger(__name__)


class StatusBar(QStatusBar):

    def __init__(self):
        super(StatusBar, self).__init__()
        self.setStyleSheet("border: none;")
        container = QWidget()
        box = QHBoxLayout(container)
        box.setSpacing(20)
        # File Path
        self.label_file = QLabel("")
        self.label_file.setObjectName("status-path")
        box.addWidget(self.label_file)

        # Cursor Position
        self._line_col = "%s / %s"
        self.label = QLabel(self._line_col % (0, 0))
        self.label.setObjectName("status-cursor")
        box.addWidget(self.label)

        # File type
        self._file_type = QLabel("CoffeeScript")
        self._file_type.setObjectName("status-type")
        box.addWidget(self._file_type)

        self.addWidget(container)

        Amaru.load_component("status_bar", self)

    def update_line_and_column(self, line, column):
        """ Update cursor position """

        self.label.setText(self._line_col % (line, column))

    def update_file_path(self, filepath):
        """ Update filename and type """

        text = os.path.sep.join(filepath.split(os.path.sep)[-2:])
        self.label_file.setText(text)
        self._update_file_type(filepath)

    def _update_file_type(self, filepath):
        _type = helpers.get_file_type(filepath)
        self._file_type.setText("<b>%s</b>" % _type)


log.debug("Installing status bar...")
status_bar = StatusBar()