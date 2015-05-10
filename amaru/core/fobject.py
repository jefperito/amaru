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
from PyQt5.QtCore import (
    QObject,
    QFile,
    QIODevice,
    QTextStream
    )


class FObject(QObject):

    """ File representation """

    def __init__(self, file_path=""):
        QObject.__init__(self)
        self._is_new = True
        if not file_path:
            self._file_path = "New_file"
        else:
            self._file_path = file_path
            self._is_new = False

    @property
    def is_new(self):
        return self._is_new

    @property
    def get_name(self):
        return os.path.basename(self._file_path)

    @property
    def get_filename(self):
        return self._file_path

    def read(self):
        """ Read file """

        try:
            with open(self._file_path, mode='r') as f:
                content = f.read()
            return content
        except IOError as reason:
            raise IOError(reason)

    def write(self, content, new_filename=""):
        if self.is_new:
            self._file_path = new_filename
            self._is_new = False
        f = QFile(self.get_filename)
        if not f.open(QIODevice.WriteOnly | QIODevice.Truncate):
            raise Exception
        outfile = QTextStream(f)
        outfile << content