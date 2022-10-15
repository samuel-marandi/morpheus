
from http.server import (HTTPServer)
from http_handler import (MyServer)

# import time
hostName = "localhost"
serverPort = 8888  # You can choose any available port; by default, it is 8000

if __name__ == "__main__":
    webServer =  HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

try:
    webServer.serve_forever()
except KeyboardInterrupt:
    pass
    webServer.server_close()
    print("Server Stopped");
