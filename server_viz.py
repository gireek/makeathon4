from threading import Thread
from server.viz_server import app, start

# def run():
#     app.run("0.0.0.0", 5000,threaded=True)
# Thread(target=run).start()
Thread(target=start).start()
