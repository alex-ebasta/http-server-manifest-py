import SimpleHTTPServer
import SocketServer
port = 3000;
SimpleHTTPServer.SimpleHTTPRequestHandler.extensions_map['.appcache'] = 'text/cache-manifest'
httpd = SocketServer.TCPServer(("", port), SimpleHTTPServer.SimpleHTTPRequestHandler)
print "Serving files in http://localhost:%d." % (port)
httpd.serve_forever()
