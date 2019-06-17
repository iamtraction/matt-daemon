#!/usr/bin/env python3

import sys
import http.server
import socketserver

ADDRESS = "0.0.0.0"
PORT = 3333

if len(sys.argv) >= 3:
    ADDRESS = sys.argv[1]
    PORT = int(sys.argv[2])
elif len(sys.argv) >= 2:
    PORT = int(sys.argv[1])

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer((ADDRESS, PORT), Handler) as httpd:
    try:
        print("\033[92m")
        print("You can now view this direcotry in the browser:")
        print("\033[0m")
        print("    http://localhost:\033[1m{0}".format(PORT))
        print("\033[0m\033[1m")
        print("Note that Matt Daemon is not recommended for production.")
        print("It only implements basic security checks.")
        print("\033[0m")
        httpd.serve_forever()
    except KeyboardInterrupt as e:
        httpd.shutdown()
        print("\033[91m")
        print("Matt Daemon terminated.")
        print("\033[0m")
