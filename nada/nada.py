#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
nada.py

Main entry point to the nada command line framework. It is responsible for program startup and request processing.
References: See documentation tab for detailed structure, dataflow and quickstart guidelines.

"""
__author__      = "Michael Siderius"
__version__     = "1.0.1"

import os
import sys 
import logging
from common.logging import setupLogger
from common.dynamicFactory import buildCommand
from common.dynamicFactory import getSimilarCommandSuggestion
from common.configManager import loadBaseConfigs
# can default in config file
# @TODO make these global for other commands can get it, which are failing
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
COMMANDS_DIR = BASE_DIR + "/commands/"
LOG_DIR = BASE_DIR + "/logs/"

def main():
    """
    Entry point to nada based tool. Sets configs, sets up logger, checks for updates and processes requests.

    :params No direct, args are recieved through sys. Configs are read directly. 
    :result All nada logic executed 
    """
    setupLogger()
    loadBaseConfigs()
    checkForUpdates()
    processRequest(sys.argv)
    shutdown()

def processRequest(args):
    """
    Parse the requested arguments, match to a command and execute domain logic.

    :params The command line arguments
    :result Run associated command to request. If no match - suggest a similar command
    """
    logging.info("processing request : '" + ' '.join(args) + "'")

    if len(args) == 1: helpExit() # visualMode
    command = buildCommand(args[1], args)
    if command: command.init()
    else: unrecognizedCommand(args[1]) 

def unrecognizedCommand(requestedCommand):
    """
    Suggest a similar command to the one requested ( which we could not find ). 
    Uses lavenstein distance for similarity matching.

    :params requested key command that was unable to be matched to runtime command
    :result Print out of the most similar commands.
    """
    logging.info("Suggesting help pages and similar commands to  '" + requestedCommand + "'")

    print("Woops! The '" + requestedCommand + "' command does not exist. See tool usage with 'nada help'.")
    suggestion = getSimilarCommandSuggestion(requestedCommand)
    if suggestion: print("Did you mean '" + suggestion + "'?")

def helpExit():
    logging.info("printing help instructions and exiting")
    exit(1)

def checkForUpdates():
    """
    Validate that the nada based command line tool is up to date. 

    :params None
    :result Checks if there is an update, if so prompt to update
    """
    logging.info("checking for updates...")

def shutdown():
    """
    Final shutdown of program. Ensure that everything is cleaned up.

    :params None
    :result None??
    """
    logging.info("Shutting down for current nada request")



if __name__ == "__main__":
    main()




