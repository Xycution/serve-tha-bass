"""
Brief:
    select_action.py - Contains the functions necessary to act upon list items
        in various ways

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
import select_category
import list_item


#bass = work()
action = select_category.list.select()

class select():
   # def view(self.initial):
    #    if self.initial == 'anime'
     #   print action.anime
    @classmethod
    def select(action):
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
        
        print """\n
        -----------       --------      -----------------        ------------       ----------
        -- 1. View   --  -- 2. Add  --  --  3. Change State  --  --  4. Delete  --  --  5. Quit  --
        -----------       --------      -----------------        ------------       ----------
        """
        action = raw_input('Please select an action number')
        
        if action == '1':
            view(action)
            
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
            -
            """
            
            print select_category.list.anime
            
            
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



# def change_state(list_item, category, current_state, new_state)

# def delete(list_item)
