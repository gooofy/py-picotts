#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#
# Copyright 2017 Guenter Bartsch
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#

import logging
import subprocess
import tempfile

VOICES = [ 'de-DE', 'en-GB', 'en-US', 'es-ES', 'fr-FR', 'it-IT' ]

class PicoTTS(object):

    def __init__(self, 
                 voice       = 'en-US'):
        self._voice       = voice      

    def _picotts_exe(self, args, sync=False):
        cmd = ['pico2wave', 
               '-l', self._voice, 
               ]

        cmd.extend(args)

        logging.debug('picotts: executing %s' % repr(cmd))

        p = subprocess.Popen(cmd,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)
        res = iter(p.stdout.readline, b'')
        if not sync:
            return res

        res2 = []
        for line in res:
            res2.append(line)
        return res2

    # def say(self, txt, sync=False):
    #     txte = txt.encode('utf8')
    #     args = []
    #     args.append(txte)
    #     self._picotts_exe(args, sync=sync)

    def synth_wav(self, txt):

        wav = None

        with tempfile.NamedTemporaryFile(suffix='.wav') as f:

            txte = txt.encode('utf8')

            args = ['-w', f.name, txte]

            self._picotts_exe(args, sync=True)

            f.seek(0)
            wav = f.read()

            logging.debug('read %s, got %d bytes.' % (f.name, len(wav)))

        return wav

    @property
    def voices(self):
        return VOICES

    @property
    def voice(self):
        return self._voice
    @voice.setter
    def voice(self, v):
        self._voice = v
