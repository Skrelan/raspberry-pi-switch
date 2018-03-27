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
    logging.info("The IP addess is of raspberry pi is : {}".format(ip))
    requests.post(ip + ":5000/ping")
    return jsonify({'ip': ip}), 200


@app.route('/ping', methods=["POST"])
def ack():
    ip = request.remote_addr
    logging.info("ACK my ip address is : {}".format(ip))
    return jsonify({'ip': ip}), 200


if __name__ == '__main__':
    app.run(debug=True)
