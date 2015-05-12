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


def get_file_type(filename):
    """ Return file type by extension """

    types_map = {
        '.py': 'Python',
        '.c': 'C',
        '.cpp': 'CPP',
        '.coffee': 'CoffeeScript',
        '.java': 'Java',
        '.html': 'HTML',
        '.css': 'CSS',
        }

    extension = os.path.splitext(filename)[-1]
    return types_map[extension]