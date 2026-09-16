# ruff: noqa: N999
from importlib.metadata import version

from SignalRegistry.core import hello

__version__ = version("SignalRegistry")

__all__ = ["hello"]