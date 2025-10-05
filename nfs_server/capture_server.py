from http.server import BaseHTTPRequestHandler, HTTPServer

class CaptureHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"GET request → {self.path}")
        print(f"Headers →\n{self.headers}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        print(f"POST request → {self.path}")
        print(f"Headers →\n{self.headers}")
        print(f"Body → {body.decode(errors='ignore')}\n")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

server = HTTPServer(('0.0.0.0', 80), CaptureHandler)
print("✅ Listening for requests on port 80 (http://127.0.0.1)")
server.serve_forever()

