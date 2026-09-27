
from importlib.metadata import version


def test_package_metadata_uses_src_cli_name():
    assert version("SRClient") == "0.0.1"


def test_package_metadata_uses_src_cli_version():
    from SRClient import __version__
    assert __version__ == "0.0.1"


def test_src_cli_importable():
    import SRClient
    assert SRClient is not None
    
def test_src_cli_has_version_attribute():
    import SRClient
    assert hasattr(SRClient, "__version__")
    
def test_src_cli_version_matches_package_metadata():  
    from importlib.metadata import version

    import SRClient
    assert SRClient.__version__ == version("SRClient")
    
def test_SRClient_constructor_node_websocket():
    from SRClient import SRClient
    registryId = "1f13e918d657c7f25ec1ec63b1e7ace0"
    nodeId     = "a9793c033ea0e3a0312d829e92b7b901"
    # instance = SRClient(sessionId=sessionId, userId=userId, registryId=registryId)
    instance = SRClient(registryId=registryId, nodeId=nodeId)
    # instance.connect()
    assert instance is not None
    
def test_SRClient_constructor_registry_websocket():
    from SRClient import SRClient
    sessionId  = "example_session_id"
    userId     = "example_user_id"
    registryId = "1f13e918d657c7f25ec1ec63b1e7ace0"
    instance = SRClient(sessionId=sessionId, userId=userId, registryId=registryId)
    assert instance is not None
 
 
def test_SRClient_node_websocket_instance():
    from SRClient import SRClient
    registryId = "1f13e918d657c7f25ec1ec63b1e7ace0"
    nodeId     = "a9793c033ea0e3a0312d829e92b7b901"
    instance = SRClient(registryId=registryId, nodeId=nodeId)
    def on_open():
        print("WebSocket connection opened.")
    def on_message(message):
        print("Received data:", message)
    instance.connect(on_open=on_open, on_message=on_message)
    assert instance is not None
  