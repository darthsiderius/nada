#!/usr/bin/env pypy
# -*- coding: utf-8 -*-
""" 
basicAboutFormatter.py


"""
from .aboutFormatter import AboutFormatter

class BasicAboutFormatter(AboutFormatter):
    def __init__(self, keywordColor = None):
        self.keywordColor = None
        self.content = None


    def print(self): 
        if not self.content: 
            logging.warning("No content to format in the about formatter.")


        print("\n ****************************************************************************")
        print(" " + self.content.__asciiLogo__)
        print(" NAME:            " + self.content.__name__)
        print(" BRIEF:           " + self.content.__description__)
        print(" PLUGIN TYPE:     " + self.content.__pluginClassification__.value )
        print(" STATUS:          " + self.content.__status__.value )
        print("")
        print(" VERSION:         " + self.content.__version__)
        print(" PUBLISH DATE:    " + self.content.__releaseDate__)
        print(" COMMIT:          " + self.content.__commit__)
        print(" REQUIRES:        " + ", ".join(self.content.__installRequires__))
        print("")
        print(" AUTHOR:          " + self.content.__author__)
        print(" CONTACT:         " + self.content.__contact__)
        print(" REFERENCES:      " + self.content.__references__)
        print(" KEYWORDS:        " + ", ".join(self.content.__keywords__))
        print("\n ****************************************************************************")


    def loadPluginPage(self, pluginInstance): 
        self.content = pluginInstance

    def loadNadaInfo(self, nadaAboutInstance):
        return None



