# ruff: noqa: N999
from importlib.metadata import version

from SRCli.core import SRCli

__version__ = version("SRCli")

__all__ = ["SRCli", "__version__"]