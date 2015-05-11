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

import unittest
import os
from amaru.core import fobject


class FObjectTestCase(unittest.TestCase):

    def setUp(self):
        cdir = os.path.join(os.path.dirname(__file__))
        self._filename = os.path.join(cdir, "for_test")

    def test_read(self):
        afile = fobject.FObject(self._filename)
        expected = "aáÁ~ñañ^sdqwe123456787654\nggǵǵǵaáahhbóóooHO"
        content = afile.read()
        self.assertTrue(content, expected)

    def test_write(self):
        pass

    def test_is_new(self):
        afile = fobject.FObject()
        self.assertTrue(afile.is_new)


if __name__ == "__main__":
    unittest.main()