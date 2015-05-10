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


from collections import OrderedDict

""" Actions """

MENU = OrderedDict()

# Menu File
MENU['file'] = {
    "text": "&File",
    "items": [{
            "text": "New File",
            "shortcut": "new",
            "triggered": "main_container:new_file"
        }, {
            "text": "Open File",
            "shortcut": "open",
            "triggered": "main_container:open_file"
        }, {
            "text": "Save File",
            "shortcut": "save",
            "triggered": "main_container:save_file"
        }, {
            "text": "Save File as",
            "shortcut": "save-as",
            "triggered": "main_container:save_file_as"
        }, "-", {
            "text": "Quit",
            "shortcut": "quit",
            "triggered": "close"}]}

# Menu Edit
MENU['edit'] = {
    "text": "&Edit",
    "items": [{
            "text": "Undo",
            "shortcut": "undo",
            "triggered": ""
        }, {
            "text": "Redo",
            "shortcut": "redo",
            "triggered": ""
        }, {
            "text": "Cut",
            "shortcut": "cut",
            "triggered": ""
        }, {
            "text": "Copy",
            "shortcut": "copy",
            "triggered": ""
        }, {
            "text": "Paste",
            "shortcut": "paste",
            "triggered": ""
        }, "-", ]}