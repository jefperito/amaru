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
    QHBoxLayout,
    QToolButton,
    QSpacerItem,
    QSizePolicy,
    QMenu
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
        self._file_type = QToolButton()
        self._file_type.setPopupMode(2)
        self._file_type.setObjectName("status-type")
        box.addWidget(self._file_type)

        # Tabs
        self._tabs_button = QToolButton()
        self._tabs_button.setPopupMode(2)
        menu = QMenu(self)
        self._load_menu_for_button(menu)
        self._tabs_button.setMenu(menu)

        box.addItem(QSpacerItem(container.width() + self.width(), 0,
                    QSizePolicy.Expanding))
        box.addWidget(self._tabs_button)

        self.addWidget(container)

        Amaru.load_component("status_bar", self)

    def _load_menu_for_button(self, menu):
        width = 4
        self._tabs_button.setText("Spaces: %s" % width)
        spaces_or_tabs = menu.addAction("Spaces")
        menu.addSeparator()
        two = menu.addAction("2")
        four = menu.addAction("4")
        eight = menu.addAction("8")

    def update_line_and_column(self, line, column):
        """ Update cursor position """

        self.label.setText(self._line_col % (line, column))

    def update_file_path(self, filepath):
        """ Update filename and type """

        text = os.path.sep.join(filepath.split(os.path.sep)[-2:])
        self.label_file.setText(text)
        self._update_file_type(filepath)

    def _update_file_type(self, filepath):
        if filepath == 'Untitled':
            _type = "Plain text"
        else:
            _type = helpers.get_file_type(filepath)
        self._file_type.setText("%s" % _type)

    def _change_indentation(self):
        pass


log.debug("Installing status bar...")
status_bar = StatusBar()