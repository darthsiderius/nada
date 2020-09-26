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

ANYTHING EXTERNAL TO MACHINE

"""
@click.group(name = "market", short_help="Manage plugins", invoke_without_command=True)
def market():
    """
    market
    
    :params
    :result 
    """
    print("""
                    __               _|_
                   |+-==|         .'.':`.`.
              |    |+--=|        / /  |  \ \\
             /'\   '+ -=|        ^^^^^^^^^^^
            //|\\      =|   &C   O__u |  u O~
          O ^^^^^           /\_u/\/uuu|uuu\/\\
     &C  /|\_@|   C__@     /)  ( '--------' ,|
     /\_ \@@@@|@@\/\      /_|   \_\   |    /_|           |
    ( ( `,o--------')      /|   / |  /|\   |\           /'\\
    /__\ /`'  |   <|                        _|_        //|\\
    /|  />   /|\   \`                    .'.':`.`.     ^^^^^
                                        / /  |  \ \    %%|%%  O
                     _|_                ^^^^^^^^^^^   %%%|%%%_/\\
                  .'.':`.`.             C_/  |       '-------'  )
                 / /  |  \ \         d}<|8888|888  {b    |     / \\
                 ^^^^^^^^^^^     _888/\_88888|8888_/\   /|\    |  \\
          ~C          |   O      '--|(-------+----' ,|
          /),\_ O     | \/|\/    |  |_\ | \  |    |/_(
       o /( )  /|\####|###### O  |   | \    /|\   | \\
      (`' )_(  \|'-----------'/\\
      /\  / |   |\    |  _o  /  )
  ejm           |/   /|\  (`'  /|
                          />   \ \\
    
    """)
    print("\nWelcome to the plugin marketplace! ")
    print("You can browse plugins to add to your local tool or publish your own!\n\n")
    print("If you ever need help, visit the help pages 'nada market:help' \n\n")
    print("market PAGE")  

@market.command()
def search(): 
    """


    :params
    :result 
    """
    print(" BROWSING MARKET ")   

@market.command()
def browse(): 
    """


    :params
    :result 
    """
    print(" BROWSING MARKET ")   

@market.command()
def install(): 
    """


    :params
    :result 
    """
    print(" install") 

@market.command()
def publish(): 
    """


    :params
    :result 
    """

    print("market publish") 

