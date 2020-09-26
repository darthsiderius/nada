#!/usr/bin/env pypy

import click
import logging
from nada.common.framework import DynamicCommandHandler
from .formatters.basicAboutFormatter import BasicAboutFormatter

@click.command(short_help="Shows about for plugins")
@click.argument('detailed', default=False)
def about(detailed):
    """
    cli
    
    :params
    :result 
    """
    if detailed: 
        pluginPage = DynamicCommandHandler().get_commands_file(detailed, "__plugin__")
        if not pluginPage: 
            logging.warning("About command failed to load package instance for :" + str(detailed))      
            DynamicCommandHandler().suggest_similar_command(detailed)
        # check version to get most recent formatter or adapter? , rotate formats based on ascii size?
        fmter = BasicAboutFormatter()
        fmter.loadPluginPage(pluginPage)
        fmter.print()
    else: 
        print("Show NADA ABOUT")
        # @TODO = create about page for nada framework? how does this work with about formatter that takes pluginPage?
        # or automatically detect it????

        printJet()

# @TODO - move when config file is doen?
def printJet():

    print("""           

               \ /                                          \  /
              --o--           `\\            //'      .____-/.\-____.
                                \\          //             ~`-'~
                                 \\. __-__.//
                       ___/-_.-.__`/~    ~\\'__.-._-\___                    
.|.       ___________.'__/__ ~-[ \.\'-----'/./ ]-~ __\__`.___________        .|.
~o~~~~~~~--------______-~~~~~-_/_/ |   .   | \_\_-~~~~~-______--------~~~~~~~o~
' `               + + +  (X)(X)  ~- \__ __/--~  (X)(X)  + + +               ' `
                             (X) `/.\\' ~ `/.\\' (X)  
                                 "\_/"   "\_/"

        
                                    About Nada
        
        
        
        
        
        
        """)
