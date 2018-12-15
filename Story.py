"""
Program name: Story.py
What does it do: Story.py serves as the template for stories. We can load stories
in from a dictionary and then use them, based on their keys.
"""

class Story(object):
    def __init__(self, stories_dictionary, commentary_dict, char_status):
        self.stories_dict = stories_dict
        self.commentary_dict = commentary_dict
        self.good_points = 0
        self.bad_points = 0
        self.health_points = 100
        # Toggles between healthy, unhealthy, poisoned, sick, or dead
        self.char_status = char_status


    # Methods to append and subtract points from score to be called in game
    def append_bad_score(self):
        self.bad_points += 1

    def subtract_bad_score(self):
        self.bad_points -= 1

    def append_good_score(self):
        self.good_points += 1

    def subtract_good_score(self):
        self.good_points -= 1
