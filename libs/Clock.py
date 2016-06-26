# -*- coding: utf-8 -*-

import time


class Clock(object):
    def __init__(self):
        self.start = None
        self.last_time = None

    def start_clock(self):
        self.start = time.time()
        self.last_time = self.start

    def get_elapsed_time(self):
        cur = time.time()
        delta = cur - self.last_time

        return delta

    def restart(self):
        cur = time.time()

        delta = cur - self.last_time
        self.last_time = cur

        return delta

