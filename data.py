from Process import EditWindow
from tkinter import Tk
from tkinter import Frame

window_width = 1366
window_height = 720

EDIT_WINDOW:EditWindow = None
ROOT:Tk = None
CONTENT_WINDOW:Frame = None
EDIT_FRAME:Frame = None
EDIT_VIEW_APP = None
LAYER_FRAME:Frame = None
SCROLL_LAYER_FRAME:Frame = None
LAYER_SCROLLER = None
FILTERS:dict = None

# Colors
PEN_COLOR:str = 'Black'
EDIT_BG_COLOR = '#343a40'
CONTENT_BG_COLOR = '#6c757d'

#edit
MODE = 'Hand'