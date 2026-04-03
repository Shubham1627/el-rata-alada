from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import uuid
import sys
from urllib.parse import urlparse, parse_qs

chats = {}  # token → messages (later Redis)

class Handler(BaseHTTPRequestHandler):

    # ✅ Handle GET requests
    def do_GET(self):
        parsed = urlparse(self.path)

        if parsed.path == "/create-chat":
            token = str(uuid.uuid4())[:8]
            chats[token] = []

            response = {
                "token": token,
                "friend_url": f"http://localhost:8081/?chat={token}"
            }

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

        else:
            self.send_response(404)
            self.end_headers()

    # ✅ Handle POST requests
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode()

        parsed = urlparse(self.path)

        if self.path == "/admin/message":
            print(f"🦇 Admin: {body}")
            sys.stdout.flush()

        elif self.path == "/friend/message":
            print(f"👤 Friend: {body}")
            sys.stdout.flush()

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

    def log_message(self, format, *args):
        return


if __name__ == "__main__":
    print("✅ Python backend running on port 8000")
    sys.stdout.flush()
    HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()

