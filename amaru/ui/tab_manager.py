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
    QTabWidget,
    QMessageBox
    )


class TabManager(QTabWidget):

    def __init__(self):
        QTabWidget.__init__(self)
        #self.setTabsClosable(True)
        self.setMovable(True)

    def add_tab(self, widget, title):
        index = self.addTab(widget, title)
        self.setTabToolTip(index, widget.fobject.get_filename)
        self.setCurrentIndex(index)

    def close_tab(self):
        index = self.currentIndex()
        self.removeTab(index)

    def removeTab(self, index):
        weditor = self.currentWidget()
        if weditor.is_modified:
            filename = weditor.fobject.get_name
            flags = QMessageBox.No
            flags |= QMessageBox.Cancel
            flags |= QMessageBox.Yes
            result = QMessageBox.information(self,
                                             self.tr("File not saved!"),
                                             self.tr("Save changes to {0} "
                                             "before closing?").format(
                                                 filename), flags)
            if result == QMessageBox.Cancel:
                return
            elif result == QMessageBox.Yes:
                print("saving...")
        super(TabManager, self).removeTab(index)

    def editor_modified(self, modified):
        current_index = self.currentIndex()
        if modified:
            current_text = self.tabText(current_index)
            self.setTabText(current_index, current_text + ' \u2022')
        else:
            text = self.currentWidget().fobject.get_name
            self.setTabText(current_index, text)