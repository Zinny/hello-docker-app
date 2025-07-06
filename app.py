from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8080
Handler = SimpleHTTPRequestHandler

with HTTPServer(("", PORT)), Handler) as httpd:
    print(f"serving on port {PORT}")
    httpd.serve.forever()