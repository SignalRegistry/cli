
from importlib.metadata import version


def test_package_metadata_uses_src_cli_name():
    assert version("SRCli") == "0.0.1"


def test_package_metadata_uses_src_cli_version():
    from SRCli import __version__
    assert __version__ == "0.0.1"


def test_src_cli_importable():
    import SRCli
    assert SRCli is not None
    
def test_src_cli_has_version_attribute():
    import SRCli
    assert hasattr(SRCli, "__version__")
    
def test_src_cli_version_matches_package_metadata():  
    from importlib.metadata import version

    import SRCli
    assert SRCli.__version__ == version("SRCli")
    
def test_srcli_constructor_node_websocket():
    from SRCli import SRCli
    registryId = "1f13e918d657c7f25ec1ec63b1e7ace0"
    nodeId     = "a9793c033ea0e3a0312d829e92b7b901"
    # instance = SRCli(sessionId=sessionId, userId=userId, registryId=registryId)
    instance = SRCli(registryId=registryId, nodeId=nodeId)
    # instance.connect()
    assert instance is not None
    
def test_srcli_constructor_registry_websocket():
    from SRCli import SRCli
    sessionId  = "example_session_id"
    userId     = "example_user_id"
    registryId = "1f13e918d657c7f25ec1ec63b1e7ace0"
    instance = SRCli(sessionId=sessionId, userId=userId, registryId=registryId)
    assert instance is not None
 
 
def test_srcli_node_websocket_instance():
    from SRCli import SRCli
    registryId = "1f13e918d657c7f25ec1ec63b1e7ace0"
    nodeId     = "a9793c033ea0e3a0312d829e92b7b901"
    instance = SRCli(registryId=registryId, nodeId=nodeId)
    def on_open():
        print("WebSocket connection opened.")
    def on_message(message):
        print("Received data:", message)
    instance.connect(on_open=on_open, on_message=on_message)
    assert instance is not None
  