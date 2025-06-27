from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)
REQUESTS = Counter('http_requests_total', 'Total HTTP Requests')

@app.route('/')
def home():
    REQUESTS.inc()
    return "Hello from Python App!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
