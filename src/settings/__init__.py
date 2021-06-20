# Load default settings from default.py
from .default import *

try:
    # Load settings from local.py if one exists
    from .local import *
except ImportError:
    pass
