#!/usr/bin/env python

# free live hosting
# https://mlab.com/plans/pricing/#plan-type=sandbox

# pymongo tutorial
# https://api.mongodb.com/python/current/tutorial.html

# mongo gui
# https://robomongo.org/

"""
Brief:
    serve_tha_bass.py - Contains the primary flow of the application execution.

Description:
    A command line application to help track video games, anime, and manga

Methods:
    startup(), choose(), execute(), main()

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
import pymongo



def startup():
    """
    Brief:
        startup() - These are the first things to appear when launching the application

    Description:
        Asks the user to select a category

    Arguments:
        -

    Return Value(s):
        category string

    Example:
        startup() --> 'anime'

    Related:
        choose()

    Author(s):
        Mekyle Fernandes, Mykayla Fernandes
    """


    category = select_category.select()

    return category


def choose():
    """
    Brief:
        choose() - asks the user to select an action to perform

    Description:
        Asks the user to select an action to perform

    Arguments:
        -

    Return Value(s):
        action string

    Example:
        choose() --> 'view'

    Related:
        startup()

    Author(s):
        Mekyle Fernandes, Mykayla Fernandes
    """

    action = select_action.select()
    return action


def execute(category, action):
    """
    Brief:
        execute(category, action) - executes the selected action on
            the selected category.

    Description:
        Executes the selected action on the selected category.

    Arguments:
        category - (Required) The category to perform the action on.
        action   - (Required) The action to perform on the category

    Return Value(s):
        True on success, False on failure

    Example:
        execute(anime, view) --> anime lists

    Related:
        -

    Author(s):
        Mykayla Fernandes
    """
    # get the category class and call its action function
    # where category().action() is the same as anime().view()
    return select_category.get_class(category).get_func(action)


def main():
    """
    Brief:
        main() - The main method. Executes the serve-tha-bass application.

    Description:
        Launches the application, asks the user what they want to do,
            and executes the corresponding actions.

    Arguments:
        -

    Return Value(s):
        True on success, False on failure

    Example:
        main() --> application launches

    Author(s):
        Mykayla Fernandes, Mekyle Fernandes
    """

    #execute application
    execute(startup(), choose())

    # end
    sys.exit(0)


if  __name__ =='__main__':
    main()
