#!/usr/bin/env python
"""
Brief:
    serve-tha-bass.py - Contains the primary flow of the application execution.

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


import select-action
import select-category
import list-item

action = list()
choice = something.select() ## << This isn't being recognized when running for some reason

class work(object):
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
    def startup(self): # this is the first thing to show when running
        print """\n
        \n
          -----------          -----------------         ------------
        -- 1. Anime   --     -- 2. Video Games  --     --  3. Manga  --
          -----------          -----------------         ------------

        """
        select =  raw_input('Please select a category:\n ').lower()

        if select == 1 or 'anime' or 'Anime':
            self.initial = 'anime'
        elif select == 2 or 'Video Games' or 'video games':
            self.initial = 'video_games'
        elif select == 3 or 'Manga' or 'manga':
            self.initial = 'manga'
        else:
            print "Please input a valid selection"

    def choose(self):

        print """\n
          -----------          -----------------         ------------
        -- 1. view   --     -- 2. Video Games  --     --  3. Manga  --
          -----------          -----------------         ------------
        """
        select = raw_input('Please select an action')

        if select == 1 or 'view':
            choice.view()






workin = work()


workin.startup()
workin.choose()

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

    # ask user what they want to do

    # execute actions

    # end


if  __name__ =='__main__':main()
