from flask import Flask, request, jsonify, render_template
import logging
import requests

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] | [%(levelname)s] | %(message)s")

app = Flask(__name__, template_folder='client/')


@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")


@app.route('/ping', methods=["GET"])
def ping():
    ip = request.remote_addr
    ip2 = request.environ['REMOTE_ADDR']
    port = request.environ.get('REMOTE_PORT')
    logging.info("The IP addess is of raspberry pi is : {}".format(ip))
    logging.info({'ip': ip, 'ip2': ip2, 'port': port})
    requests.post("http://{}:{}".format(ip2, port))
    return jsonify({'ip': ip, 'ip2': ip2, 'port': port}), 200


@app.route('/', methods=["POST"])
def ack():
    ip = request.remote_addr
    logging.info("ACK my ip address is : {}".format(ip))
    return jsonify({'ip': ip}), 200


@app.route('/test')
def test():
    a = requests.get("https://raspberrypi-switch.herokuapp.com/ping")
    return "sent"


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
