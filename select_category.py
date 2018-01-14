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
from list_item import listItem


    
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
      -----------          -----------------         ------------         -----------
    -- 1. Anime   --     -- 2. Video Games  --     --  3. Manga  --     --   4. Exit   --
      -----------          -----------------         ------------         -----------

    """
    category = raw_input('Please select a category number:\n')
    category = int(category)  # convert input from string to an integer

    # make sure user input is an integer
    
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
    elif category == 4:
        print "Now Exiting Serve Tha Bass\nThank You! :]"
        exit()
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
    elif category == 'games':
        return games()
    else:
        return manga()

        
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
    # should i create a class for each bucket?
    # should i treat these as objects instead of lists?
    # Make each list a separate text file?
    backlog = []  # list_item objects in the backlog state
    in_progress = []  # list_item objects in the in_progress state
    complete = []  # list_item objects in the complete state
    
    
    # add functions here
    def __init__(self):
        pass
    
    
    def view(self):
        print "viewing the anime class:\n"
        headers = ['Backlog', 'In Progress', 'Complete']
        data = [headers] + list(zip(self.backlog, self.in_progress, self.complete))
        
        for i, d in enumerate(data):
            line = '|'.join(str(x).ljust(12) for x in d)
            print(line)
            if i == 0:
                print('-' * len(line))
                print i, data
                i = i + 1
        
    
    def add(self):
        print "Please begin adding your desired anime:\n"
        name = raw_input("What is the name of the anime?\n")
        print "Which state is the anime in?\n"
        print "-------------------------------------------------\n"
        print "-- 1. Backlog -- 2. In Progress -- 3. Complete --\n"
        print "-------------------------------------------------\n"
        state = raw_input("Provide the number that corresponds with the state: \n")
        if state == '1':
            state = 'backlog'
        elif state == '2':
            state = 'in_progress'
        elif state == '3':
            state = 'complete'
        else:
            print "Please provide a valid input."
        genre = raw_input("What genre is this anime?\n")
        tag = raw_input("Provide a tag for this anime\n")
        
        item = listItem(name, 'anime', state, genre, tag)
        
        print "you have added: \n"
        print(item.name)
        print(item.category)
        print(item.state)
        print(item.genre)
        print(item.tag)
        
        if item.state == 'backlog':
            self.backlog.append(item.name)
            print "added to backlog: \n"
            print self.backlog
        elif item.state == 'in_progress':
            self.in_progress.append(item)
            print "added to in_progress: \n"
            print self.in_progress
        else:
            self.complete.append(item)
            print "added to complete: \n"
            print self.complete
            
        # return to main menu
        return serve_tha_bass.execute(serve_tha_bass.startup(), serve_tha_bass.choose())
        
        
        
        
    def change_state(self):
        pass
    
    def delete(self):
        pass
    
        
        
    def get_func(self, action):
        if action == 'view':
            return self.view()
        elif action == 'add':
            return self.add()
        elif action == 'state':
            return self.change_state()
        elif action == 'delete':
            return self.delete()
        elif action == 'menu':
            return serve_tha_bass.execute(startup(), choose())
        elif action == 'quit':
            return sys.exit(0)
        else:
            print "Please provide a valid input."        
        
    
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
    def __init__(self):
        pass
    
    
    def view(self):
        print "viewing the manga class"
        
        
    def get_func(self, action):
        if action == 'view':
            return self.view()
            
    
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
    def __init__(self):
        pass
    
    
    def view(self):
        print "viewing the game class"
        
        
    def get_func(self, action):
        if action == 'view':
            return self.view()
        
