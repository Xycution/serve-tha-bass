"""
Brief:
    select_category.py - Contains the class definitions for all the categories
        and the functions needed to manipulate them.

Description:
    Contains the class definitions for all the categories
        and the functions needed to manipulate them.

Methods:
    select(), get_class()

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
        select() - Asks user to select a category.

    Description:
        Asks user to select a category.

    Arguments:
        -

    Return Value(s):
        category string on success, False on failure

    Example:
        select() --> 'anime'
    
    Related:
        select_action.select()

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
    """
    Brief:
        get_class(category) - Returns an instance of the category class
            it was given.

    Description:
        Returns an instance of the category class it was given.

    Arguments:
        category - (Required) the category name string

    Return Value(s):
        category class on success, False on failure

    Example:
        get_class(anime) --> anime()
    
    Related:
        get_func(action)

    Author(s):
    Mekyle Fernandes, Mykayla Fernandes
    """
    if category == 'anime':
        return anime()

        
class anime():
    """
    Brief:
        anime() - The anime class.
    
    Description:
        Contains the anime class definition.
    
    Method(s):
        view(), get_func()
    
    Return Value(s):
        -
    
    Example:
        -
    
    Author(s):
    Mykayla Fernandes, Mekyle Fernandes
    """
    backlog = []  # list_item objects in the backlog state
    in_progress = []  # list_item objects in the in_progress state
    complete = []  # list_item objects in the complete state
    
    # add functions here
    def __init__(self):
        pass
    
    
    def view(self):
        print "viewing the anime class"
    
    
    def get_func(self, action):
        if action == 'view':
            return self.view()
    
class manga():
    """
    Brief:
        manga() - The manga class.
    
    Description:
        Contains the manga class definition.
    
    Method(s):
        -
    
    Return Value(s):
        -
    
    Example:
        -
    
    Related:
        games(), anime()
    
    Author(s):
        Mykayla Fernandes
    """
    backlog = []  # list_item objects in the backlog state
    in_progress = []  # list_item objects in the in_progress state
    complete = []  # list_item objects in the complete state
    
    # add functions here
    
    
class games():
    """
    Brief:
        games() - The games class.
    
    Description:
        Contains the game class definition.
    
    Method(s):
        -
    
    Return Value(s):
        -
    
    Example:
        -
    
    Related:
        anime(), manga()
    
    Author(s):
        Mykayla Fernandes
    """
    backlog = []  # list_item objects in the backlog state
    in_progress = []  # list_item objects in the in_progress state
    complete = []  # list_item objects in the complete state
    
    # add functions here
