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
    QTreeWidget,
    QTreeWidgetItem,
    QHeaderView
    )

from amaru.ui.main import Amaru


class TreeProject(QTreeWidget):

    def __init__(self):
        QTreeWidget.__init__(self)
        self.setAnimated(True)
        self.setHeaderLabel(self.tr("Folders"))
        self.header().setStretchLastSection(False)
        self.header().setHidden(True)
        self.header().setSectionResizeMode(0, QHeaderView.ResizeToContents)

        self.itemClicked.connect(self._open_file)

        Amaru.load_component("tree_project", self)

    def _open_file(a, b):
        if b.isFile:
            filename = b.path
            main_container = Amaru.get_component("main_container")
            main_container.open_file(filename)

    def open_project(self, folder_structure):
        structure, root = folder_structure
        root_basename = os.path.basename(root)
        parent = TreeItem(self, [root_basename])
        self._load_tree(structure, parent, root)
        parent.setExpanded(True)

    def _load_tree(self, structure, parent, root):
        files, folders = structure.get(root)
        if files is not None:
            for f in sorted(files):
                file_item = TreeItem(parent, [f])
                file_item.path = os.path.join(root, f)
                file_item.setToolTip(0, f)
        if folders is not None:
            for folder in sorted(folders):
                folder_item = TreeItem(parent, [folder])
                folder_item.isFile = False
                folder_item.path = os.path.join(root, folder)
                folder_item.setToolTip(0, folder)
                self._load_tree(structure, folder_item,
                                os.path.join(root, folder))


class TreeItem(QTreeWidgetItem):

    def __init__(self, parent=None, name=''):
        QTreeWidgetItem.__init__(self, parent, name)
        self.isFile = True
        self._path = ''

    def __get_path(self):
        return self._path

    def __set_path(self, path):
        self._path = path

    path = property(__get_path, __set_path)


tree_project = TreeProject()