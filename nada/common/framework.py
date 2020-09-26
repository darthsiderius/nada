#!/usr/bin/env pypy

# -*- coding: utf-8 -*-

""" 
framework.py

This is the core of the nada command line tool domain logic. 
The tool is based on the open source 'click' packages. These packages are overridden and customized. This 
'wrapper' / layer also includes additionalfunctionality , such as similar command matching, 
allowing semicolon notation, dynamic loading of plugins and logging.

"""

import os
import sys
import click
import uuid
import logging
import difflib
from datetime import date
import traceback

class Singleton(type):
    """
    Singleton Meta class that can be used in other class types
    """
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class DynamicCommandHandler(click.MultiCommand, metaclass=Singleton):
    """
    DynamicCommandHandler is a singleton class that is injected into the click framework.
    It is customized to dynamically load plugins by name and callback defined in its
    __plugin__file.
    """

    def list_commands(self, env=None):
        """
        List_commands overrides the default implementation. This is responsible for
        listing out all plugins/base commands on the system.

        :result list of commands as strings
        """
        try:
            cmds = []
            # @TODO , refactor to config base path
            cmdFolder = os.path.abspath(os.path.join(os.path.dirname(__file__), "../plugins"))
            for filename in os.listdir(cmdFolder):
                if not filename.endswith("_"):
                    cmds.append(filename)
            cmds.sort()
            return cmds
        
        except:
            tb = traceback.format_exc()
            logging.error("Failed to retrieve a list of all plugins")
            logging.error(tb)
            return

    def suggest_similar_command(self,commandName,env=None):
        """
        Given a name and env (from parent), find a similar command to that of the misspelled 'commandName' param.

        :results prints out a ' did you mean command?' suggestion if a similar command is found
        @TODO - abstract print statement
        """
        similar = difflib.get_close_matches(commandName, self.list_commands(env))
        print("\nI could not find a matching command to : '" + commandName +"")
        # if a similar command exists
        if len(similar) >= 1 and similar[0] != commandName:
            print("Did you mean '" + similar[0] + "'?")
        else: 
            logging.warning("No matching command suggestion found") 

        #@TODO - create shutdown commands that have formatting
        exit("\n")

        
    def get_commands_file(self, commandName, fileName, attributes=None):
        """
        Given a command name, and a file name, retrieve a instance of the package.
        Optinally can use attributes to specify what attributes to include in package instance.

        :params commandName ( matches plugin folder 
        :params fileName to create instance
        :params optional attributes to include in instance
        :result returns instance of a package, which was dynamically imported
        """
        try:
            # if no defined attributes are defined, import all of them.
            if not attributes: attributes = ['*']
            mod = __import__(f"nada.plugins.{commandName}.{fileName}", globals(), locals(), attributes)
        except ImportError:
            tb = traceback.format_exc()
            logging.error("Failed to retrieve the command about : '" + commandName + "'")
            logging.error(tb)
            return
        logging.info("Dynamically retrieved a commands file : '" + fileName + "'")
        return mod

    def get_command(self, env, name):
        """
        Overrides the default multicommand get command. Given a name, it will get
        the entry point callback to the associated plugin.

        :params Name of the command. Ex : 'logs', 'about'
        :result Returns callback for entry into the plugin
        """
        try:
            pluginInfo = self.get_commands_file(name,"__plugin__",["__pluginEntryCallback__"])
            md = pluginInfo.__pluginEntryCallback__
        except:
            tb = traceback.format_exc()
            self.suggest_similar_command(name,env)
            logging.error("Failed to retrieve the command : '" + name + "'")
            logging.error(tb)
            return
        logging.info("Dynamically retrieved the command instance for : '" + name + "'")
        return md


# @TODO create parsers objects
#@TODO does not work with 2 semicolons
def transformSystemArgs():
    """
    Transform system arguments that have semicolon notation into
    a usable format to the click framework.  Ex nada logs:list.

    :params None, works on sys.args directly.
    :result Sy.argv are modified if they have semicolon notation. Ex nada logs:show -> nada logs show
    """
    newArgs = []
    for idx, arg in enumerate(sys.argv):
        if ":" in arg: 
            if arg.count(":") > 1: exit("SHOW SYNTAX PAGE")
            l,r = arg.split(":")
            if l and len(l) > 0: 
                newArgs.append(l)
                if r: newArgs.append(r)
            else:  exit("SHOW SYNTAX PAGE")
        else:   newArgs.append(arg)
    sys.argv = newArgs


class LoggingManager(metaclass=Singleton):
    """
    This is a singleton logging manager for the program. Once instance will be made per
    request. It allows for configuring the built in logger for clean logging messages
    and managing these logs. Currently, it is creating ('rolling') a new logfile per day.
    """
    def __init__(self):
        # @TODO change to param here for path
        self.logDirectory = os.path.dirname(os.path.realpath(__file__)) + "/../../logs/"
        self.requestId = None
        self.activeLogFile = None
        self.messageFormat = "%(asctime)-23s %(levelname)-8s @%(request_id)-8s %(filename)-15s %(funcName)-s -> %(message)s"
        self.dateFormat ="'%m/%d/%Y %I:%M:%S %p"
        self.logLevel = logging.INFO

    def setupLogger(self):
        """
        Initiate the custom logger formats, directory structure and active log file
        """
        self.assignRequestId()
        self.createLoggingDirectory()
        self.setActiveLogFile()
        
        old_factory = logging.getLogRecordFactory()

        def record_factory(*args, **kwargs):
            
            record = old_factory(*args, **kwargs)
            record.request_id = self.requestId
            return record

        logging.basicConfig(filename=self.activeLogFile, format=self.messageFormat, datefmt=self.dateFormat, level=self.logLevel)  
        logging.setLogRecordFactory(record_factory)
        logging.info("Logger initiated")

    def setActiveLogFile(self):
        """
        Set the active log file, based on todays date. Ex, 2020-09-25.log
        """
        today = str(date.today())
        self.activeLogFile = self.logDirectory + today + '.log'

    def createLoggingDirectory(self):
        """
        If the logging directory is not present, create it.
        """
        os.makedirs(os.path.dirname(self.logDirectory), exist_ok=True)

    def assignRequestId(self):
        """
        Assign a unique UUID to each log request so that we can identify which log messages
        occur with what command request. These are appended to each log statement. Ex: '@abs134'
        """
        self.requestId =  uuid.uuid4().hex[:6]

    def getCurrentRequestId(self):
        """
        Returns the current assigned request identifier
        """
        return self.requestId

    def getLogDirectoryPath(self):
        """
        Returns the logging directory path
        """
        return self.logDirectory

    def getActiveLogFile(self):
        """
        Returns the active log file currently being used for the day.
        """
        return self.activeLogFile