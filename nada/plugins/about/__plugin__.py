#!/usr/bin/env pypy
# -*- coding: utf-8 -*-
""" 
__plugin__.py

This is the 'about' plugins plugin file.
This includes required information to interface with the overarching framework.

"""
from .about import about
from nada.common.types import PluginStatus
from nada.common.types import PluginClassification

########################## REQUIRED FIELDS #########################################

__name__                    =   "about"
__description__             =   "View information about plugins, such as versions and author!"
__version__                 =   "0.0.1"
__releaseDate__             =   "September 21, 2020"
__author__                  =   "Michael Siderius"
__contact__                 =   "michael.siderius@gmail.com"
__commit__                  =   "???"
__installRequires__         =   ["click", "pypy"]
__frameworkVersion__        =   "00.0.000.001"
__pluginEntryCallback__     =   about
__pluginClassification__    =   PluginClassification.GENERAL
__status__                  =   PluginStatus.UNSTABLE

########################## OPTIONAL FIELDS ##########################################

__references__     =   "https://nada.com/commands/about"
__keywords__       =    ["boilerplate", "utility", "logging"]
 #@TODO -- need to figuer ascii art 
__asciiLogo__ = """
                  ___                          (_)
                _/XXX\\
 _             /XXXXXX\_                                    __
 X\__    __   /X XXXX XX\                          _       /XX\__      ___
     \__/  \_/__       \ \                       _/X\__   /XX XXX\____/XXX\\
   \  ___   \/  \_      \ \               __   _/      \_/  _/  -   __  -  \__/
  ___/   \__/   \ \__     \\__           /  \_//  _ _ \  \     __  /  \____//
 /  __    \  /     \ \_   _//_\___     _/    //           \___/  \/     __/
 __/_______\________\__\_/________\_ _/_____/_____________/_______\____/_______
                                   /|\\
                                  / | \\
                                 /  |  \\
                                /   |   \\
                               /    |    \\             ABOUT
                              /     |     \\
                             /      |      \\

"""