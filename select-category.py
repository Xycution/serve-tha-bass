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

import serve-tha-bass
import select-action
import list-item


class list:
# anime list
anime = [1: 'Code Geass', 2: 'World Trigger', 3: 'One Piece']


# video games list
vidgames = [ 1: 'Pokemon', 2: 'XCOM', 3: 'Conflict: Global Terror']


# manga list
manga = [ 1: 'Attack on Titan', 2: 'One Piece', 3: 'My Hero Academia']


def select_category():
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
    \n
      -----------          -----------------         ------------
    -- 1. Anime   --     -- 2. Video Games  --     --  3. Manga  --
      -----------          -----------------         ------------

    """
    category = raw_input('Please select a category:\n ').lower()

    if category == 1 or 'anime' or 'Anime':
        self.initial = 'anime'
    elif category == 2 or 'Video Games' or 'video games':
        self.initial = 'video_games'
    elif category == 3 or 'Manga' or 'manga':
        self.initial = 'manga'
    else:
        print "Please input a valid selection"




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
