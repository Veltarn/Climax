# -*- coding: utf-8 -*-

import sys
from Core.Clock import Clock

class ProgressBar(object):
    def __init__(self, min=0, max=100, size=10):
        self._minValue = min
        self._maxValue = max
        #Size in character, not pixel
        self._size = size
        self._value = 0
        self._last_value = 0
        self.items_per_second = 0
        self._displayedCharacter = "="
        self.clock = Clock()
        self.clock.start_clock()

    @property
    def minValue(self):
        return self._minValue

    @minValue.setter
    def minValue(self, value):
        self._minValue = value

    @minValue.deleter
    def minValue(self):
        del self._minValue

    @property
    def maxValue(self):
        return self._maxValue

    @maxValue.setter
    def maxValue(self, value):
        self._maxValue = value

    @maxValue.deleter
    def maxValue(self):
        del self._maxValue

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @size.deleter
    def size(self):
        del self._size

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        tmp = self._value
        self._value = v
        self._updateBar(tmp, v)

    @value.deleter
    def value(self):
        del self._value

    @property
    def displayedCharacter(self):
        return self._displayCharacter

    @displayedCharacter.setter
    def displayedCharacter(self, value):
        if len(value) > 1:
            self._displayedCharacter = value[0]
        else:
            self._displayedCharacter = value

    @displayedCharacter.deleter
    def displayedCharacter(self):
        del self._displayedCharacter

    def _updateBar(self, old_value, new_value):
        elapsed_time = self.clock.get_elapsed_time()
        if elapsed_time >= 1.0:
            self.items_per_second = new_value - self._last_value
            self._last_value = new_value
            self.clock.restart()

        nbCharsToDisplay = int(round(self._value * self._size / self._maxValue))
        emptyChars = self._size - nbCharsToDisplay
        pCentValue = self._value * 100 / self._maxValue
        bar = "[" + self._displayedCharacter * nbCharsToDisplay + "" + " " * emptyChars  + "] " + str(pCentValue) + "% (" + str(self.items_per_second) + " items per second)"

        sys.stdout.write(bar + "\r" )
        sys.stdout.flush()