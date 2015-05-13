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

""" ¡Rock and Roll! """

# Resource file
from amaru import amaru_resources  # lint:ok
import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QSettings
from amaru.ui.main import Amaru
from amaru.core import (
    logger,
    #settings,
    paths
    )
# Logger
log = logger.get_logger(__name__)

amaru_dir = os.path.dirname(__file__)
style = os.path.join(amaru_dir, "resources", "themes", "amaru_dark.qss")


def rock_and_roll():
    qsettings = QSettings(paths.SETTINGS, QSettings.IniFormat)
    qapp = QApplication(sys.argv)
    # Load components after qapp
    #lint:disable
    import amaru.ui.main_container
    import amaru.ui.status_bar
    import amaru.ui.lateral.tree_project
    import amaru.ui.lateral.lateral
    #lint:enable

    # StyleSheet
    log.debug("Aply style sheet...")
    with open(style, mode='r') as f:
        qapp.setStyleSheet(f.read())

    # Show GUI
    log.debug("Showing GUI...")
    gui = Amaru()
    gui.setMinimumSize(700, 500)
    gui.show()

    # Load tabs from last session
    tabs = qsettings.value("opened-tabs")
    if tabs is None:
        tabs = []
    gui.load_files(tabs)

    sys.exit(qapp.exec_())