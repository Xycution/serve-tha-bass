#!/usr/bin/env python
#import select-action
#import select-category as something

action = list()
choice = something.select() ## << This isn't being recognized when running for some reason

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