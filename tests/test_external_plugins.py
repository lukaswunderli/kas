# test for external plugins
#
# Copyright (c) Kistler Instrumente AG, 2024
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

import pytest
import shutil
from kas import kas


def test_valid_external_plugin(monkeykas, tmpdir):
    tdir = str(tmpdir / 'external_plugins')
    shutil.copytree('tests/external_plugins', tdir)
    monkeykas.chdir(tdir)
    monkeykas.setenv('KAS_EXTERNAL_PLUGINS', tdir)
    kas.kas(['dummy', 'test.yml'])

def test_invalid_external_plugin_versions_too_low(monkeykas, tmpdir):
    tdir = str(tmpdir / 'external_plugins')
    shutil.copytree('tests/external_plugins', tdir)
    monkeykas.chdir(tdir)
    monkeykas.setenv('KAS_EXTERNAL_PLUGINS', tdir)

    with pytest.raises(SystemExit) as excinfo:
        kas.kas(['dummyfail1', 'test.yml'])

def test_invalid_external_plugin_versions_too_high(monkeykas, tmpdir):
    tdir = str(tmpdir / 'external_plugins')
    shutil.copytree('tests/external_plugins', tdir)
    monkeykas.chdir(tdir)
    monkeykas.setenv('KAS_EXTERNAL_PLUGINS', tdir)

    with pytest.raises(SystemExit) as excinfo:
        kas.kas(['dummyfail2', 'test.yml'])
