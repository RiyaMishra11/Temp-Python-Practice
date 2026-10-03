"""101 - Simple HTTP Server Demo"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

HOST = "127.0.0.1"
PORT = 8000

class RequestHandler(BaseHTTPRequestHandler):
    def send_json(self, data, status=200):
        body = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/":
            self.send_json({
                "message": "Python HTTP server is running",
                "endpoint": "/api/status"
            })
        elif self.path == "/api/status":
            self.send_json({
                "status": "ok",
                "service": "python-demo-server"
            })
        else:
            self.send_json({"error": "Not found"}, 404)

    def log_message(self, format, *args):
        print(f"[HTTP] {self.address_string()} - {format % args}")

def main():
    server = HTTPServer((HOST, PORT), RequestHandler)
    print(f"Server: http://{HOST}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Stopping server...")
    finally:
        server.server_close()

if __name__ == "__main__":
    main()
