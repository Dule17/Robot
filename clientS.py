import socket

#adresa servera i port
HOST, PORT = "localhost", 5000
class Klijent:
    def __init__(self):
       self.duzina=0

    def vozi(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        try:
          sock.sendall(str(self.duzina))
          response = sock.recv(100000000) #mozda treba veci broj (broj bajtova)
          niz = eval(response.strip())
          self.duzina = self.duzina + len(niz)
          for i in range(0, len(niz)):
             motorOutput(niz[i][1], niz[i][0])
        finally:
              sock.close()

k=Klijent()
def step():
    k.vozi()

def brainStop():
    pass

def shutdown():
    pass
