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
from PyQt5.QtCore import pyqtSignal

from amaru.ui.main import Amaru


class TabManager(QTabWidget):

    # Signals
    allTabsClosed = pyqtSignal()

    def __init__(self):
        QTabWidget.__init__(self)
        self.setTabsClosable(True)
        self.setMovable(True)

        self.tabCloseRequested[int].connect(self.removeTab)

    def add_start_page(self, qml):
        root = qml.get_root
        tab_bar = self.tabBar()
        tab_bar.setVisible(False)
        self.addTab(qml, "Start Page")
        root.start_animation()

        qml.animationFinished.connect(lambda: tab_bar.setVisible(True))

    def add_tab(self, widget, title):
        status_bar = Amaru.get_component("status_bar")
        if not status_bar.isVisible():
            status_bar.show()
        index = self.addTab(widget, title)
        self.setTabToolTip(index, widget.fobject.get_filename)
        self.setCurrentIndex(index)

    def close_tab(self):
        index = self.currentIndex()
        self.removeTab(index)

    def show_hide_tabbar(self, value):
        """ Visibility of tab bar """

        tab_bar = self.tabBar()
        tab_bar.setVisible(value)

    def removeTab(self, index):
        if index == -1:
            return
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
                main_container = Amaru.get_component("main_container")
                main_container.save_file()
        super(TabManager, self).removeTab(index)
        if self.currentWidget() is None:
            # All tabs closed
            self.allTabsClosed.emit()

    def editor_modified(self, modified):
        current_index = self.currentIndex()
        if modified:
            current_text = self.tabText(current_index)
            self.setTabText(current_index, current_text + ' \u2022')
        else:
            text = self.currentWidget().fobject.get_name
            self.setTabText(current_index, text)