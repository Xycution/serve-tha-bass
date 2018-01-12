#!/usr/bin/env python

"""
Brief:
    serve_tha_bass.py - Contains the primary flow of the application execution.

Description:
    A command line application to help track video games, anime, and manga

Methods:
    main()

Return Value(s):
    True on Success, False on Failure

Example:
    >python serve-tha-base.py --> application launches

Author(s):
    Mekyle Fernandes, Mykayla Fernandes
"""

import sys

import select_action
import select_category
import list_item



# sel_cat = select_category.list.select()
#choice = something.select() ## << This isn't being recognized when running for some reason

def startup(): # this is the first thing to show when running
    """
    Brief:
        startup() - These are the first things to appear when launching the application

    Description:
        -

    Arguments:
        -

    Return Value(s):
        -

    Example:
        -

    Author(s):
        Mekyle Fernandes, Mykayla Fernandes
    """
    
    
    category = select_category.select()
    
    return category
    

def choose():
    """
    Brief:
        -

    Description:
        -

    Arguments:
        -

    Return Value(s):
        -

    Example:
        -
    
    Author(s):
        -
    """
    
    action = select_action.select()
    return action

    
def execute(category, action):
    # get the category class and call its action function
    return
    

def main():
    """
    Brief:
        -

    Description:
        -

    Arguments:
        -

    Return Value(s):
        -

    Example:
        -

    Author(s):
        -
    """
    # launch application -- startup()
    # ask user what they want to do -- select_action.select()
    # execute actions
    execute(startup(), choose())

    # end
    sys.exit(0)


if  __name__ =='__main__':
    main()
