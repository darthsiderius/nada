#!/usr/bin/env pypy
# -*- coding: utf-8 -*-
""" 
__plugin__.py

This is the 'logs' plugins required __plugin__ file.
This includes required information to interface with the overarching framework.

Note: Reference material on __plugin__ files at @TODO ?

"""
from .logs import logs
from nada.common.types import PluginStatus
from nada.common.types import PluginClassification

########################## REQUIRED FIELDS #########################################

__name__                    =   "logs"
__description__             =   "View and manage the tools logging files"
__version__                 =   "0.0.1"
__releaseDate__             =   "September 21, 2020"
__author__                  =   "Michael Siderius"
__contact__                 =   "michael.siderius@gmail.com"
__commit__                  =   "???"
__installRequires__         =   ["click"]
__frameworkVersion__        =   "00.0.000.001"
__pluginEntryCallback__     =   logs
__pluginClassification__    =   PluginClassification.GENERAL
__status__                  =   PluginStatus.UNSTABLE

########################## OPTIONAL FIELDS ##########################################

__references__     =   "https://nada.com/commands/logs"
__keywords__       =    ["boilerplate", "utility", "logging"]
__asciiLogo__ = """
            888                                        
            888                                        
            888                                        
            888 .d88b.  .d88b.  .d88b.  .d88b. 888d888 
            888d88""88bd88P"88bd88P"88bd8P  Y8b888P"   
            888888  888888  888888  88888888888888     
            888Y88..88PY88b 888Y88b 888Y8b.    888     
            888 "Y88P"  "Y88888 "Y88888 "Y8888 888     
                            888     888                
                    Y8b d88PY8b d88P                
                        "Y88P"  "Y88P"       
"""
