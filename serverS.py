import socket
import threading
import SocketServer
import json
import pygame
import winsound

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        pozicija = int(self.request.recv(1024).strip())
        pom = []
        while pozicija==len(test.matrica): b=1;
        for i in range(pozicija, len(test.matrica)):
            pom.append(test.matrica[i])
        self.request.sendall(json.dumps(pom))

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

class Joystick:
  matrica=[]

  def __init__(self):
    pygame.joystick.init()
    pygame.display.init()
    self.joystick = pygame.joystick.Joystick(0)
    self.joystick.init()
	
  def ObradaEventa(self,e):
     if e.type == pygame.JOYAXISMOTION:
           x=(-1)*round(self.joystick.get_axis(0),2)
           y=(-1)*round(self.joystick.get_axis(1),2)
           self.matrica.append([x,y])
           motorOutput(y,x)
     else:
        pass

  def Horn(self,e):
     if e.type == pygame.JOYBUTTONDOWN:
        if (e.dict['button'] == 0):
            winsound.PlaySound('horn.wav',winsound.SND_FILENAME) 
    
  def Upravljanje(self):
    while True:
        e = pygame.event.wait()
        if (e.type == pygame.JOYAXISMOTION):
            self.ObradaEventa(e)
        elif e.type == pygame.JOYBUTTONDOWN:
            self.Horn(e)
            
            
test=Joystick()
    
HOST, PORT = "localhost", 5000
server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
server_thread = threading.Thread(target=server.serve_forever)
# Exit the server thread when the main thread terminates
server_thread.daemon = True
server_thread.start()
print "Server loop running in thread:", server_thread.name

def step():
     test.Upravljanje()

def brainStop():
    pass


def shutdown():
    pass
