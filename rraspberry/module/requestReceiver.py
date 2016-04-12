import SocketServer
import threading
#for communicate with subPi & MainPi

status = 0

def start():

    class RequestHandler(SocketServer.BaseRequestHandler):
	def handle(self):
	    global status
	    self.data = self.request.recv(1024).strip()
            if self.data == "00":
               status = 1


    server = SocketServer.TCPServer(("192.168.1.3",9001), RequestHandler)

    threading._start_new_thread(server.serve_forever,())
    return 0


def get_status():
    return status

def set_status():
    global status
    status = 0
