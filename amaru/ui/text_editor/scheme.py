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


PYTHON = {
    'BackgroundEditor': '#272822',
    'Default': '#F8F8F2',
    'Comment': '#75715E',
    'Number': '#AE81FF',
    'DoubleQuotedString': '#E6DB74',
    'SingleQuotedString': '#E6DB74',
    'Keyword': '#66D9EF',
    'TripleSingleQuotedString': '#E6DB74',
    'TripleDoubleQuotedString': '#E6DB74',
    'ClassName': '#86E22E',
    'FunctionMethodName': '#86E22E',
    'Operator': '#FFFFFF',
    'CommentBlock': '#FF0000',
    'UnclosedString': '#FF0000',
    'HighlightedIdentifier': '#66D9A4',
    'Decorator': '#FD971F'
    }

CPP = {
    'BackgroundEditor': '#272822',
    'Default': '#F8F8F2',
    'Comment': '#75715E',
    'CommentLine': '#75715E',
    'CommentDoc': '#FF0000',
    'Number': '#AE81FF',
    'Keyword': '#66D9EF',
    'DoubleQuotedString': '#E6DB74',
    'SingleQuotedString': '#B8DB74',
    #'UUID': '#FF0000',
    'PreProcessor': '#D50550',
    'Operator': '#FFFFFF',
    'UnclosedString': '#FF0000',
    #'VerbatimString': '#FF0000',
    #'Regex': '#00FF00',
    #'CommentLineDoc': '#00FF00',
    'PreProcessorComment': '#282FD5',
    #'HashQuotedString': '#FF0000',
    #'GlobalClass': '#FF0000',
    #'RawString': '#FF0000',
    #'UserLiteral': '#00FF00',
    #'TaskMarker': '#FF0000',
    #'EscapeSequence': '#FF0000'
    }

CSS = {
    'BackgroundEditor': '#272822',
    'Default': '#F8F8F2',
    'Tag': '#86E22E',
    'ClassSelector': '#66D9EF',
    'PseudoClass': '#66A0EF',
    'UnknownPseudoClass': '#66D9A4',
    'Operator': '#FFFFFF',
    'CSS1Property': '#FD971F',
    'UnknownProperty': '#FDC27C',
    'Value': '#AE81FF',
    #'Comment': '#FF0000',
    'IDSelector': '#C8E22E',
    #'Important': '#FF0000',
    #'AtRule': '#FF0000',
    #'DoubleQuotedString': '#FF0000',
    #'SingleQuotedString': '#FF0000',
    #'CSS2Property': '#FF0000',  # Keyset 3
    #'Attribute': '#FF0000',
    #'CSS3Property': '#FF0000',  # Keyset 4
    #'PseudoElement': '#FF0000',  # Keyset 5
    #'ExtendedCSSProperty': '#FF0000'  # Keyset 6
    #'ExtendedPseudoClass': '#FF0000'  # Keyset 7
    #'ExtendedPseudoElement': '#FF0000'  # Keyset 8
    'MediaRule': '#D50550',
    'Variable': '#FF0000',
    }

HTML = {
    'BackgroundEditor': '#272822',
    'Default': '#F8F8F2',
    'Tag': '#86E22E',
    'Attribute': '#FD971F',
    #'UnknownAttribute': '#FF0000',
    'HTMLNumber': '#AE81FF',
    'HTMLDoubleQuotedString': '#E6DB74',
    'HTMLSingleQuotedString': '#E6DB74',
    'OtherInTag': '#FFFFFF',
    'HTMLComment': '#75715E',
    #'Entity': '#FF0000',
    #'XMLTagEnd': '#FF0000',
    #'XMLStart': '#FF0000',
    #'XMLEnd': '#FF0000',
    #'Script': '#FF0000',
    #'ASPAtStart': '#FF0000',
    'ASPStart': '#FF0000',
    #'CDATA': '#FF0000',
    #'PHPStart': '#FF0000',
    #'HTMLValue': '#FF0000',
    }

SCHEMES = {
    "python": PYTHON,
    "cpp": CPP,
    "css": CSS,
    "html": HTML
    }


def get_lexer_scheme(key):
    return SCHEMES.get(key, None)