
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
        

        self.ws = None
        self.ws_type = None

    def connect(self, on_open=None, on_message=None):
        # Test if on_open and on_message callbacks are provided and they are callable
        if (on_open and callable(on_open)) and (on_message and callable(on_message)):
            def on_open_wrapper(ws):
                on_open(ws)
            def on_message_wrapper(ws, message):
                on_message(ws, message)
            self.ws = websocket.WebSocketApp(self.host, on_open=on_open_wrapper, on_message=on_message_wrapper)
            self.ws.run_forever(dispatcher=rel, reconnect=5)
            rel.signal(2, rel.abort)  # Keyboard Interrupt
            rel.dispatch()
        elif on_open == None and on_message == None:
            self.ws = websocket.WebSocket()
            self.ws.connect(self.host)
        else:   
            raise RuntimeError("Unexpected combination of on_open and on_message callbacks.")
    
    def close(self):
        if self.ws:
            self.ws.close()
            
    def send(self, message):
        if isinstance(self.ws, websocket.WebSocket):
            self.ws.send(message)
        else:
            raise TypeError("Unexpected WebSocket type.")
    
    def recv(self):
        if isinstance(self.ws, websocket.WebSocket):
            return self.ws.recv()
        else:
            raise TypeError("Unexpected WebSocket type.")
    
    def __del__(self):
        self.close()
        
    
