from threading import Thread
from DataBase import DataBase
import socket
import json
from time import sleep
from os import system

class JsonParser:
    def __init__(self , Data : str) -> None:
        self.Data = Data
    def __GetJson__(self) -> json:
        return json.loads(self.Data)

class Recv:
    def __init__(self , IP : str , PORT : int) -> None:
        self.reqpermin = None
        self.IP = IP
        self.PORT = PORT
        self.number = 0
        self.SOCKET = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
        self.SOCKET.bind((self.IP,self.PORT))
    def set_throttle(self , ReqsPerMinute : int) -> None:
        self.reqpermin = ReqsPerMinute
        Thread(target=self._Throttle , daemon=True).start()
    def _Throttle(self) -> None:
        try:
            while True:
                self.number = 0
                sleep(self.reqpermin)
        except:
            pass
    def get_update(self) -> None:
        try:
            self.Packet , self.Addr = self.SOCKET.recvfrom(4069)
            self.Null = JsonParser(self.Packet.decode("UTF-8"))
            self.Parsed = self.Null.__GetJson__()
            self.SOCKET.sendto(b"200" , self.Addr)
            if self.reqpermin != None: #Throttle setted
                if self.number <= self.reqpermin:
                    self.number = self.number + 1
                    return self.Parsed
                else:
                    print("\nPacket Declined From {} Address !\n".format(self.Addr))
                    self.SOCKET.sendto(b"429" , self.Addr)
            else: #Throttle Not Set
                return self.Parsed
        except Exception as error:
            return error
        
