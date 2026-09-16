
from enum import Enum, auto


# Enumeration for SignalRegistry platform interface types
class InterfaceType(Enum):
  REGISTRY_WEBSOCKET = auto()
  NODE_WEBSOCKET     = auto()
  
class SignalRegistry:
  
  # Class constructor which initializes the SignalRegistry platform interface kwargs 
  def __init__(self, **kwargs):
    # If 'userId', 'sessionId', and 'registryId' are provided, it is registry socket connection
    if kwargs.get("sessionId") and kwargs.get("userId") and kwargs.get("registryId"):
      self.sessionId     = kwargs.get("sessionId")
      self.userId        = kwargs.get("userId")
      self.registryId    = kwargs.get("registryId")
      self.interfaceType = InterfaceType.REGISTRY_WEBSOCKET
    # If 'registryId' and 'nodeId' are provided, it is node socket connection
    elif kwargs.get("registryId") and kwargs.get("nodeId"):
      self.registryId    = kwargs.get("registryId")
      self.nodeId        = kwargs.get("nodeId")
      self.interfaceType = InterfaceType.NODE_WEBSOCKET
    else:
      raise ValueError("Invalid combination of arguments for SignalRegistry initialization")
