#!/usr/bin/env python
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
import sys

# Project Path
amaru_dir = os.path.abspath(os.path.dirname(
    os.path.realpath(os.path.dirname(sys.argv[0]))))
sys.path.insert(0, amaru_dir)

import amaru
from amaru.core import logger
# Logger
log = logger.get_logger(__name__)


if __name__ == "__main__":
    log.debug("Starting...")
    amaru.rock_and_roll()