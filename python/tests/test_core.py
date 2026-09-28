
from importlib.metadata import version


def test_package_metadata_uses_SRClient_name():
    assert version("SRClient") == "0.0.1"


def test_package_metadata_uses_SRClient_version():
    from SRClient import __version__
    assert __version__ == "0.0.1"


def test_SRClient_importable():
    import SRClient
    assert SRClient is not None
    
def test_SRClient_has_version_attribute():
    import SRClient
    assert hasattr(SRClient, "__version__")
    
def test_SRClient_version_matches_package_metadata():  
    from importlib.metadata import version

    import SRClient
    assert SRClient.__version__ == version("SRClient")
    
def test_SRClient_constructor_node_websocket():
    # Read environment variables for registry and node IDs
    import os
    if os.getenv("HOST_TYPE") == "remote":
        registryId = os.getenv("REGISTRY_ID_REMOTE")
        nodeId     = os.getenv("NODE_ID_REMOTE")
    else:
        registryId = os.getenv("REGISTRY_ID_LOCAL")
        nodeId     = os.getenv("NODE_ID_LOCAL")
    from SRClient import SRClient
    instance = SRClient(registryId=registryId, nodeId=nodeId)
    assert instance is not None
    
def test_SRClient_constructor_registry_websocket():
    import os
    if os.getenv("HOST_TYPE") == "remote":
        sessionId  = os.getenv("SESSION_ID_REMOTE")
        userId     = os.getenv("USER_ID_REMOTE")
        registryId = os.getenv("REGISTRY_ID_REMOTE")
    else:
        sessionId  = os.getenv("SESSION_ID_LOCAL")
        userId     = os.getenv("USER_ID_LOCAL")
        registryId = os.getenv("REGISTRY_ID_LOCAL")
    print(f"Registry ID: {registryId}, Session ID: {sessionId}, User ID: {userId}")
    from SRClient import SRClient
    instance = SRClient(sessionId=sessionId, userId=userId, registryId=registryId)
    assert instance is not None
 
 
def test_SRClient_node_websocket_instance():
    import os
    if os.getenv("HOST_TYPE") == "remote":
        registryId = os.getenv("REGISTRY_ID_REMOTE")
        nodeId     = os.getenv("NODE_ID_REMOTE")
    else:
        registryId = os.getenv("REGISTRY_ID_LOCAL")
        nodeId     = os.getenv("NODE_ID_LOCAL")
    
    from SRClient import SRClient
    instance = SRClient(registryId=registryId, nodeId=nodeId)
    def on_open():
        print("WebSocket connection opened.")
    def on_message(message):
        print("Received data:", message)
    instance.connect(on_open=on_open, on_message=on_message)
    assert instance is not None
  