#!/usr/bin/env python
import SimpleHTTPServer

from BaseHTTPServer import HTTPServer


class RequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        request_headers = self.headers.dict
        content = "It's easier to ask forgiveness than it is to get permission.\n"
        fwd_for = "X-Forwarded-For: %s" % request_headers.get('x-forwarded-for', None)
        real_ip = "X-Real-IP: %s" % request_headers.get('x-real-ip', None)
        self.wfile.write("\n".join([content, fwd_for, real_ip]))
        return


def main():
    port = 8000
    print('Listening on localhost:%s' % port)
    server = HTTPServer(('', port), RequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
