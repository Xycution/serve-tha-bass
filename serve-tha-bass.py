#!/usr/bin/env python
#import select-action
#import select-category

class work(object):
    def startup(self): # this is the first thing to show when running
        print """\n
        \n
          -----------          -----------------         ------------
        -- 1. Anime   --     -- 2. Video Games  --     --  3. Manga  --
          -----------          -----------------         ------------

        """
        select =  raw_input('Please select a category:\n ')

        if select == 1 or 'anime' or 'Anime':
            self.category = 'anime'
        elif select == 2 or 'Video Games' or 'video games':
            self.category = 'video_games'
        elif select == 3 or 'Manga' or 'manga':
            self.category = 'manga'
        else:
            print "Please input a valid selection"






workin = work()

    
workin.startup()
    
