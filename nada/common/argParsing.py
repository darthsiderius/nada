#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
help.py


"""
__author__      = "Michael Siderius"
__version__     = "1.0.1"

OPTION_PREFIX = "--"

def getFirstOption(args):
    if len(args) > 3: 
        return args[3].strip(OPTION_PREFIX)

class CommandDispatcher(object):
    def __init__(self, dispatchMap, args):
        self.args = args
        self.dispatchMap = dispatchMap
        self.optionsMap = None

    def hasOptions(self):
        if len(self.args) > 2: return True
        return False

    def inDispatchMap(self,fnc):
        if fnc in self.dispatchMap: return True
        else: return False

    def ignoreOptionPrefix(self):
        return True
# what is default?
    def execute(self):
        print(self.args)
        # no options given and there is a default cmd to execute based on key cmd
        if not self.hasOptions() and self.inDispatchMap(self.args[1]): 
            func = self.dispatchMap[self.args[1]]

        elif self.hasOptions() and self.inDispatchMap(self.args[2]): 
            func = self.dispatchMap[self.args[2]]
        
        elif "default" in self.inDispatchMap:
            func = self.dispatchMap["default"]

        else: exit(1)

        func()

        
        





