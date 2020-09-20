#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
help.py


"""
__author__      = "Michael Siderius"
__version__     = "1.0.1"

from json import dumps
from .base import Base
# generate this?
class About(Base):
        
    # abstract method for retrieving the help page of a specific command
    def start(self):
        print("""           

        ABOUT PAGE
        """)

     # abstract method for retrieving the help page of a specific command
    def getHelp(self): 
        print("?")
    



    