# kas - setup tool for bitbake based projects
#
# Copyright (c) Siemens AG, 2017-2024
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# This plugin (c) Kistler Instrumente AG, 2014
#
"""
    This plugin implements the ``kas dummy`` command.
"""

import sys
import logging
from pathlib import Path
from typing import TypeVar, TextIO
from collections import OrderedDict
from kas.context import get_context
from kas.plugins.checkout import Checkout
from kas.kasusererror import KasUserError, ArgsCombinationError

__license__ = 'MIT'
__copyright__ = 'Copyright (c) Kistler Instrumente AG, 2024'


class OutputFormatError(KasUserError):
    def __init__(self, format):
        super().__init__(f'invalid format {format}')


class Dummy(Checkout):
    """
    Implements a dummy kas plugin for testing
    """

    name = 'dummy'
    helpmsg = (
        'Dummy plugin which is valid'
    )

    @classmethod
    def setup_parser(cls, parser):
        super().setup_parser(parser)
        #parser.add_argument('--format',
                            #choices=['txz', 'tgz', 'tar', 'tbz'],
                            #default='txz',
                            #help='Output format (default: txz)')

    def run(self, args):
        args.skip += [
            'setup_dir',
            'repos_apply_patches',
            'setup_environ',
            'write_bbconfig',
        ]

        super().run(args)

        logging.info('Dummy plugin')

__KAS_PLUGINS__ = [Dummy]
__KAS_MAX__ = "1111.1.1"
__KAS_MIN__ = "0.8.0"
