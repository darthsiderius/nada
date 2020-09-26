#!/usr/bin/env pypy

# -*- coding: utf-8 -*-

""" 
logs.py

"""
import os
import sys
import click
import subprocess
import logging
from nada.common.framework import LoggingManager

@click.group(short_help="Shows file changes.", invoke_without_command=True)
def logs():
    """
    cli
    
    :params
    :result 
    """

@logs.command()
def show(): 
    """
    show

    :params
    :result 
    """
    logFile = LoggingManager().getActiveLogFile()

    print("\nShowing recent logs \n ... \n")
    os.system("tail -50 " + logFile )
    print("\n")
    logging.info("Executed logs show command")

@logs.command()
def list(): 
    """
    list

    :params
    :result 
    """

    logDir = LoggingManager().getLogDirectoryPath()
    logcount = os.popen("find " + logDir + " -iname *.log | wc -l").read()
    osCmd = "cd " + logDir + " && ls -lota *.log  |  grep -P '.{0,10}.log' --color "
    logging.info("Executed logs list command. cmd = " + osCmd)

    print("\nDirectory:   " + logDir)
    print("Log Count:   " + str(logcount))
    os.system(osCmd)
    print("\n")


@logs.command()
def clean(): 
    """
    clean

    :params
    :result 
    """
    if click.confirm('\nAre you sure you want to delete all log files?'):
        logDir = LoggingManager().getLogDirectoryPath()
        osCmd = "rm " + logDir + "/*.log"
        os.system(osCmd)
        print("\nAll log files have been deleted...\n")
        logging.info("Executed logs clean command. cmd = " + osCmd)
    else:
        print("Aborting clean command. \n")

@logs.command()
@click.argument('phrase')
def search(phrase): 
    """
    search

    :params
    :result 
    """
    print("\n\nSearching for logs entries referring to '" + phrase +"'...\n")
    logDir = LoggingManager().getLogDirectoryPath()
    osCmd = "cd " + logDir + " && grep -ir " + phrase + " --color "
    os.system(osCmd)
    print("\n")
    logging.info("Executed logs search command. cmd = " + osCmd)

