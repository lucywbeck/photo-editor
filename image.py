from PIL import Image as PIL_Image


class Image(object):
    """
    A class that allows flexible access to an image pixel list.
    """
    @property
    def source(self):
        """
        The image source

        Invariant: source is a valid image file
        """
        return self._source

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
    def pix(self):
        """
        The data at a pixel level

        It can be accessed like a 2-dimensional list of 3-element tuples.

        Invariant: pix is a PixelAccess Object
        """
        return self._pix

    def __init__(self,file):
        """
        Initializes an Image.

        Parameter file: The image file
        Precondition: file is a valid image file
        """
        im = PIL_Image.open(file)
        self._source = file
        self._width = im.size[0]
        self._height = im.size[1]
        self._pix = im.load()
