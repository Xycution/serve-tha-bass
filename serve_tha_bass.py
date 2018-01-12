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

import select_action
import select_category
import list_item


sel_cat = select_category.list.select()
#choice = something.select() ## << This isn't being recognized when running for some reason

def startup(): # this is the first thing to show when running
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
    
    
    select_category.list.select()

def choose(sel_cat):
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
    select_action.select.select()


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
    startup()

    # ask user what they want to do
    choose(sel_cat)

    # execute actions

    # end


if  __name__ =='__main__':main()
