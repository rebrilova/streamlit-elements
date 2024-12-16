from streamlit_elements.core.frame import new_frame as _new_frame
from streamlit_elements.core.exceptions import *
from streamlit_elements.modules import *
from streamlit_elements.version import __version__

__version__="0.1.0"
def elements(key: str) -> None:
    """Create a Streamlit Elements frame."""
    return _new_frame(key)
