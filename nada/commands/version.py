#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
help.py


"""
__author__      = "Michael Siderius"
__version__     = "1.0.1"

from json import dumps
from .base import Base
from common.asciiArt import *
from common.dynamicFactory import buildCommand
from common.dynamicFactory import getSimilarCommandSuggestion
# generate this?
class Version(Base):
    def start(self):
        print("Nada 1.0.1 (git revision 53104; last commit 2017-08-28)")
     # abstract method for retrieving the help page of a specific command
    def getHelp(self): 
        print("?")
    



    