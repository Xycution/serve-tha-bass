"""
Brief:
    select_category.py - Contains the class definitions for all the categories
        and the functions needed to manipulate them.

Description:
    -

Methods:
    -

Return Value(s):
    -

Example:
    -

Author(s):
    Mekyle Fernandes, Mykayla Fernandes
"""

import serve_tha_bass
import select_action
import list_item

    
def select():
    """
    Brief:
    -

    Description:
    -

    Arguments:
    -

    Return Value(s):
    category on success, False on failure

    Example:
    -

    Author(s):
    Mekyle Fernandes, Mykayla Fernandes
    """

    print """\n
    \n
      -----------          -----------------         ------------
    -- 1. Anime   --     -- 2. Video Games  --     --  3. Manga  --
      -----------          -----------------         ------------

    """
    category = raw_input('Please select a category number:\n')
    category = int(category)  # convert input from string to an integer

    # make sure user input is an integer << This accepts the input but repeats 1 times
    # before moving to next function.
    if category == 1:
        category = 'anime'
        print "You have selected: " + category
        return category
    elif category == 2:
        category = 'games'
        print "You have selected: video " + category
        return category
    elif category == 3:
        category = 'manga'
        print "You have selected: " + category
        return category
    else:
        print category + " is not a valid input."
        return False

    
def get_class(category):
    if category == 'anime':
        return anime()

        
class anime():
    """
    Brief:
    -
    
    Description:
    -
    
    Method(s):
    -
    
    Return Value(s):
    -
    
    Example:
    -
    
    Author(s):
    -
    """
    backlog = []  # list_item objects in the backlog state
    in_progress = []  # list_item objects in the in_progress state
    complete = []  # list_item objects in the complete state
    
    # add functions here
    def get_func(action):
        if action == 'view':
            return view()
    
    def view():
        return "viewing the anime class"
    
    
class manga():
    """
    Brief:
    -
    
    Description:
    -
    
    Method(s):
    -
    
    Return Value(s):
    -
    
    Example:
    -
    
    Author(s):
    -
    """
    backlog = []  # list_item objects in the backlog state
    in_progress = []  # list_item objects in the in_progress state
    complete = []  # list_item objects in the complete state
    
    # add functions here
    
    
class videoGames():
    """
    Brief:
    -
    
    Description:
    -
    
    Method(s):
    -
    
    Return Value(s):
    -
    
    Example:
    -
    
    Author(s):
    -
    """
    backlog = []  # list_item objects in the backlog state
    in_progress = []  # list_item objects in the in_progress state
    complete = []  # list_item objects in the complete state
    
    # add functions here
