from threading import Thread
from server.viz_server import start

Thread(target=start).start()
