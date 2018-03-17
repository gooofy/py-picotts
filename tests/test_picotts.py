#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#
# Copyright 2017 Guenter Bartsch
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
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

