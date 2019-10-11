from flask import Flask, render_template, jsonify
import random
import string
from net_scan import scan


app = Flask(__name__)


@app.route('/')
def net_view_welcome():
    return render_template('net_view.html',
                           version=''.join(random.choices(string.ascii_uppercase + string.digits, k=10)))


@app.route('/hosts')
def net_view_main():
    print('* Scanning network')
    hosts = scan()
    print(f'* Deploying hosts: {hosts}')
    return jsonify(hosts)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
