
from enum import Flag, auto

import rel
import websocket


# Enumeration for SRCli platform interface types
class InterfaceType(Flag):
  REGISTRY_WEBSOCKET = auto()
  NODE_WEBSOCKET     = auto()
  WEBSOCKET          = REGISTRY_WEBSOCKET | NODE_WEBSOCKET
  
class SRCli:
  
  # Class constructor which initializes the SRCli platform interface kwargs 
  def __init__(self, **kwargs):
    # If 'userId', 'sessionId', and 'registryId' are provided, it is registry socket connection
    if kwargs.get("sessionId") and kwargs.get("userId") and kwargs.get("registryId"):
      self.sessionId     = kwargs.get("sessionId")
      self.userId        = kwargs.get("userId")
      self.registryId    = kwargs.get("registryId")
      self.interfaceType = InterfaceType.REGISTRY_WEBSOCKET
      self.host          = kwargs.get("host", f"wss://api.signalregistry.net/ws?registryId={self.registryId}&sessionId={self.sessionId}&userId={self.userId}")
      
      
    # If 'registryId' and 'nodeId' are provided, it is node socket connection
    elif kwargs.get("registryId") and kwargs.get("nodeId"):
      self.registryId    = kwargs.get("registryId")
      self.nodeId        = kwargs.get("nodeId")
      self.interfaceType = InterfaceType.NODE_WEBSOCKET
      self.host          = kwargs.get("host", f"wss://api.signalregistry.net/ws/node?registryId={self.registryId}&nodeId={self.nodeId}")
    else:
      raise ValueError("Invalid combination of arguments for SRCli initialization")
    
    # Create registry websocket connection here
    if self.interfaceType in InterfaceType.WEBSOCKET:
      self.ws_on_data   = None
      self.ws_connected = False
      self.ws           = websocket.WebSocketApp(self.host)
    #   # Create handler functions for websocket events
    #   def on_message(ws, message):
    #       print(message)

    #   def on_error(ws, error):
    #       print(error)

    #   def on_close(ws, close_status_code, close_msg):
    #       print("### closed ###")

    #   def on_open(ws):
    #       print("Opened connection")
    #   # websocket.enableTrace(True)
    #   self.ws = websocket.WebSocketApp(self.host,
    #                             on_open    = on_open,
    #                             on_message = on_message,
    #                             on_error   = on_error,
    #                             on_close   = on_close)

    #   self.ws.run_forever(dispatcher=rel, reconnect=5, )  
    #   rel.signal(2, rel.abort)  # Keyboard Interrupt
    #   rel.dispatch()
  
  def connect(self):
    if hasattr(self, "ws"):
      if self.ws_on_data:
        self.ws_connected = True
        self.ws.run_forever(dispatcher=rel, reconnect=5, )  
        rel.signal(2, rel.abort)  # Keyboard Interrupt
        rel.dispatch()
      else:
        raise RuntimeError("WebSocket on_data handler is not set.")
  
  def close(self):
    if hasattr(self, "ws"):
      self.ws.close()
      self.ws_connected = False
  
  def __del__(self):
    self.close()
    
  
  def on_data(self, message) -> None:
    def on_message(ws, message):
      self.on_data(message)

    self.ws.on_message = on_message
    self.ws_on_data = True
    print(message)
