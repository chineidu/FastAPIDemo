import importlib.metadata
from my_app.main import app


# Import the VESRION
__version__ = importlib.metadata.version("my_app")
