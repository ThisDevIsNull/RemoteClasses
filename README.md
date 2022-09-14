# RemoteClasses
Android Rat Remote Classes

Create An object :

from Reciver import Recv
App = Recv(IP = "127.0.0.1" , PORT = 8080)

Set The Throttle For Connection :

App.set_throttle(ReqsPerMinute = 3) # Set a limit of 3 packets per minute

Get Update :

while True:
    print(App.get_update())
    
    
