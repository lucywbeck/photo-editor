"""
Author: Lucy Beck
Date: January 22, 2021
"""
from PIL import Image as PIL_Image


class Image(object):
    """
    A class that stores image data.
    """
    @property
    def original_source(self):
        """
        The original image source

        Invariant: source is a valid image file
        """
        return self._original_source

    @property
    def current_source(self):
        """
        The current image source

        Invariant: source is a valid image file
        """
        return self._current_source

    @property
    def width(self):
        """
        The width of the image

        Invariant: value is a number (int or float) > 0
        """
        return self._width

    @property
    def height(self):
        """
        The height of the image

        Invariant: value is a number (int or float) > 0
        """
        return self._height

    @property
    def current_pix(self):
        """
        The data at a pixel level

        Invariant: current_pix is a 2-dimensional list of 3-element tuples
        """
        return self._pix_history[-1]

    def __init__(self,file):
        """
        Initializes an Image.

        Parameter file: The image file
        Precondition: file is a valid image file
        """
        im = PIL_Image.open(file)
        self._original_source = file
        self._current_source = 'new.png'
        self._width = im.size[0]
        self._height = im.size[1]
        self._original_pix = im.load()
        self._pix_history = [self._original_pix]

    def update_pix_history(self,pix):
        """
        Adds the most recent edit to the pixel history

        If the number of elements in the pixel history exceeds 50 items,
        the first element in the list will be removed from history.
        """
        self._pix_history.append(pix)
        if len(self._pix_history) > 50:
            self._pix_history.pop()

    def undo(self):
        """
        Removes the most recent edit from the pixel history
        """
        if len(self._pix_history) > 1:
            self._pix_history.pop()

    def reset(self):
        """
        Removes all edits from the pixel history
        """
        self._pix_history = [self._original_pix]
