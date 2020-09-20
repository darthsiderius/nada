#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
doctor.py


"""
__author__      = "Michael Siderius"
__version__     = "1.0.1"

from json import dumps
from .base import Base
from common.argParsing import CommandDispatcher

class Doctor(Base):
    def __init__(self,options):
        Base.__init__(self,options)
        self.dispatchMap = {'diagnose' : self.diagnose, 'repair' : self.repair, 'default' : self.diagnose}
        self.dispatcher = CommandDispatcher(self.dispatchMap, self.options)

    def start(self):
        print("cmd = doctor")
        self.dispatcher.execute()

    def diagnose(self):
        print("cmd = diagnose")


    def repair(self):
        print("cmd = repair")

    def getHelp(self): 
        return """
            nada doctor <optional>
            nada doctor diagnose
            nada doctor repair
            nada doctor complain
        """