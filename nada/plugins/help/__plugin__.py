#!/usr/bin/env pypy
# -*- coding: utf-8 -*-
""" 
__plugin__.py

This is the 'help' plugins plugin file.
This includes required information to interface with the overarching framework.

"""
from .help import help
from nada.common.types import PluginStatus
from nada.common.types import PluginClassification

########################## REQUIRED FIELDS #########################################

__name__                    =   "help"
__description__             =   "Get help on how to use the tool and specific commands."
__version__                 =   "0.0.1"
__releaseDate__             =   "September 21, 2020"
__author__                  =   "Michael Siderius"
__contact__                 =   "michael.siderius@gmail.com"
__commit__                  =   "???"
__installRequires__         =   ["click"]
__frameworkVersion__        =   "00.0.000.001"
__pluginEntryCallback__     =   help
__pluginClassification__    =   PluginClassification.GENERAL
__status__                  =   PluginStatus.UNSTABLE

########################## OPTIONAL FIELDS ##########################################

__references__     =   "https://nada.com/commands/help"
__keywords__       =    ["boilerplate", "utility"]
__asciiLogo__ = """
             .--.           .---.        .-.
         .---|--|   .-.     | N |  .---. |~|    .--.
      .--|===|Ch|---|_|--.__| A |--|:::| |~|-==-|==|---.
      |%%|NT2|oc|===| |~~|%%| D |--|   |_|~|CATS|  |___|-.
      |  |   |ah|===| |==|  | A |  |:::|=| |    |GB|---|=|
      |  |   |ol|   |_|__|  |   |__|   | | |    |  |___| |
      |~~|===|--|===|~|~~|%%|~~~|--|:::|=|~|----|==|---|=|
      ^--^---'--^---^-^--^--^---'--^---^-^-^-==-^--^---^-'

"""
