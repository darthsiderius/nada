#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import difflib
import traceback
import importlib
import logging
import pkgutil

def buildCommand(classname, options=None):
    try:  
        cls = getattr(importlib.import_module("commands." + classname.lower()), classname.title())
        instance = cls(options)
        return instance
    except:  
        trace = traceback.format_exc()
        logging.error("Could not match requested command. Request='" + str(classname or "") + "' error=" + trace)
        return None

def getAllCommands():
    # @TODO - change to config path, fails when not in sub dir
    allCommands = [name for _, name, _ in pkgutil.iter_modules(['../commands'])]
    if "base" in allCommands: allCommands.remove("base")
    logging.info("Retrieved all possible commands = " + ",".join(allCommands))
    return allCommands

def getSimilarCommandSuggestion(classname):
    allCommands = getAllCommands()
    similar = difflib.get_close_matches(classname, allCommands)
    # if a similar command exists
    if len(similar) >= 1 :
        logging.info("Found similar command '" + similar[0] + "' for request '" + classname + "'") 
        return similar[0]
    else: 
        logging.info("No matching command suggestion found") 
        return None