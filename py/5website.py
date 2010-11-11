# As you might guess, provides a simple HTTP server.
import SimpleHTTPServer

# Allows us to attach to this machine and pass requests to the HTTP server.
import SocketServer

# A blank string for the host indicates the local computer, and port 8000 is
# a standard alternative HTTP port.
CONNECTION_SETTINGS = ('', 8000)

# Create the actual server.
httpd = SocketServer.TCPServer(
    CONNECTION_SETTINGS,
    SimpleHTTPServer.SimpleHTTPRequestHandler
)

httpd.serve_forever()