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

from collections import Callable
from PyQt5.QtWidgets import (
    QMainWindow,
    QMessageBox,
    QShortcut
    )
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt
from amaru.core import logger
# Logger
log = logger.get_logger(__name__)


class Amaru(QMainWindow):

    # Application components
    __COMPONENTS = {}

    def __init__(self):
        QMainWindow.__init__(self)
        self.setStyleSheet("background: blue")
        self.setWindowTitle(self.tr("[Amaru]"))
        #FIXME: read from settings
        self.showMaximized()

        # Menu bar
        menu_bar = self.menuBar()
        self._install_menubar(menu_bar)

        # Status bar
        self.status_bar = Amaru.get_component("status_bar")
        self.setStatusBar(self.status_bar)

        # Central
        self.load_central_widget()

        # Change tabs ALT + 1-9
        key = Qt.Key_1
        tab_shortcuts = type('TabShortcuts', (QShortcut,), {'index': None})
        for index in range(10):
            short = tab_shortcuts(QKeySequence(Qt.ALT + key), self)
            short.index = index
            key += 1
            short.activated.connect(self._change_tab)

        Amaru.load_component("amaru", self)

    def _change_tab(self):
        sender = self.sender()
        main_container = Amaru.get_component("main_container")
        main_container.change_tab_index(sender.index)

    @classmethod
    def load_component(cls, name, component):
        """ Load an instance of component """

        Amaru.__COMPONENTS[name] = component

    @classmethod
    def get_component(cls, name):
        """ Returns the instance of a component """

        return Amaru.__COMPONENTS.get(name, None)

    def _install_menubar(self, menubar):
        log.debug("Installing menu bar...")
        from amaru.ui import actions

        for item in actions.MENU:
            menubar_item = actions.MENU.get(item)
            menu_name = menubar_item.get('text')
            items = menubar_item.get('items')
            menu = menubar.addMenu(menu_name)
            for menu_item in items:
                if isinstance(menu_item, str):
                    menu.addSeparator()
                else:
                    action = menu_item.get('text')
                    shortcut = menu_item.get('shortcut')
                    obj = self
                    connection = menu_item.get('triggered').split(':')[0]
                    if connection.startswith('main_container'):
                        obj = Amaru.get_component("main_container")
                        connection = menu_item.get('triggered').split(':')[1]
                    qaction = menu.addAction(action)
                    if shortcut is not None:
                        qaction.setShortcut(shortcut)
                    slot = getattr(obj, connection, None)
                    if isinstance(slot, Callable):
                        qaction.triggered.connect(slot)

    def _install_toolbar(self):
        log.debug("Installing status bar...")

    def load_central_widget(self):
        main_container = Amaru.get_component("main_container")
        lateral = Amaru.get_component("lateral")
        lateral.hide()
        self.addDockWidget(Qt.LeftDockWidgetArea, lateral)
        self.setCentralWidget(main_container)

    def show_hide_lateral(self):
        lateral = Amaru.get_component("lateral")
        if lateral.isVisible():
            lateral.hide()
        else:
            lateral.show()

    def visibility_status_bar(self):
        """ Change visibility of Status Bar """

        status_bar = Amaru.get_component("status_bar")
        if status_bar.isVisible():
            status_bar.hide()
        else:
            status_bar.show()

    def show_full_screen_mode(self):
        """ Activate Full Screen Mode """

        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

    def show_about_qt_dialog(self):
        """ Show about Qt dialog """

        QMessageBox.aboutQt(self)