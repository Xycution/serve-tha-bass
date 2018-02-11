"""
Brief:
    select_action.py - Contains the functions necessary to act upon list items
        in various ways.

Description:
    Contains the functions necessary to act upon list items
        in various ways.

Methods:
    select()

Return Value(s):
    -

Example:
    -

Author(s):
    Mekyle Fernandes, Mykayla Fernandes
"""

import serve_tha_bass
import select_category
import list_item
import pymongo


def select():
    """
    Brief:
        select() - Asks the user to select an action.

    Description:
        Asks the user to select an action.

    Arguments:
        -

    Return Value(s):
        action string value

    Example:
        select() --> 'view'

    Author(s):
    Mekyle Fernandes, Mykayla Fernandes
    """

    print """\n
    --------------------------------------------------
    -- 1. View --  -- 2. Add --  -- 3. Change State --

    -- 4. Delete --  -- 5. Main Menu --  -- 6. Quit --
    --------------------------------------------------
    """
    action = raw_input('Please select an action number:')

    if action == '1':
        action = 'view'
        print "You have selected: " + action
        return action
    elif action == '2':
        action = 'add'
        print "You have selected: " + action
        return action
    elif action == '3':
        action = 'state'
        print "You have selected: " + action
        return action
    elif action == '4':
        action = 'delete'
        return action
    elif action == '5':
        action = 'menu'
        print "You have selected: " + action
        return action
    elif action == '6':
        action = 'quit'
        print "You have selected: " + action
        return action
    else:
        print action + " is an invalid input."
        return False


def view(category):
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
    Mekyle Fernandes, Mykayla Fernandes
    """
    # not sure if we need this function yet
    pass



def add(category):
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
    # not sure if we need this function yet
    pass



# def change_state(list_item, category, current_state, new_state)

# def delete(list_item)
