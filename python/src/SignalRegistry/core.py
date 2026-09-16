
from enum import Flag, auto

import rel
import websocket


def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("Opened connection")

# Enumeration for SignalRegistry platform interface types
class InterfaceType(Flag):
  REGISTRY_WEBSOCKET = auto()
  NODE_WEBSOCKET     = auto()
  WEBSOCKET          = REGISTRY_WEBSOCKET | NODE_WEBSOCKET
  
class SignalRegistry:
  
  # Class constructor which initializes the SignalRegistry platform interface kwargs 
  def __init__(self, **kwargs):
    # If 'userId', 'sessionId', and 'registryId' are provided, it is registry socket connection
    if kwargs.get("sessionId") and kwargs.get("userId") and kwargs.get("registryId"):
      self.sessionId     = kwargs.get("sessionId")
      self.userId        = kwargs.get("userId")
      self.registryId    = kwargs.get("registryId")
      self.interfaceType = InterfaceType.REGISTRY_WEBSOCKET
      self.host          = kwargs.get("host", "wss://api.signalregistry.net/ws")
      


      
    # If 'registryId' and 'nodeId' are provided, it is node socket connection
    elif kwargs.get("registryId") and kwargs.get("nodeId"):
      self.registryId    = kwargs.get("registryId")
      self.nodeId        = kwargs.get("nodeId")
      self.interfaceType = InterfaceType.NODE_WEBSOCKET
    else:
      raise ValueError("Invalid combination of arguments for SignalRegistry initialization")
    
    # Create registry websocket connection here
    if self.interfaceType == InterfaceType.WEBSOCKET:
      websocket.enableTrace(True)
      ws = websocket.WebSocketApp(self.host,
                                on_open    = on_open,
                                on_message = on_message,
                                on_error   = on_error,
                                on_close   = on_close)

      ws.run_forever(dispatcher=rel, reconnect=5)  
      rel.signal(2, rel.abort)  # Keyboard Interrupt
      rel.dispatch()
