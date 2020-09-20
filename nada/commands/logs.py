#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
help.py


"""
__author__      = "Michael Siderius"
__version__     = "1.0.1"

from json import dumps
from .base import Base
import logging
from common.argParsing import CommandDispatcher
from common.logging import listLogFiles
from common.logging import deleteAllLogs
from common.logging import showLogs
from common.logging import searchLogs
# generate this?
class Logs(Base):
    def __init__(self,options):
        Base.__init__(self,options)
        self.dispatchMap = {'-list' : listLogFiles, '-show' : showLogs, '-clean' : deleteAllLogs, '-search' : searchLogs }
        self.dispatcher = CommandDispatcher( self.dispatchMap, self.options)

    def start(self): 
        self.dispatcher.execute()

     # abstract method for retrieving the help page of a specific command
    def getHelp(self): 
        return """
            nada logs <--type>
            nada logs -show 
            nada logs -search "Request" -- use grep and color
            nada logs -list
            nada logs -clean
        """
