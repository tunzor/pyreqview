import os
from datetime import datetime
from flask import Flask, request

flask_host = os.getenv('FLASK_HOST', default='localhost')
flask_port = os.getenv('FLASK_PORT', default=5000)

app = Flask(__name__, template_folder=".")

requests_list = []

def formatted_requests_list():
    output = ''
    for request in requests_list:
        output += '<tr>'
        for value in request:
            output += f'<td class="text-nowrap">{value}</td>'
        output += '</tr>'
    return output

@app.route('/', methods=['GET'])
def index():
    return f'''
        <html>
        <head>
        <title>PyReqView - Request Viewer</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        </head>
        <body class="m-3">
        <h1>&#128270 Request Viewer &#128269</h1>
        <p>Send a request to <code>/request</code>, then refresh this page.</p>
        <p>The <code>DELETE</code>, <code>GET</code>, <code>PATCH</code>, <code>POST</code>, and <code>PUT</code> methods are all accepted.</p> 
        <p>For example, open <a href="/request?foo=bar"><code>/request?foo=bar</code></a> to send a GET request from your browser.</p>
        <h2>Values sent</h2>
        <table class="table table-striped table-bordered">
        <tr>
        <td>Timestamp</td>
        <td>Method</td>
        <td>URL arguments</td>
        <td>Data</td>
        <td>Headers</td>
        </tr>
        {formatted_requests_list()}
        </table>
        </body>
        </html>
    '''

@app.route('/request', methods=['DELETE', 'GET', 'PATCH', 'POST', 'PUT'])
def send_request():
    requests_list.append([
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        request.method,
        request.args.to_dict(),
        request.data.decode("utf-8"),
        request.headers
        ])
    return f"{request.method} request received", 201

if __name__ == "__main__":
    app.run(host=flask_host,port=flask_port)