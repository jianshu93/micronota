# ----------------------------------------------------------------------------
# Copyright (c) 2015--, micronota development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------
import re

from skbio import read

from . import BaseMod


class Module(BaseMod):
    def __init__(self, directory, file_patterns=None):
        if file_patterns is None:
            file_patterns = {'txt': 'aragorn.txt'}
        super().__init__(directory, file_patterns)

    def parse(self):
        '''Parse the annotation and add it to interval metadata. '''
        for seqid, imd in read(self.files['txt'], format='aragorn'):
            self.result[seqid] = imd

    def report(self):
        self.report = {}
        for sid, imd in self.result.items():
            self.report[sid] = len(imd._intervals)
