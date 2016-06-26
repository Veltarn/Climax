#-*- coding utf-8 -*-

import time
import threading

class Timer:
	def __init__(self, tempo, callback, *args, **kwargs):
		self._timer = None
		self._tempo = tempo
		self._callback = callback
		self._args = args
		self._kwargs = kwargs

	def _run(self):
		self._timer = threading.Timer(self._tempo, self._run)
		self._timer.start()
		self._callback(*self._args, **self.__kwargs)

	def start(self):
		self._timer = threading.Timer(self._tempo, self._run)
		self._timer.start()

	def stop(self):
		self._timer.cancel()
