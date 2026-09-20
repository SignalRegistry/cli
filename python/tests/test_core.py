
from importlib.metadata import version


def test_package_metadata_uses_src_cli_name():
    assert version("SRCli") == "0.0.1"


