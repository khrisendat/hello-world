from flask import Flask, request
import socket

app = Flask(__name__)

@app.route('/')
def hello_world():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    client_ip = request.remote_addr
    return f'Hello, World!\nServer hostname: {hostname}\nServer IP: {local_ip}\nClient IP: {client_ip}'

if __name__ == '__main__':
    # Try a different port that might be allowed
    port = 3000
    app.run(host='0.0.0.0', port=port, debug=True)