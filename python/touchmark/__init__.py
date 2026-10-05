"""Official Python client for the Touchmark API."""

from importlib.metadata import version

from . import models
from ._client import (
    DEFAULT_BASE_URL,
    AsyncTouchmark,
    Touchmark,
    TouchmarkError,
)

__all__ = [
    "DEFAULT_BASE_URL",
    "AsyncTouchmark",
    "Touchmark",
    "TouchmarkError",
    "models",
]
__version__ = version("touchmark")
