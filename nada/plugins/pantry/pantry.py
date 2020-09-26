#!/usr/bin/env pypy

import click
"""
Plugins:info app ?? repetative?
Plugins:list
Plugins:remove app 
          Have required in config file
Plugins:install app
Plugins:market:search 
Plugins:create name
          - creates template, logging etc.
Plugins:publish name
          Don’t have permissions to publish mandatory app  
Plugins:update

maybe keep plugins to managing own plugins locally
and have  a 'market plugin' for external

... where should 'create go'?


ANYTHING LOCAL ON MACHINE

"""

@click.group(name = "pantry", short_help="Manage plugins", invoke_without_command=True)
def pantry():
    """
    Plugins
    
    :params
    :result 
    """

    print("pantry PAGE")   


@pantry.command()
def list(): 
    """


    :params
    :result 
    """
    print(" LIST")   

@pantry.command()
def trash(): 
    """


    :params
    :result 
    """
    print(" trash") 

@pantry.command()
def create(): 
    """


    :params
    :result 
    """
    print("pantry create") 

@pantry.command()
def update(): 
    """

    :params
    :result 
    """
    print("pantry update") 
