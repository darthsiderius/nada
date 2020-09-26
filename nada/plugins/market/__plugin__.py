#!/usr/bin/env pypy
# -*- coding: utf-8 -*-
""" 
__plugin__.py

This is the 'plugins' plugins plugin file.
This includes required information to interface with the overarching framework.

"""
from .market import market
from nada.common.types import PluginStatus
from nada.common.types import PluginClassification

########################## REQUIRED FIELDS #########################################

__name__                    =   "market"
__description__             =   "Browse new plugins, publish your own or manage currently installed."
__version__                 =   "0.0.1"
__releaseDate__             =   "September 21, 2020"
__author__                  =   "Michael Siderius"
__contact__                 =   "michael.siderius@gmail.com"
__commit__                  =   "???"
__installRequires__         =   ["click"]
__frameworkVersion__        =   "00.0.000.001"
__pluginEntryCallback__     =   market
__pluginClassification__    =   PluginClassification.GENERAL
__status__                  =   PluginStatus.UNSTABLE

########################## OPTIONAL FIELDS ##########################################

__references__     =   "https://nada.com/commands/help"
__keywords__       =    ["boilerplate", "utility"]
__asciiLogo__ = """


"""
