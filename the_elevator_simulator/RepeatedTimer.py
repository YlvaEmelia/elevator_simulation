# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 21:09:27 2015

@author: Ylva Lindberg
"""

from threading import Timer

class RepeatedTimer(object):
# Source: http://stackoverflow.com/questions/3393612/run-certain-code-every-n-seconds
    def __init__(self, interval, function, *args, **kwargs):
        self._timer = None
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self._timer = Timer(self.interval, self._run)
        #self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)
        
    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False
    
    def isRunning(self):
        return self.is_running