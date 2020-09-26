#!/usr/bin/env pypy
# -*- coding: utf-8 -*-
""" 
nada.py

This is the programs main file and entry point. It is responsible for forwarding requests to the 
customized click framework and doing prerequisite setup - such as checking for
updates and setting up the global logger.

"""

import click
import logging
from .common.framework import LoggingManager
from .common.framework import DynamicCommandHandler
from .common.framework import transformSystemArgs

def init():
    """
    This is the entry point into the nada command tool and will invoke all necessary logic.
    The entry point is defined in the setup.py file.

    :params None
    :result request is processed
    """
    LoggingManager().setupLogger()
    transformSystemArgs()
    processRequest()

    # @TODO - add update check here?


@click.group(cls=DynamicCommandHandler,  invoke_without_command=True)
def processRequest():
    """
    Suggest a similar command to the one requested ( which we could not find ). 
    Uses lavenstein distance for similarity matching.

    :params requested key command that was unable to be matched to runtime command
    :result Print out of the most similar commands.
    """
    logging.info("Initiating forwarding of request to associated plugin.")

