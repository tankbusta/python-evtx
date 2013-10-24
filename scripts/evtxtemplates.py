#!/bin/python
#    This file is part of python-evtx.
#
#   Copyright 2012, 2013 Willi Ballenthin <william.ballenthin@mandiant.com>
#                    while at Mandiant <http://www.mandiant.com>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
#   Version v0.1
from __future__ import print_function, absolute_import

import sys
import mmap
import contextlib
from Evtx.Evtx import FileHeader
from Evtx.Views import evtx_template_readable_view

def main():
    with open(sys.argv[1], 'r') as f:
        with contextlib.closing(mmap.mmap(f.fileno(), 0,
                                          access=mmap.ACCESS_READ)) as buf:
            fh = FileHeader(buf, 0x0)
            for (i, chunk) in enumerate(fh.chunks()):
                for template in chunk.templates().values():
                    print("Template {%s} at chunk %d, offset %s" % \
                        (template.guid(), i,
                         hex(template.absolute_offset(0x0))))
                    print(evtx_template_readable_view(template))

if __name__ == "__main__":
    main()
