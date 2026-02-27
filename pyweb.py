# Python Web Server

# Importing necessary libraries
import http.server
import socketserver

# Defining the handler
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes('<html><body><h1>Welcome to the Python Web Server!</h1></body></html>', 'utf8'))

# Setting up the server
PORT = 8080
handler_object = MyHttpRequestHandler

with socketserver.TCPServer(('', PORT), handler_object) as httpd:
    print(f'Serving at port {PORT}')
    httpd.serve_forever()