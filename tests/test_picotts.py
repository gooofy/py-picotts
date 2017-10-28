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

import unittest
import logging
import StringIO
import wave

from picotts import PicoTTS

class TestPicoTTS (unittest.TestCase):

    def test_voices(self):
        picotts = PicoTTS()

        voices = picotts.voices
        self.assertGreater (len(voices), 5)

    def test_synth_wav(self):

        picotts = PicoTTS(voice='en-US')
        wavs = picotts.synth_wav('Hello World!')
        wav = wave.open(StringIO.StringIO(wavs))
        
        self.assertEqual   (wav.getnchannels(),     1)
        self.assertEqual   (wav.getframerate(), 16000)
        self.assertGreater (wav.getnframes(),   20000)

    def test_synth_wav_de(self):

        picotts = PicoTTS(voice='de-DE')
        wavs = picotts.synth_wav('Hallo Welt!')
        wav = wave.open(StringIO.StringIO(wavs))
        
        self.assertEqual   (wav.getnchannels(),     1)
        self.assertEqual   (wav.getframerate(), 16000)
        self.assertGreater (wav.getnframes(),   20000)

if __name__ == "__main__":

    # logging.basicConfig(level=logging.ERROR)
    logging.basicConfig(level=logging.DEBUG)

    unittest.main()

