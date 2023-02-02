"""from Aaron Maxwell.
analyze the file path to get extension. chose the correct reader class based on that.
and finally create the appropriate reader object."""
import abc
class ImageReader(metaclass=abs.ABCMeta):
    def __init__(self, path):
        self.path = path
    @abs.abstractmethod
    def read(self):
        pass # should be implemented in subclass
    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.path)

class GIFReader(ImageReader):
    def read(self):
        "Read a GIF"

class JPEGReader(ImageReader):
    def read(self):
        "Read a GIF"

class PNGReader(ImageReader):
    def read(self):
        "Read a GIF"

class RawByteDeader(ImageReader):
    def read(self):
        "Read raw bytes"

def extension_of(path):
    position_of_last_dot = path.rfind('.')
    return path[position_of_last_dot+1:]

READERS =
{'git':GIFReader,
 'jpg':JPEGReader,
 'png': PNGReader}

def get_image_reader(path):
    try:
        reader_class = READERS[extension_of(path)]
    except KeyError:
        reader_class = RawByteDeader
    return reader_class(path)

def get_image_reader(path):

    return READERS.get(extension_of(path), RawByteDeader)