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
import time

from PyQt5.QtWidgets import (
    QDialog,
    QWidget,
    QVBoxLayout
    )
from PyQt5.QtQuick import QQuickView
from PyQt5.QtCore import (
    QUrl,
    pyqtSignal
    )

PATH_QML = os.path.join(os.path.dirname(__file__), "StartPage.qml")


class QmlStartPage(QDialog):

    # Signals
    animationFinished = pyqtSignal()

    def __init__(self):
        super(QmlStartPage, self).__init__()
        box = QVBoxLayout(self)
        box.setContentsMargins(0, 0, 0, 0)
        # View
        view = QQuickView()
        view.setSource(QUrl.fromLocalFile(PATH_QML))
        view.setResizeMode(QQuickView.SizeRootObjectToView)
        # Root object
        self._root = view.rootObject()

        widget_container = QWidget.createWindowContainer(view)
        box.addWidget(widget_container)

        self._root.animationFinished.connect(self._on_animation_finished)

    @property
    def get_root(self):
        """ Return the root object """

        return self._root

    def _on_animation_finished(self):
        """ Sleep 3 seconds and emit the signal """

        time.sleep(3)
        self.animationFinished.emit()
