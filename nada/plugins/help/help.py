#!/usr/bin/env pypy

import click


@click.group(name = "help", short_help="Get help", invoke_without_command=True)
def help():
    """
    Help
    
    :params
    :result 
    """

    print("HELP")   



