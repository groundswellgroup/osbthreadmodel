from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import threading
import time


class Handler(BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        time.sleep(40)
        self.send_response(200)
        self.end_headers()
        message = '<response>' + threading.currentThread().getName() + '</response>'
        self.wfile.write(message)
        self.wfile.write('\n')
        return

    def do_POST(self):
        self.do_GET()

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

if __name__ == '__main__':
    server = ThreadedHTTPServer(('localhost', 8000), Handler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
