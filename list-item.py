"""
Brief:
    -

Description:
    -

Methods:
    -

Return Value(s):
    -

Example:
    -

Author(s):
    -
"""

import serve-tha-bass
import select-category
import select-action


class listItem:
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
    def __init__(self, name, category, state, genre, tag):
        self.name = name
        self.category = category
        self.state = state
        self.genre = genre
        self.tag = tag

    def get_name(self):
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
        return self.name

    def set_name(self):
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
        # self.name = raw_input ask for name/title
        pass

    def get_category(self):
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
        return self.category

    def set_category(self):
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
        # self.category = raw_input ask for category
        pass

    def get_state(self):
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
        return self.state

    def set_state(self):
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
        # self.state = raw_input ask which state to move it to
        pass

    def get_genre(self):
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
        return self.genre

    def set_genre(self):
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
        # self.genre = raw_input ask for the genre
        pass
