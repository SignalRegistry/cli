# ruff: noqa: N999
from importlib.metadata import version

from SRClient.core import SRClient

__version__ = version("SRClient")

__all__ = ["SRClient", "__version__"]