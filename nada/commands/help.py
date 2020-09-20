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
class Help(Base):
    # @TODO make the help pages a template object for all same format
    # abstract method for retrieving the help page of a specific command
    def start(self):
        if len(self.options) >= 3: self.printCommandSpecificHelp(self.options[2])
        else: self.printOverviewHelpPage()

    def printOverviewHelpPage(self):
        printJet()
        print("""           
                                   General Help

        ABOUT:      
                    NADA is a command line framework tool which allows for 
                    rapid, scalable development of python command line tools.
        
        SYNTAX:     
                    nada <command> [--options]
                    where:
                        <*> = required
                        [*] = optional 

        EXAMPLES:       
                    nada about
                    nada help [command]

        COMMANDS:
                    about   -   Learn more about NADA, the authors and how it was built.
                    doctor  -   Diagnose, detect and resolve tool issues.
                    help    -   View usage, references and points of contact.
                    logs    -   Search, view and manage NADA logs.
                    update  -   Update NADA to recieve the most up to date features.
        REFERENCE:
                    Visit https://www.nada.com for online resources.
                    For design documentation, see the SDD in base directory.

        CONTACTS:  
                    Michael.siderius@gmail.com
                    JaneDoe1@foxmail.com 

        """)
    
    def printCommandSpecificHelp(self, command):
        # try to create a command instance of specificed command
        # if successful, print out its help page
        # if not, attempt to get the most similar command and retry to print that help page
        # if similar commands help map doesnt exist, print out overview help page
        cmdInstance = buildCommand(command)
        if cmdInstance: print(cmdInstance.getHelp())
        else: 
            print("I could not find a detailed help page for the command '" + command + "'.")
            suggestion = getSimilarCommandSuggestion(command)
            if suggestion: 
                print("Did you mean ' nada help " + suggestion + "'?")
                self.printCommandSpecificHelp(suggestion)
            else: self.printOverviewHelpPage()

     # abstract method for retrieving the help page of a specific command
    def getHelp(self): 
        print("?")
    



    