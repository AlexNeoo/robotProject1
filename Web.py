from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

resp = "504B03040A000000000033656A561548986526000000260000000900000073706F72742E74787473706F7274616765746573743" \
     "13740676D61696C2E636F6D0D0A53706F727461676537373737504B01023F000A000000000033656A56154898652600000026000" \
     "00009002400000000000000200000000000000073706F72742E7478740A0020000000000001001800E2D0EAE33C53D901149979E43C" \
     "53D90182D8D7E33C53D901504B050600000000010001005B0000004D0000000000"

class HttpGetHandler(BaseHTTPRequestHandler):
    """Обработчик с реализованным методом do_GET."""
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/zip")
        self.send_header("Content-Length", "190")
        self.end_headers()
        # self.wfile.write('<html><head><meta charset="utf-8">'.encode())
        # self.wfile.write('<title>Простой HTTP-сервер.</title></head>'.encode())
        # self.wfile.write('<body>Был получен GET-запрос.</body></html>'.encode())

        data = bytes.fromhex(resp)
        self.wfile.write(data)
        # self.wfile.write("UEsDBAoAAAAAADNlalYVSJhlJgAAACYAAAAJAAAAc3BvcnQudHh0c3BvcnRhZ2V0ZXN0MTdAZ21haWwuY"
        #                  "29tDQpTcG9ydGFnZTc3NzdQSwECPwAKAAAAAAAzZWpWFUiYZSYAAAAmAAAACQAkAAAAAAAAACAAAAAAAAAA"
        #                  "c3BvcnQudHh0CgAgAAAAAAABABgA4tDq4zxT2QEUmXnkPFPZAYLY1+M8U9kBUEsFBgAAAAABAAEAWwAAAE0AAAAAAA==".encode())


def run(server_class=HTTPServer, handler_class=HttpGetHandler):
  print(0x10)
  server_address = ('', 8000)
  httpd = server_class(server_address, handler_class)
  try:
      httpd.serve_forever()
  except KeyboardInterrupt:
      httpd.server_close()


run()
