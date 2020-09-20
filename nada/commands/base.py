#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The base command."""
import logging
from common.logging import setupLogger
from common.argParsing import CommandDispatcher

class Base(object):
    """A base command."""

    def __init__(self, options, *args, **kwargs):
        self.options = options
        self.args = args
        self.kwargs = kwargs
        
        # logging in commands not working
        # logging.info("Starting '" + self.args[1] + "' command. Arguments = '" + ' '.join(self.options) + "'")
    # entry point for global command execution
    def init(self):
        # start
        # prereqs
        self.start()
    
    # @Required
    # abstract method for sub command execution
    def start(self): raise NotImplementedError('Error: the start() method must be implemented in commands')
   
    # @Required
    # abstract method for retrieving the help page of a specific command, include options for the tool
    def getHelp(self): raise NotImplementedError('Error: the help() method must be implemented in commands')
    
    #@Optional
    def visualMode(self): pass