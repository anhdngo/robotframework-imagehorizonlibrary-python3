from interaction import *
from recognition import *

class ImageHorizonLibraryException(Exception):
    pass

try:
    import pyautogui
except ImportError:
    raise ImageHorizonLibraryException('Please install pyautogui')

try:
    import robot
except ImportError:
    raise ImageHorizonLibraryException('Please install Robot Framework')


class ImageHorizonLibrary(_RecognizeImages, _Keyboard):
    def __init__(self, reference_folder=None):
        self.reference_folder = reference_folder