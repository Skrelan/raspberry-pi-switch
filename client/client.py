from websocket import create_connection
import time

url = {"local": "ws://backend:5000/connect-better", "web": ""}
KEY = ""


def web_server(url):
    ws = create_connection(url)
    ws.send(KEY)
    while True:
        try:
            r = ws.recv()
            print r
            if r == '1':
                print "Light ON"
            elif r == '0':
                print "Light OFF"
            else:
                print "Invalid request"
            ws.send("State is : {}".format(r))
            time.sleep(1)
        except Exception as e:
            print e
            ws.shutdown()
            return
    ws.shutdown()


def worker(url):
    print "setting up socket connection with {}".format(url)
    while True:
        try:
            web_server(url)
        except Exception as e:
            print "{}".format(e)
        time.sleep(1)


if __name__ == "__main__":
    # web_server(url)
    worker(url["local"])
