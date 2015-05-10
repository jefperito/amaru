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
    QDockWidget,
    )

from amaru.ui.main import Amaru


class Lateral(QDockWidget):

    def __init__(self):
        super(Lateral, self).__init__()
        self.setFeatures(QDockWidget.DockWidgetFloatable |
                         QDockWidget.DockWidgetMovable)
        Amaru.load_component("lateral", self)
        tree_project = Amaru.get_component("tree_project")
        main_container = Amaru.get_component("main_container")
        main_container.folderOpened.connect(tree_project.open_project)
        self.setWidget(tree_project)


lateral = Lateral()